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
    FIXED_LUNAR_HOLIDAYS, MONTHLY_EVENTS,
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
    'DAILY':       '#43A047',   # Xanh lá — thông tin ngày âm lịch (như ảnh)
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

    # ── 1. Thông tin ngày âm lịch HÀNG NGÀY (Mục tiêu chính) ──
    # Định dạng: "Ngày/Tháng" (Ví dụ: 15/7)
    daily_info = HolidayInfo(
        name=f'{day}/{m}',
        description=f'Ngày {day} tháng {m} âm lịch.',
        category='DAILY'
    )
    # Luôn thêm thông tin ngày âm lịch
    results.append((daily_info, True))

    # ── 2. Ngày lễ cố định ──────────────────────────────────
    fixed = FIXED_LUNAR_HOLIDAYS.get((m, day))
    if fixed:
        results.append((fixed, False)) # Để info ngày làm primary summary

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

    # Sắp xếp: primary trước
    primary_events   = [e for e, p in events if p]
    secondary_events = [e for e, p in events if not p]

    # Tiêu đề chính (Ngày/Tháng âm lịch)
    primary = primary_events[0]
    summary = primary.name
    
    # Nếu có ngày lễ quan trọng, hãy đưa tên lễ vào Summary luôn cho dễ nhìn
    # Ví dụ: "1/1 🧧 Tết Nguyên Đán"
    important_holidays = [e for e in secondary_events if e.category in ('NATIONAL', 'TRADITIONAL')]
    if important_holidays:
        summary = f"{summary} • {important_holidays[0].name}"

    # ── Xây dựng description ────────────────────────────────
    desc_parts: list[str] = []

    # Danh sách tất cả sự kiện trong ngày
    for i, (hi, _) in enumerate(events):
        h_name = hi.name
        if '{m}' in h_name:
            h_name = h_name.replace('{m}', lunar.month_name_vn)
        h_desc = hi.description
        if '{m}' in h_desc:
            h_desc = h_desc.replace('{m}', lunar.month_name_vn)
        
        prefix = "📌" if i == 0 else "🔹"
        desc_parts.append(f'{prefix} {h_name}\n{h_desc}')
        if i < len(events) - 1:
            desc_parts.append('──')

    # Thêm footer thông tin âm lịch
    desc_parts.append('\n' + lunar.build_description_footer())

    description = '\n'.join(desc_parts)

    # ── Tạo VEVENT ──────────────────────────────────────────
    event = Event()
    event.add('uid',         str(uuid.uuid4()) + f'@vietlunar{d.year}')
    event.add('summary',     summary)
    event.add('description', description)
    event.add('dtstart',     d)                     # All-day event
    event.add('dtend',       d + timedelta(days=1)) # Kết thúc ngày hôm sau

    # Categories (dùng để lọc trong calendar app)
    cats = list({hi.category for hi, _ in events})
    event.add('categories', cats)

    # Màu (Apple Calendar hỗ trợ, Google Calendar bỏ qua)
    color_cat = primary.category
    color_hex = CATEGORY_COLOR.get(color_cat, '#1E88E5')
    event.add('color', color_hex)  # RFC 7986

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
