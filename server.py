# server.py — Máy chủ HTTP API cục bộ cho VietLunarCalendar
# ============================================================
import json
import os
import shutil
import time
import zipfile
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse

from config import START_YEAR, END_YEAR, OUTPUT_DIR
from ics_generator import LunarCalendarGenerator

PORT = 8000
BASE_DIR = Path(__file__).parent.resolve()
WEB_DIR = BASE_DIR / 'web'
OUTPUT_PATH = BASE_DIR / 'output'


# ──────────────────────────────────────────────────────────────
# Helpers (Sao chép từ main.py để đồng bộ)
# ──────────────────────────────────────────────────────────────

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
    """Nén danh sách các file vào một file nén định dạng .zip."""
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, arcname=file.name)
    return output_zip


# ──────────────────────────────────────────────────────────────
# HTTP Request Handler
# ──────────────────────────────────────────────────────────────

class LunarCalendarAPIHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # Tắt bớt log request mặc định để terminal sạch sẽ, đáng yêu
        pass

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        # 1. Phục vụ giao diện chính web/index.html
        if path in ('/', '/index.html'):
            html_file = WEB_DIR / 'index.html'
            if html_file.exists():
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                with open(html_file, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error_response(404, "Không tìm thấy giao diện index.html")
            return

        # 2. Phục vụ việc tải file trong thư mục output/
        if path.startswith('/output/'):
            filename = os.path.basename(path)
            file_path = (OUTPUT_PATH / filename).resolve()

            # Bảo mật: Đảm bảo file được tải nằm trong thư mục output/
            if file_path.exists() and file_path.parent == OUTPUT_PATH:
                self.send_response(200)
                
                # Cấu hình MIME type thích hợp
                if filename.endswith('.ics'):
                    self.send_header('Content-Type', 'text/calendar; charset=utf-8')
                elif filename.endswith('.zip'):
                    self.send_header('Content-Type', 'application/zip')
                else:
                    self.send_header('Content-Type', 'application/octet-stream')
                
                self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
                self.end_headers()
                
                with open(file_path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error_response(404, "Không tìm thấy file kết quả yêu cầu.")
            return

        # 3. Các đường dẫn khác báo lỗi 404
        self.send_error_response(404, "Đường dẫn không hợp lệ.")

    def do_POST(self):
        if self.path == '/api/generate':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)

            try:
                params = json.loads(post_data.decode('utf-8'))
                start_year = int(params.get('start', START_YEAR))
                end_year = int(params.get('end', END_YEAR))
                split = bool(params.get('split', False))

                if start_year > end_year:
                    self.send_json_response(200, {
                        "success": False,
                        "error": "Năm bắt đầu phải nhỏ hơn hoặc bằng năm kết thúc!"
                    })
                    return

                # Khởi tạo tiến trình tạo lịch âm
                OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
                gen = LunarCalendarGenerator()
                total_files: list[Path] = []
                response_files = []

                # ── 1. Tạo file riêng từng năm (nếu yêu cầu) ────────
                yearly_files: list[Path] = []
                if split:
                    for year in range(start_year, end_year + 1):
                        cal = gen.generate_year(year)
                        fname = OUTPUT_PATH / f'viet_lunar_{year}.ics'
                        gen.save(cal, fname)
                        yearly_files.append(fname)
                        total_files.append(fname)
                        response_files.append({
                            "name": fname.name,
                            "size": format_size(fname),
                            "events": count_events(fname),
                            "url": f"/output/{fname.name}"
                        })

                    # Nén zip nếu có nhiều hơn 1 năm lẻ
                    if len(yearly_files) > 1:
                        zip_name = OUTPUT_PATH / f'viet_lunar_yearly_{start_year}_{end_year}.zip'
                        create_zip_archive(yearly_files, zip_name)
                        total_files.append(zip_name)
                        response_files.insert(0, {
                            "name": zip_name.name,
                            "size": format_size(zip_name),
                            "events": -1,
                            "url": f"/output/{zip_name.name}"
                        })

                # ── 2. Tạo file tổng hợp cả khoảng ──────────────────
                suffix = f'{start_year}_{end_year}'
                if start_year == end_year:
                    suffix = str(start_year)

                cal = gen.generate_range(start_year, end_year)
                fname = OUTPUT_PATH / f'viet_lunar_{suffix}.ics'
                gen.save(cal, fname)
                total_files.append(fname)
                
                # Lưu file latest để cập nhật
                latest_fname = OUTPUT_PATH / 'viet_lunar_latest.ics'
                shutil.copy(fname, latest_fname)

                response_files.append({
                    "name": fname.name,
                    "size": format_size(fname),
                    "events": count_events(fname),
                    "url": f"/output/{fname.name}"
                })

                # Trả phản hồi thành công cùng danh sách file tải về
                self.send_json_response(200, {
                    "success": True,
                    "files": response_files
                })

            except Exception as e:
                self.send_json_response(200, {
                    "success": False,
                    "error": str(e)
                })
        else:
            self.send_error_response(404, "Đường dẫn API không hợp lệ.")

    # ──────────────────────────────────────────────────────────
    # Response Utilities
    # ──────────────────────────────────────────────────────────

    def send_json_response(self, status: int, data: dict):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def send_error_response(self, status: int, message: str):
        self.send_response(status)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))


# ──────────────────────────────────────────────────────────────
# Khởi chạy Server
# ──────────────────────────────────────────────────────────────

def run_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, LunarCalendarAPIHandler)
    print(f"🌸 Pinkie Web Server đang chạy tại: http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🌸 Đang đóng máy chủ...")
        httpd.server_close()


if __name__ == '__main__':
    run_server()
