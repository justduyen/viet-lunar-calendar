# 🌙 Lịch Âm Việt Nam — Công cụ tạo file iCalendar

Dự án này giúp bạn tạo các file `.ics` chứa thông tin lịch âm Việt Nam (bao gồm ngày lễ truyền thống, Can Chi, Tiết Khí) từ năm **2026 đến 2060**. Các file này có thể dễ dàng nhập (import) vào Google Calendar, Apple Calendar, hoặc Outlook.

---

## ✨ Tính năng nổi bật

| Tính năng | Chi tiết |
|---|---|
| **Độ chính xác cao** | Sử dụng thư viện `lunar-python` dựa trên thuật toán thiên văn học chuẩn xác. |
| **Múi giờ chuẩn** | Được thiết kế riêng cho múi giờ Việt Nam (GMT+7 - `Asia/Ho_Chi_Minh`). |
| **Giao diện sạch sẽ** | Can Chi và Tiết Khí được đưa vào phần Mô tả (Description), giúp tiêu đề lịch gọn gàng. |
| **Sự kiện hàng tháng** | Tự động nhắc Mùng 1 🌑, Rằm 🌕, Cúng Thần Tài/Cô Hồn (mùng 2 & 16), và nhắc chuẩn bị lễ vật. |
| **Ngày lễ truyền thống** | Đầy đủ các dịp Tết Nguyên Đán, Giỗ Tổ Hùng Vương, Vu Lan, Trung Thu, v.v. |
| **Tự động hóa** | Tích hợp GitHub Actions để tự động cập nhật lịch định kỳ. |

---

## 🚀 Cài đặt (Installation)

Yêu cầu máy tính đã cài đặt **Python 3.8+**.

```bash
# 1. Tạo môi trường ảo (khuyến nghị)
python -m venv .venv
.venv\Scripts\activate        # Trên Windows
source .venv/bin/activate     # Trên Linux/macOS

# 2. Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

---

## ▶️ Sử dụng (Usage)

Chạy lệnh sau để bắt đầu tạo file lịch:

```bash
# Tạo file tổng hợp 2026–2060 (mặc định)
python main.py

# Tạo file tổng hợp kèm theo file zip chứa các năm riêng lẻ
python main.py --split

# Chỉ tạo lịch cho một năm cụ thể
python main.py --year 2026

# Tạo lịch cho một khoảng thời gian tùy chọn
python main.py --start 2026 --end 2035
```

Các file kết quả sẽ được lưu trong thư mục `output/`.

---

## 📅 Danh sách ngày lễ và sự kiện

### Sự kiện định kỳ hàng tháng
| Thời điểm | Sự kiện |
|---|---|
| **Mùng 1** | 🌑 Mùng 1 Tháng [X] — Ngày Sóc (đi lễ chùa, thắp hương gia tiên). |
| **Mùng 2 & 16** | 🕯️ Cúng Cô Hồn & Thần Tài (Dành cho người kinh doanh). |
| **Ngày 14 & Cuối tháng** | ⚠️ Nhắc chuẩn bị đồ lễ cho ngày Rằm hoặc Mùng 1 vào ngày mai. |
| **Ngày 15 (Rằm)** | 🌕 Rằm Tháng [X] — Ngày Vọng (đi lễ chùa, ăn chay). |

### Các ngày lễ lớn trong năm
- **Tết Nguyên Đán (🧧):** Mùng 1 đến mùng 3 tháng Giêng.
- **Vía Thần Tài (💰):** Mùng 10 tháng Giêng.
- **Rằm Tháng Giêng:** Tết Nguyên Tiêu.
- **Giỗ Tổ Hùng Vương:** 10 tháng 3 âm lịch.
- **Lễ Phật Đản:** 15 tháng 4 âm lịch.
- **Tết Đoan Ngọ:** mùng 5 tháng 5 âm lịch.
- **Lễ Vu Lan:** Rằm tháng Bảy (Xá tội vong nhân).
- **Tết Trung Thu:** Rằm tháng Tám.
- **Cúng Ông Công Ông Táo:** 23 tháng Chạp.
- **Đêm Giao Thừa:** Ngày cuối cùng của năm âm lịch.

---

## 📥 Hướng dẫn nhập (Import) vào ứng dụng Lịch

**Google Calendar:**
1. Truy cập [calendar.google.com](https://calendar.google.com).
2. Nhấn biểu tượng bánh răng (⚙️) > **Cài đặt** > **Nhập & Xuất** > **Nhập**.
3. Chọn file `.ics` bạn đã tạo và nhấn **Nhập**.

**Apple Calendar:**
1. Mở ứng dụng Lịch trên máy tính.
2. Chọn menu **Tệp (File)** > **Nhập (Import)...**
3. Chọn file `.ics` và nhấn **Nhập**.

---

## ❓ Câu hỏi thường gặp (Troubleshooting)

**1. Tại sao tôi không thấy lịch trên điện thoại?**
- Hãy đảm bảo bạn đã bật tính năng **Đồng bộ hóa (Sync)** cho lịch vừa nhập trong cài đặt của ứng dụng Google Calendar trên điện thoại.

**2. Lịch có tự động cập nhật không?**
- Nếu bạn nhập bằng file `.ics` thủ công, bạn sẽ cần xóa lịch cũ và nhập lại bản mới khi có thay đổi. Nếu bạn sử dụng tính năng GitHub Actions để tạo URL lịch công khai, lịch có thể tự cập nhật nếu được thêm qua URL.

**3. Tại sao file .ics lại có dung lượng lớn?**
- File tổng hợp nhiều năm chứa hàng ngàn sự kiện. Nếu ứng dụng của bạn phản hồi chậm, hãy cân nhắc chỉ nhập file của từng năm riêng lẻ (có sẵn trong file nén `.zip`).

---

## 📜 Giấy phép (License)

Dự án này được phát hành dưới giấy phép **MIT**. Xem file `LICENSE` để biết thêm chi tiết.
