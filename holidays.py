# ============================================================
# holidays.py — Dữ liệu ngày lễ & sự kiện âm lịch Việt Nam
# ============================================================
from dataclasses import dataclass


@dataclass
class HolidayInfo:
    name: str             # Tên ngày lễ (có emoji)
    description: str      # Mô tả / ý nghĩa
    category: str         # 'NATIONAL' | 'TRADITIONAL' | 'MONTHLY' | 'REMINDER'
    is_public_holiday: bool = False  # Ngày nghỉ lễ chính thức


# ──────────────────────────────────────────────────────────────
# 1. NGÀY LỄ CỐ ĐỊNH THEO ÂM LỊCH
#    Key: (tháng_âm, ngày_âm)
# ──────────────────────────────────────────────────────────────
FIXED_LUNAR_HOLIDAYS: dict[tuple, HolidayInfo] = {

    # ── Tết Nguyên Đán ──────────────────────────────────────
    (1, 1): HolidayInfo(
        name='🧧 Mùng 1 Tết Nguyên Đán',
        description='Ngày đầu tiên của năm mới âm lịch. Đây là ngày lễ lớn nhất trong năm '
                    'của người Việt. Gia đình sum họp, chúc tết, lì xì, đi lễ chùa.',
        category='NATIONAL',
        is_public_holiday=True,
    ),
    (1, 2): HolidayInfo(
        name='🧧 Mùng 2 Tết Nguyên Đán',
        description='Ngày thứ hai của Tết Nguyên Đán. Thông thường là ngày về nhà bên ngoại '
                    'hoặc đi chúc tết họ hàng, bạn bè.',
        category='NATIONAL',
        is_public_holiday=True,
    ),
    (1, 3): HolidayInfo(
        name='🧧 Mùng 3 Tết Nguyên Đán',
        description='Ngày thứ ba của Tết Nguyên Đán. Ngày cuối cùng trong 3 ngày Tết chính. '
                    'Nhiều gia đình làm lễ hóa vàng tiễn tổ tiên.',
        category='NATIONAL',
        is_public_holiday=True,
    ),

    # ── Tháng Giêng ─────────────────────────────────────────
    (1, 10): HolidayInfo(
        name='💰 Vía Thần Tài (10 Tháng Giêng)',
        description='Ngày vía Thần Tài — ngày mùng 10 tháng Giêng âm lịch. Người kinh doanh '
                    'mua vàng, cúng Thần Tài để cầu tài lộc, may mắn trong năm mới.',
        category='TRADITIONAL',
    ),
    (1, 15): HolidayInfo(
        name='🌕 Rằm Tháng Giêng — Tết Nguyên Tiêu',
        description='Rằm tháng Giêng (15/1 âm lịch) hay còn gọi là Tết Nguyên Tiêu. '
                    'Đây là rằm đầu tiên và quan trọng nhất trong năm. Nhiều người đi lễ chùa '
                    'cầu an, cầu phúc cho cả năm.',
        category='TRADITIONAL',
    ),

    # ── Tháng Ba ────────────────────────────────────────────
    (3, 10): HolidayInfo(
        name='🏺 Giỗ Tổ Hùng Vương (10/3 Âm Lịch)',
        description='Ngày Giỗ Tổ Hùng Vương (10 tháng 3 âm lịch) — Quốc lễ tưởng nhớ '
                    'các vua Hùng đã có công dựng nước. Ngày nghỉ lễ chính thức.',
        category='NATIONAL',
        is_public_holiday=True,
    ),

    # ── Tháng Tư ────────────────────────────────────────────
    (4, 15): HolidayInfo(
        name='🙏 Lễ Phật Đản (15/4 Âm Lịch)',
        description='Lễ Phật Đản — kỷ niệm ngày Đức Phật Thích Ca Mâu Ni đản sinh (15 tháng 4 âm). '
                    'Phật tử đến chùa lễ Phật, thả đèn hoa đăng, phóng sinh.',
        category='TRADITIONAL',
    ),

    # ── Tháng Năm ───────────────────────────────────────────
    (5, 5): HolidayInfo(
        name='☀️ Tết Đoan Ngọ (5/5 Âm Lịch)',
        description='Tết Đoan Ngọ (mùng 5 tháng 5 âm lịch) hay Tết diệt sâu bọ. '
                    'Người Việt ăn rượu nếp, hoa quả để tiêu diệt "sâu bọ" trong người. '
                    'Thời điểm giữa năm âm lịch.',
        category='TRADITIONAL',
    ),

    # ── Tháng Bảy ───────────────────────────────────────────
    (7, 15): HolidayInfo(
        name='🕯️ Lễ Vu Lan — Rằm Tháng Bảy (Xá Tội Vong Nhân)',
        description='Lễ Vu Lan (Rằm tháng 7 âm lịch) — ngày báo hiếu cha mẹ, tổ tiên. '
                    'Đây cũng là ngày Xá Tội Vong Nhân, cúng thí thực cô hồn. '
                    'Phật tử cài hoa hồng, đi lễ chùa cầu siêu cho vong linh.',
        category='TRADITIONAL',
    ),

    # ── Tháng Tám ───────────────────────────────────────────
    (8, 15): HolidayInfo(
        name='🏮 Tết Trung Thu (15/8 Âm Lịch)',
        description='Tết Trung Thu (Rằm tháng 8 âm lịch) — Tết của thiếu nhi. '
                    'Trẻ em rước đèn, phá cỗ, ăn bánh Trung Thu. Người lớn ngắm trăng, '
                    'sum họp gia đình dưới ánh trăng tròn.',
        category='TRADITIONAL',
    ),

    # ── Tháng Mười Hai ──────────────────────────────────────
    (12, 23): HolidayInfo(
        name='🍳 Cúng Ông Công Ông Táo (23 Tháng Chạp)',
        description='Ngày 23 tháng Chạp âm lịch — Lễ tiễn Ông Công, Ông Táo về trời. '
                    'Các gia đình Việt làm lễ cúng cá chép (phóng sinh), tiễn Táo Quân '
                    'lên thiên đình báo cáo với Ngọc Hoàng về việc trong năm.',
        category='TRADITIONAL',
    ),
    # Ngày 30 tháng Chạp (hoặc 29 nếu tháng thiếu) — xử lý riêng trong code
    # bằng cách kiểm tra ngày cuối cùng của tháng 12 âm lịch
}


# ──────────────────────────────────────────────────────────────
# 2. SỰ KIỆN ĐỊNH KỲ HÀNG THÁNG
#    Key: ngày_âm (int) — áp dụng cho tất cả các tháng
# ──────────────────────────────────────────────────────────────
MONTHLY_EVENTS: dict[int, HolidayInfo] = {

    1: HolidayInfo(
        name='🌑 Mùng 1 {m} — Ngày Sóc (Trăng Non)',
        description='Ngày đầu tiên của tháng âm lịch — Ngày Sóc (New Moon). '
                    'Ngày tốt để đi lễ chùa, cúng thần linh, thắp hương gia tiên. '
                    'Nhiều người ăn chay trong ngày này.',
        category='MONTHLY',
    ),
    2: HolidayInfo(
        name='🕯️ Mùng 2 {m} — Cúng Cô Hồn & Thần Tài',
        description='Ngày Mùng 2 hàng tháng: Ngày cúng Cô Hồn và Thần Tài cho người kinh doanh. '
                    'Chuẩn bị lễ vật: hoa quả, muối gạo, tiền vàng mã, nhang đèn.',
        category='MONTHLY',
    ),
    14: HolidayInfo(
        name='⚠️ Ngày 14 {m} — Chuẩn Bị Đồ Cúng Rằm',
        description='Ngày 14 âm lịch: Ngày mai là Rằm (15 âm). Hãy chuẩn bị lễ vật '
                    'cúng Rằm: hoa tươi, quả, xôi chè, nhang đèn, vàng mã.',
        category='REMINDER',
    ),
    15: HolidayInfo(
        name='🌕 Rằm {m} — Ngày Vọng (Trăng Tròn)',
        description='Ngày Rằm (15 âm lịch) — Ngày Vọng, trăng tròn. '
                    'Ngày tốt để đi lễ chùa, cúng gia tiên, thắp hương Phật. '
                    'Nhiều người ăn chay trong ngày này.',
        category='MONTHLY',
    ),
    16: HolidayInfo(
        name='🕯️ Ngày 16 {m} — Cúng Cô Hồn & Thần Tài',
        description='Ngày 16 hàng tháng: Ngày cúng Cô Hồn và Thần Tài cho người kinh doanh. '
                    'Chuẩn bị lễ vật: hoa quả, muối gạo, tiền vàng mã, nhang đèn.',
        category='MONTHLY',
    ),
}

# Ngày Giao Thừa: ngày cuối cùng của tháng 12 âm lịch (29 hoặc 30)
GIAO_THUA = HolidayInfo(
    name='🎆 Đêm Giao Thừa — Cuối Năm Âm Lịch',
    description='Đêm Giao Thừa — ngày cuối cùng của năm âm lịch. '
                'Các gia đình làm lễ cúng Giao Thừa ngoài trời (cúng trời đất) '
                'và trong nhà (cúng gia tiên) để đón năm mới. '
                'Lúc 00:00 là thời khắc chuyển giao năm cũ sang năm mới.',
    category='NATIONAL',
    is_public_holiday=True,
)

# Nhắc chuẩn bị Mùng 1: ngày cuối tháng âm (29 hoặc 30)
REMIND_MUNG1 = HolidayInfo(
    name='⚠️ Ngày Cuối Tháng — Chuẩn Bị Đồ Cúng Mùng 1',
    description='Ngày cuối cùng của tháng âm lịch: Ngày mai là Mùng 1. '
                'Hãy chuẩn bị lễ vật cúng Mùng 1: hoa tươi, quả, nhang đèn, vàng mã.',
    category='REMINDER',
)
