# main.py — Điểm bắt đầu (Entry point) CLI cho VietLunarCalendar
# ============================================================
"""
Công cụ tạo file iCalendar (.ics) cho lịch âm Việt Nam.

Cách dùng:
    python main.py                          # Tạo file tổng hợp giai đoạn 2026–2060
    python main.py --split                  # Tạo thêm các file riêng lẻ cho từng năm
    python main.py --start 2026 --end 2030  # Tạo lịch cho một khoảng năm tùy chỉnh
    python main.py --year 2027              # Chỉ tạo lịch cho một năm cụ thể
"""
import argparse
import sys
import time
import zipfile
from datetime import datetime, date
from pathlib import Path

try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False

from config import START_YEAR, END_YEAR, OUTPUT_DIR
from ics_generator import LunarCalendarGenerator


# ──────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────

def print_banner():
    banner = r"""
╔══════════════════════════════════════════════════════════╗
║         🌙  LỊCH ÂM VIỆT NAM — iCalendar Generator       ║
║              Múi giờ GMT+7 (Asia/Ho_Chi_Minh)             ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)


def format_size(path: Path) -> str:
    """Trả về kích thước file dạng KB / MB."""
    size = path.stat().st_size
    if size >= 1_048_576:
        return f'{size / 1_048_576:.2f} MB'
    return f'{size / 1024:.1f} KB'


def count_events(filepath: Path) -> int:
    """Đếm số VEVENT trong file .ics."""
    count = 0
    try:
        with open(filepath, 'rb') as f:
            for line in f:
                if line.strip() == b'BEGIN:VEVENT':
                    count += 1
    except Exception:
        pass
    return count


def create_zip_archive(files: list[Path], output_zip: Path):
    """Nén danh sách các file .ics vào một file nén định dạng .zip."""
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, arcname=file.name)
    return output_zip


# ──────────────────────────────────────────────────────────────
# Main logic
# ──────────────────────────────────────────────────────────────

def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description='Tạo file iCalendar (.ics) Lịch Âm Việt Nam',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        '--start', type=int, default=START_YEAR,
        help=f'Năm bắt đầu (mặc định: {START_YEAR})',
    )
    parser.add_argument(
        '--end', type=int, default=END_YEAR,
        help=f'Năm kết thúc (mặc định: {END_YEAR})',
    )
    parser.add_argument(
        '--year', type=int, default=None,
        help='Chỉ tạo file cho 1 năm cụ thể (ghi đè --start / --end)',
    )
    parser.add_argument(
        '--split', action='store_true',
        help='Tạo file riêng cho từng năm (ngoài file tổng hợp)',
    )
    parser.add_argument(
        '--output-dir', type=str, default=OUTPUT_DIR,
        help=f'Thư mục output (mặc định: {OUTPUT_DIR})',
    )
    args = parser.parse_args()

    # Xử lý tham số năm (Mặc định: Năm hiện tại -> +10 năm)
    current_year = date.today().year
    
    if args.year:
        start_year = end_year = args.year
    else:
        # Nếu người dùng không nhập --start, mặc định lấy năm hiện tại
        start_year = args.start if 'start' in [a.dest for a in parser._actions if args.start != START_YEAR] else current_year
        # Nếu không nhập --end, mặc định lấy start + 5 (Theo yêu cầu tối ưu 5 năm)
        end_year = args.end if 'end' in [a.dest for a in parser._actions if args.end != END_YEAR] else (start_year + 5)

    if start_year > end_year:
        print(f'❌ Lỗi: --start ({start_year}) phải nhỏ hơn hoặc bằng --end ({end_year})')
        sys.exit(1)

    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    gen = LunarCalendarGenerator()
    total_files: list[Path] = []

    print(f'📅 Khoảng thời gian : {start_year} → {end_year}')
    print(f'📂 Thư mục output   : {output_path.resolve()}')
    print()

    # ── Tạo file riêng từng năm (nếu yêu cầu) ──────────────
    if args.split or args.year:
        years = range(start_year, end_year + 1)
        iter_years = tqdm(years, desc='Đang tạo file từng năm', unit='năm') \
                     if HAS_TQDM else years

        yearly_files: list[Path] = []
        for year in iter_years:
            t0 = time.time()
            cal = gen.generate_year(year)
            fname = output_path / f'viet_lunar_{year}.ics'
            gen.save(cal, fname)
            yearly_files.append(fname)
            total_files.append(fname)
            elapsed = time.time() - t0
            if not HAS_TQDM:
                print(f'  ✅ {fname.name}  ({format_size(fname)}, {elapsed:.1f}s)')

        # Nén vào file zip nếu dùng --split (nhiều hơn 1 năm)
        if args.split and len(yearly_files) > 1:
            zip_name = output_path / f'viet_lunar_yearly_{start_year}_{end_year}.zip'
            print(f'\n📦 Đang nén {len(yearly_files)} file vào {zip_name.name}...')
            create_zip_archive(yearly_files, zip_name)
            total_files.append(zip_name)
            print(f'  ✅ Đã tạo file zip ({format_size(zip_name)})')

    # ── Tạo file tổng hợp ───────────────────────────────────
    if not args.year:
        suffix = f'{start_year}_{end_year}'
        if start_year == end_year:
            suffix = str(start_year)

        print(f'\n⏳ Đang tạo file tổng hợp {start_year}–{end_year} '
              f'({end_year - start_year + 1} năm)...')
        t0 = time.time()
        cal = gen.generate_range(start_year, end_year)
        fname = output_path / f'viet_lunar_{suffix}.ics'
        gen.save(cal, fname)
        total_files.append(fname)
        elapsed = time.time() - t0
        print(f'  ✅ Hoàn thành trong {elapsed:.1f}s')

    # ── Tổng kết ────────────────────────────────────────────
    print()
    print('═' * 55)
    print('📊 KẾT QUẢ:')
    for fp in total_files:
        n_events = count_events(fp)
        print(f'   📄 {fp.name}')
        print(f'      → {n_events:,} events  |  {format_size(fp)}')
    print('═' * 55)
    print()
    print('💡 Hướng dẫn import:')
    print('   Google Calendar : calendar.google.com → Cài đặt → Import')
    print('   Apple Calendar  : File → Import...')
    print('   Outlook         : File → Open & Export → Import/Export')
    print()
    print('🎉 Hoàn thành!')


if __name__ == '__main__':
    main()
