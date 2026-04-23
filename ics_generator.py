# ============================================================
# ics_generator.py — Tạo file iCalendar (.ics) cho lịch âm VN
# ============================================================
from __future__ import annotations

import uuid
from datetime import date, timedelta
from pathlib import Path
from typing import Optional

from icalendar import Calendar, Event, vText, vCalAddress

from config import (
    CALENDAR_NAME, CALENDAR_DESCRIPTION,
    PRODID, CALENDAR_VERSION, TIMEZONE,
)
from holidays import (
    FIXED_SOLAR_HOLIDAYS, FIXED_LUNAR_HOLIDAYS, MONTHLY_EVENTS,
    GIAO_THUA, REMIND_MUNG1, HolidayInfo,
)
from lunar_converter import to_lunar, is_last_day_of_lunar_month, LunarDate


# ──────────────────────────────────────────────────────────────
# Màu sắc theo category (X-APPLE-CALENDAR-COLOR hint)
# ──────────────────────────────────────────────────────────────
CATEGORY_COLOR: dict[str, str] = {
    'NATIONAL':    '#E53935',   # Đỏ — lễ quốc gia
    'TRADITIONAL': '#FB8C00',   # Cam — lễ truyền thống
    'MONTHLY':     '#1E88E5',   # Xanh dương — định kỳ hàng tháng
    'REMINDER':    '#FDD835',   # Vàng — nhắc nhở
    'DAILY':       '#A3BE8C',   # Sage Green — thông tin ngày âm lịch
}


# ──────────────────────────────────────────────────────────────
# Xây dựng danh sách sự kiện cho một ngày
# ──────────────────────────────────────────────────────────────

def _collect_events_for_day(
    d: date,
    lunar: LunarDate,
) -> list[tuple[HolidayInfo, bool]]:
    """
    Trả về danh sách (HolidayInfo, is_primary) cho ngày d.
    is_primary = True nghĩa là sự kiện quan trọng nhất (hiển thị trong Summary).
    """
    results: list[tuple[HolidayInfo, bool]] = []
    m = lunar.lunar_month_abs
    day = lunar.lunar_day

    # ── 1. Thông tin ngày âm lịch HÀNG NGÀY ──────────────────
    daily_info = HolidayInfo(
        name=f'{day}/{m}',
        description=f'Ngày {day} tháng {m} âm lịch.',
        category='DAILY'
    )
    results.append((daily_info, True))

    # ── 2. Ngày lễ DƯƠNG LỊCH ───────────────────────────────
    solar_h = FIXED_SOLAR_HOLIDAYS.get((d.month, d.day))
    if solar_h:
        results.append((solar_h, False))

    # ── 3. Ngày lễ ÂM LỊCH ──────────────────────────────────
    fixed = FIXED_LUNAR_HOLIDAYS.get((m, day))
    if fixed:
        results.append((fixed, False))

    # ── 3. Đêm Giao Thừa ────────────────────────────────────
    if m == 12 and is_last_day_of_lunar_month(d):
        if (12, day) not in FIXED_LUNAR_HOLIDAYS:
            results.append((GIAO_THUA, False))

    # ── 4. Sự kiện hàng tháng ───────────────────────────────
    monthly = MONTHLY_EVENTS.get(day)
    if monthly:
        results.append((monthly, False))

    # ── 5. Nhắc chuẩn bị Mùng 1 ─────────────────────────────
    tomorrow = d + timedelta(days=1)
    if is_last_day_of_lunar_month(tomorrow) and m != 12:
        results.append((REMIND_MUNG1, False))

    return results


# ──────────────────────────────────────────────────────────────
# Xây dựng iCal Event từ danh sách sự kiện
# ──────────────────────────────────────────────────────────────

def _build_ical_event(
    d: date,
    lunar: LunarDate,
    events: list[tuple[HolidayInfo, bool]],
) -> Optional[Event]:
    """Tạo một VEVENT all-day từ danh sách sự kiện trong ngày."""
    if not events:
        return None

    # Sắp xếp: daily info làm gốc, các sự kiện khác đi kèm
    daily_event = [e for e, p in events if e.category == 'DAILY'][0]
    other_events = [e for e, _ in events if e.category != 'DAILY']

    # Tiêu đề thông minh: "Ngày/Tháng • Tên Sự Kiện"
    summary = daily_event.name # e.g. "15/7"
    
    if other_events:
        # Lấy tên các sự kiện khác, xử lý placeholder {m}
        event_names = []
        for e in other_events:
            n = e.name.replace('{m}', lunar.month_name_vn)
            # Loại bỏ các emoji lặp lại hoặc chuỗi quá dài nếu cần
            event_names.append(n)
        
        summary = f"{summary} • {' | '.join(event_names)}"

    # ── Xây dựng description ────────────────────────────────
    desc_parts: list[str] = []

    # Danh sách tất cả sự kiện trong ngày
    for i, (hi, _) in enumerate(events):
        h_name = hi.name.replace('{m}', lunar.month_name_vn)
        h_desc = hi.description.replace('{m}', lunar.month_name_vn)
        
        # Prefixes phong cách Nature
        prefix = "🌸" if hi.category in ('NATIONAL', 'TRADITIONAL') else "🍃"
        if hi.category == 'DAILY': prefix = "🌱"
        
        desc_parts.append(f'{prefix} {h_name}\n{h_desc}')
        if i < len(events) - 1:
            desc_parts.append('──')

    description = '\n'.join(desc_parts)

    # ── Tạo VEVENT (Sử dụng ID cố định để tránh trùng lặp khi import lại) ────
    event = Event()
    # UID cố định theo ngày: vnlunar-20260217@justduyen
    event.add('uid',         f"vnlunar-{d.strftime('%Y%m%d')}@justduyen")
    event.add('summary',     summary)
    event.add('description', description)
    event.add('dtstart',     d)
    event.add('dtend',       d + timedelta(days=1))

    # Categories (dùng để lọc trong calendar app)
    cats = list({hi.category for hi, _ in events})
    event.add('categories', cats)

    # Màu sắc: Ưu tiên màu của lễ quan trọng nhất
    priority = ['NATIONAL', 'TRADITIONAL', 'MONTHLY', 'REMINDER', 'DAILY']
    active_cats = {hi.category for hi, _ in events}
    
    selected_cat = 'DAILY'
    for cat in priority:
        if cat in active_cats:
            selected_cat = cat
            break
            
    color_hex = CATEGORY_COLOR.get(selected_cat, '#1E88E5')
    event.add('color', color_hex)  # RFC 7986 (Hint cho Apple Calendar)

    # Đánh dấu ngày nghỉ chính thức
    if any(hi.is_public_holiday for hi, _ in events):
        event.add('x-microsoft-cdo-importance', '2')

    # Timezone stamp
    import pytz
    tz = pytz.timezone(TIMEZONE)
    from datetime import datetime
    event.add('dtstamp', datetime.now(tz))

    return event


# ──────────────────────────────────────────────────────────────
# Class tạo Calendar
# ──────────────────────────────────────────────────────────────

class LunarCalendarGenerator:
    """Tạo file .ics lịch âm Việt Nam theo khoảng năm cho trước."""

    def _make_calendar(self, name: str = CALENDAR_NAME) -> Calendar:
        """Khởi tạo Calendar object với metadata chuẩn."""
        cal = Calendar()
        cal.add('prodid',  PRODID)
        cal.add('version', CALENDAR_VERSION)
        cal.add('calscale', 'GREGORIAN')
        cal.add('method',   'PUBLISH')
        cal.add('x-wr-calname',   name)
        cal.add('x-wr-timezone',  TIMEZONE)
        cal.add('x-wr-caldesc',   CALENDAR_DESCRIPTION)
        cal.add('x-apple-calendar-color', '#E53935')
        return cal

    def generate_year(self, year: int) -> Calendar:
        """Tạo đối tượng Calendar cho một năm Dương lịch cụ thể."""
        cal = self._make_calendar(f'Lịch Âm Việt Nam {year}')
        start = date(year, 1, 1)
        end   = date(year, 12, 31)
        self._fill_calendar(cal, start, end)
        return cal

    def generate_range(self, start_year: int, end_year: int) -> Calendar:
        """Tạo đối tượng Calendar tổng hợp cho một khoảng thời gian nhiều năm."""
        cal = self._make_calendar(f'Lịch Âm Việt Nam {start_year}–{end_year}')
        start = date(start_year, 1, 1)
        end   = date(end_year, 12, 31)
        self._fill_calendar(cal, start, end)
        return cal

    def _fill_calendar(self, cal: Calendar, start: date, end: date) -> None:
        """Duyệt qua từng ngày trong khoảng thời gian, phát hiện và thêm sự kiện vào Calendar."""
        current = start
        while current <= end:
            try:
                lunar   = to_lunar(current)
                day_events = _collect_events_for_day(current, lunar)
                if day_events:
                    event = _build_ical_event(current, lunar, day_events)
                    if event:
                        cal.add_component(event)
            except Exception as exc:
                # Ghi nhận cảnh báo nhưng không làm gián đoạn toàn bộ quá trình
                print(f'[WARN] Lỗi khi xử lý ngày {current}: {exc}')
            current += timedelta(days=1)

    @staticmethod
    def save(cal: Calendar, filepath: str | Path) -> None:
        """Lưu đối tượng Calendar ra file định dạng .ics."""
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'wb') as f:
            f.write(cal.to_ical())
