# 🌸 Lịch Âm Việt Nam Tự Động Đồng Bộ — Pinkie Lunar Calendar 🌸

**Tiếng Việt** | [English](README_EN.md)
![Update Lunar Calendar ICS](https://github.com/justduyen/lich-am-viet-nam/actions/workflows/main.yml/badge.svg)

> [!quote] **Motto của JustDuyen**
> *Dành riêng cho những bạn nữ đáng yêu không rành công nghệ và những bạn nam ngọt ngào nhất ngoài kia~ (´｡• ᵕ •｡`) ♡*

Chào mừng bạn đến với **Pinkie Lunar Calendar**! Đây là bộ công cụ tối ưu giúp bạn **tạo và tự động đồng bộ Lịch Âm Việt Nam** vào điện thoại iPhone, Android, Google Calendar, Apple Calendar, và Microsoft Outlook. 

Dự án được thiết kế tỉ mỉ với giao diện Web GUI màu hồng pastel ngọt ngào, kính mờ sang trọng theo phong cách **Pinkie Suite**! 

Lịch bao gồm đầy đủ thông tin: các ngày lễ truyền thống Việt Nam, ngày sóc vọng (Mùng 1 & Rằm), Can Chi của ngày, và 24 Tiết khí thiên văn chuẩn xác từ năm **2026 đến 2060**.

---

## ⚡ CÁCH 1: Đồng Bộ Tự Động Qua URL (DỄ NHẤT & KHUYÊN DÙNG)
*Không cần cài đặt, không cần chạy code, lịch tự động cập nhật hàng năm!*

Bạn chỉ cần sao chép (copy) đường dẫn đăng ký vĩnh viễn dưới đây:

📌 **Đường dẫn đăng ký:** 
`https://raw.githubusercontent.com/justduyen/lich-am-viet-nam/main/output/viet_lunar_latest.ics`

### 📱 Cách tích hợp vào thiết bị của bạn:

* **Trên iPhone / iPad (Apple Calendar):**
  1. Vào **Cài đặt (Settings)** trên iPhone &rarr; Chọn **Lịch (Calendar)**.
  2. Chọn **Tài khoản (Accounts)** &rarr; Chọn **Thêm tài khoản (Add Account)**.
  3. Chọn **Khác (Other)** ở dưới cùng &rarr; Chọn **Thêm lịch đã đăng ký (Add Subscribed Calendar)**.
  4. Dán đường dẫn đăng ký ở trên vào và bấm **Tiếp theo (Next)** &rarr; **Lưu (Save)**. *Xong rồi! Lịch âm sẽ hiển thị ngay lập tức.*
  
* **Trên Google Calendar (Điện thoại Android / Máy tính):**
  1. Mở trang Web [calendar.google.com](https://calendar.google.com) trên trình duyệt máy tính.
  2. Ở thanh bên trái, tìm mục **Lịch khác (Other calendars)** và bấm vào dấu cộng **`+`**.
  3. Chọn **Từ URL (From URL)**.
  4. Dán đường dẫn đăng ký ở trên vào và bấm **Thêm lịch (Add calendar)**. Lịch sẽ tự động đồng bộ xuống điện thoại Android của bạn!

* **Trên Microsoft Outlook:**
  1. Chọn **File** &rarr; **Open & Export** &rarr; **Import/Export**.
  2. Chọn **Import an iCalendar (.ics) or vCalendar file (.vcs)**.
  3. Dán đường dẫn đăng ký ở trên vào mục URL và làm theo hướng dẫn để kết nối!

---

## 🎨 CÁCH 2: Tạo File Tùy Chỉnh Qua Giao Diện Web GUI (DỄ VỪA)
*Dành cho bạn muốn tự chọn khoảng năm mong muốn, chia nhỏ file hoặc nén tệp zip bằng giao diện trực quan siêu dễ thương.*

### 🛠️ Các bước thực hiện:

1. **Cài đặt Python 3.8+** trên máy tính của bạn.
2. Mở terminal/PowerShell và di chuyển vào thư mục dự án:
   ```bash
   cd "D:\Obsidian\1 dự án\Mini Apps\viet-lunar-calendar"
   ```
3. Kích hoạt môi trường ảo (Virtual Environment) và cài đặt thư viện phụ trợ:
   ```bash
   .venv\Scripts\activate        # Trên Windows
   # hoặc: source .venv/bin/activate trên Linux/macOS
   
   pip install -r requirements.txt
   ```
4. **Khởi chạy ứng dụng cực kỳ đơn giản:**
   ```bash
   python main.py
   ```
   *Chương trình sẽ tự động kích hoạt máy chủ Web cục bộ và **tự động mở trình duyệt** tại địa chỉ `http://localhost:8000` với giao diện màu hồng Pinkie tuyệt đẹp!*
5. Chọn khoảng năm bạn muốn tạo, tích chọn "Tạo file lẻ" nếu muốn, rồi bấm nút **Tạo Lịch Âm Việt Nam 🌸**. Sau đó nhấn **Tải về** trực tiếp trên các thẻ kết quả hiện ra!

---

## 💻 CÁCH 3: Chạy Qua Dòng Lệnh CLI (NÂNG CAO)
*Dành cho các lập trình viên muốn tự động hóa, tích hợp mã nguồn hoặc chạy trong các script CI/CD.*

Để sử dụng chế độ dòng lệnh thuần túy như phiên bản cũ, hãy sử dụng cờ `--cli` để bỏ qua việc mở trình duyệt:

```bash
# Tạo file tổng hợp mặc định từ năm 2026 đến 2031
python main.py --cli

# Tạo lịch lẻ từng năm kèm nén tệp ZIP tổng hợp
python main.py --cli --split

# Chỉ tạo tệp lịch âm cho một năm cụ thể
python main.py --cli --year 2026

# Tạo lịch âm cho một khoảng thời gian tùy ý
python main.py --cli --start 2026 --end 2035
```
*Tất cả các file kết quả sẽ được lưu trữ trực tiếp trong thư mục `output/`.*

---

## 📅 Các Ngày Lễ & Sự Kiện Được Tích Hợp

Lịch Âm của bạn sau khi đồng bộ sẽ có đầy đủ các sự kiện dễ thương sau:
- **🧧 Tết Nguyên Đán:** Từ mùng 1 đến mùng 3 tháng Giêng âm lịch.
- **💰 Ngày Vía Thần Tài:** Mùng 10 tháng Giêng âm lịch.
- **🏮 Rằm Tháng Giêng (Tết Nguyên Tiêu):** Ngày lễ chùa cầu an lớn nhất năm.
- **🌾 Giỗ Tổ Hùng Vương:** 10 tháng 3 âm lịch.
- **🪷 Đại Lễ Phật Đản:** 15 tháng 4 âm lịch.
- **🛶 Tết Đoan Ngọ:** Mùng 5 tháng 5 âm lịch.
- **🕯️ Đại Lễ Vu Lan (Rằm Tháng Bảy):** Mùa báo hiếu gia tiên.
- **🥮 Tết Trung Thu:** Rằm tháng Tám âm lịch.
- **🍳 Cúng Ông Công Ông Táo:** 23 tháng Chạp âm lịch.
- **🌌 Đêm Giao Thừa:** Ngày cuối cùng năm âm lịch.
- **🌑 Ngày Mùng 1 (Sóc) & 🌕 Ngày Rằm (Vọng) hàng tháng:** Tự động hiển thị và nhắc nhở ăn chay, đi lễ chùa cầu bình an!

---

## 📜 Giấy Phép (License)

Dự án được phân phối hoàn toàn miễn phí dưới giấy phép **MIT**. Chi tiết vui lòng xem tại tệp [LICENSE](./LICENSE).

---

## 🧸 Đóng Góp Ý Tưởng (Contribution)

Mọi ý tưởng đóng góp cải tiến, nâng cấp giao diện kính mờ Pinkie hay sửa lỗi đều rất đáng quý. Hãy gửi một Pull Request dễ thương hoặc mở một Issue nhé! Chúc bạn luôn có những ngày tháng ngập tràn niềm vui và may mắn! (´｡• ᵕ •｡`) ♡
