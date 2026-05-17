# 🌸 Pinkie Lunar Calendar — Lịch Âm Việt Nam 🌸

**Tiếng Việt** | [English](README_EN.md)

![Update Lunar Calendar ICS](https://github.com/justduyen/viet-lunar-calendar/actions/workflows/main.yml/badge.svg)

> [!quote] **Brand Motto**
> *For all the cute girls who aren't super tech-savvy and the sweetest, gentlest boys out there~ (´｡• ᵕ •｡`) ♡*
> — **JustDuyen**

Chào mừng bạn đến với **Pinkie Lunar Calendar**! Đây là một ứng dụng Web GUI & CLI siêu dễ thương, được thiết kế tỉ mỉ theo tông màu hồng pastel ngọt ngào của hệ sinh thái **Pinkie Suite** nhằm giúp bạn tạo ra các tệp `.ics` Lịch Âm Việt Nam (bao gồm ngày lễ truyền thống, Can Chi, Tiết Khí) từ năm **2026 đến 2060** cực kỳ trực quan và nhanh chóng!

Các tệp lịch tạo ra có thể dễ dàng nhập (import) vào Google Calendar, Apple Calendar (iPhone/Macbook) hoặc Microsoft Outlook chỉ trong 1-Click!

---

## ✨ Các Tính Năng Nổi Bật Mang Đậm Phong Cách Pinkie

| Tính năng | Biểu tượng | Mô tả chi tiết |
| :--- | :---: | :--- |
| **🌸 Pinkie Web Dashboard** | `🧸` | Giao diện Web kính mờ (glassmorphic) cực kỳ lung linh, hỗ trợ thanh trượt chọn năm, bo góc mềm mại và nút chuyển chế độ **Sáng/Tối** siêu xinh. |
| **💖 Độ chính xác tuyệt đối** | `✨` | Lập trình dựa trên thuật toán thiên văn Jean Meeus của thư viện `lunar-python` chuẩn xác. |
| **🎀 Thiết kế tối giản, sạch sẽ** | `🍃` | Toàn bộ thông tin Can Chi, Tiết Khí được đưa vào phần mô tả sự kiện (Description) giúp tiêu đề lịch luôn gọn gàng, trang nhã. |
| **🐾 Hiển thị âm lịch hàng ngày** | `🌱` | Hiển thị ngày âm lịch dạng `15/7` hàng ngày với màu hồng pastel dịu mắt trên ứng dụng lịch của bạn. |
| **⚙️ Tự động hóa hoàn toàn** | `🔮` | Tích hợp **GitHub Actions** để tự động cập nhật lịch định kỳ mỗi tháng mà bạn không cần cấu hình lại. |

---

## 🚀 Hướng Dẫn Cài Đặt (Installation)

Ứng dụng yêu cầu máy tính của bạn đã cài đặt **Python 3.8+**.

```bash
# 1. Di chuyển vào thư mục dự án
cd "D:\Obsidian\1 dự án\Mini Apps\viet-lunar-calendar"

# 2. Kích hoạt môi trường ảo (Khuyên dùng)
.venv\Scripts\activate        # Trên Windows
source .venv/bin/activate     # Trên Linux/macOS

# 3. Cài đặt các thư viện phụ trợ
pip install -r requirements.txt
```

---

## ▶️ Cách Khởi Chạy (Usage)

Mặc định, **Pinkie Lunar Calendar** sẽ khởi chạy giao diện Web GUI cục bộ cực kỳ đáng yêu và **tự động mở trình duyệt** của bạn:

```bash
# 🌸 Khởi chạy giao diện Web GUI Pinkie (Mặc định)
python main.py
```
*Trình duyệt của bạn sẽ tự động mở trang điều khiển tại địa chỉ: `http://localhost:8000`*

---

### ⚙️ Chế độ dòng lệnh tương thích ngược (CLI Mode):
Nếu bạn muốn sử dụng giao diện dòng lệnh cũ để tự động hóa hoặc tích hợp script, hãy sử dụng thêm cờ `--cli`:

```bash
# Tạo file tổng hợp ở chế độ dòng lệnh CLI
python main.py --cli

# Tạo file tổng hợp kèm theo tệp nén ZIP chứa các năm riêng lẻ
python main.py --cli --split

# Chỉ tạo lịch cho một năm cụ thể
python main.py --cli --year 2026

# Tạo lịch cho một khoảng thời gian tùy chọn
python main.py --cli --start 2026 --end 2035
```
*Các tệp kết quả sau khi tạo xong sẽ được tự động lưu vào thư mục `output/`.*

---

## 🔗 Đường Dẫn Đăng Ký Vĩnh Viễn (Khuyên Dùng)

Để lịch tự động cập nhật trên thiết bị của bạn mà không cần phải tải lại mỗi năm, hãy sử dụng tính năng đăng ký theo URL (Raw link) dưới đây:

📌 **Đường dẫn đăng ký:** `https://raw.githubusercontent.com/justduyen/viet-lunar-calendar/main/output/viet_lunar_latest.ics`

---

## 📅 Các Ngày Lễ & Nhắc Nhở Truyền Thống Được Tích Hợp

- **🧧 Tết Nguyên Đán:** Mùng 1 đến mùng 3 tháng Giêng âm lịch.
- **💰 Vía Thần Tài:** Mùng 10 tháng Giêng âm lịch.
- **🏮 Tết Nguyên Tiêu (Rằm tháng Giêng):** Đi chùa cầu bình an.
- **🌾 Giỗ Tổ Hùng Vương:** 10 tháng 3 âm lịch.
- **🪷 Lễ Phật Đản:** 15 tháng 4 âm lịch.
- **🛶 Tết Đoan Ngọ (Giết sâu bọ):** Mùng 5 tháng 5 âm lịch.
- **🕯️ Rằm Tháng Bảy (Lễ Vu Lan):** Xá tội vong nhân.
- **🥮 Tết Trung Thu:** Rằm tháng Tám âm lịch.
- **🍳 Cúng Ông Công Ông Táo:** 23 tháng Chạp âm lịch.
- **🌌 Đêm Giao Thừa:** Khoảnh khắc chuyển giao năm mới âm lịch.
- **🌑 Sự kiện Mùng 1 & 🌕 Ngày Rằm hàng tháng:** Đi chùa cầu phúc, nhắc nhở ăn chay định kỳ.

---

## 📥 Hướng Dẫn Nhập (Import) Vào Ứng Dụng Lịch

> [!tip]
> Bạn có thể đọc hướng dẫn trực quan ngay tại giao diện **Pinkie Web Dashboard** sau khi khởi chạy!

* **Google Calendar:** Truy cập [calendar.google.com](https://calendar.google.com) &rarr; Click biểu tượng bánh răng **⚙️ Cài đặt** &rarr; Chọn **Nhập & Xuất** &rarr; Chọn tệp `.ics` vừa tải về và nhấn nút **Nhập**.
* **Apple Calendar (iPhone/Macbook):**
  - *Trên máy Mac:* Mở ứng dụng Lịch &rarr; Chọn menu **Tệp (File)** &rarr; Chọn **Nhập (Import)...** &rarr; Chọn tệp `.ics` và hoàn tất.
  - *Trên iPhone:* Gửi tệp `.ics` qua Zalo/Email cho chính mình &rarr; Click trực tiếp vào tệp trên điện thoại &rarr; Chọn **Thêm tất cả sự kiện**.
* **Microsoft Outlook:** Chọn **File** &rarr; Chọn **Open & Export** &rarr; Chọn **Import/Export** &rarr; Chọn nạp tệp iCalendar (.ics) để đồng bộ!

---

## 📜 Giấy Phép (License)

Dự án được phân phối tự do dưới giấy phép **MIT**. Chi tiết xem tại tệp [LICENSE](./LICENSE).

---

## 🧸 Đóng Góp Ý Tưởng (Contribution)

Mọi ý tưởng cải tiến, thiết kế hay thêm thắt các tính năng ngọt ngào cho Pinkie đều được chào đón! Đừng ngần ngại mở một Issue hoặc gửi một Pull Request dễ thương nhé! 🌸
