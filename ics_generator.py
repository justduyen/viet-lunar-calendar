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

    # ── 1. Ngày lễ cố định (ưu tiên cao nhất) ───────────────
    fixed = FIXED_LUNAR_HOLIDAYS.get((m, day))
    if fixed:
        results.append((fixed, True))

    # ── 2. Đêm Giao Thừa: ngày cuối tháng 12 âm ────────────
    if m == 12 and is_last_day_of_lunar_month(d):
        # Không trùng với ngày 30/12 đã cố định (nếu tháng đủ)
        if (12, day) not in FIXED_LUNAR_HOLIDAYS:
            results.append((GIAO_THUA, not bool(fixed)))

    # ── 3. Sự kiện hàng tháng ───────────────────────────────
    monthly = MONTHLY_EVENTS.get(day)
    if monthly:
        # Nếu ngày này đã có lễ cố định quan trọng hơn → phụ trợ
        is_primary_monthly = not bool(fixed)
        results.append((monthly, is_primary_monthly))

    # ── 4. Nhắc chuẩn bị Mùng 1: ngày TRƯỚC ngày cuối tháng ──
    #    Nếu tháng đủ (30 ngày), nhắc vào ngày 29.
    #    Nếu tháng thiếu (29 ngày), nhắc vào ngày 28.
    tomorrow = d + timedelta(days=1)
    if is_last_day_of_lunar_month(tomorrow) and m != 12:
        # Tránh trùng lặp với các sự kiện định kỳ khác nếu có
        is_primary_remind = not bool(fixed) and not bool(monthly)
        results.append((REMIND_MUNG1, is_primary_remind))

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

    # Tiêu đề chính
    primary = primary_events[0] if primary_events else secondary_events[0]
    summary = primary.name
    
    # Điền tên tháng vào tiêu đề nếu có placeholder {m} (Dành cho sự kiện định kỳ hàng tháng)
    if '{m}' in summary:
        summary = summary.replace('{m}', lunar.month_name_vn)

    # ── Xây dựng description ────────────────────────────────
    desc_parts: list[str] = []

    # Mô tả sự kiện chính
    p_desc = primary.description
    if '{m}' in p_desc:
        p_desc = p_desc.replace('{m}', lunar.month_name_vn)
    desc_parts.append(p_desc)

    # Các sự kiện phụ (nếu có)
    for hi in secondary_events:
        h_name = hi.name
        if '{m}' in h_name:
            h_name = h_name.replace('{m}', lunar.month_name_vn)
        h_desc = hi.description
        if '{m}' in h_desc:
            h_desc = h_desc.replace('{m}', lunar.month_name_vn)
        desc_parts.append(f'\n——\n{h_name}\n{h_desc}')

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
