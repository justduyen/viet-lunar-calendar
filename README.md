<!-- SEO Metadata -->
<meta name="description" content="Tự động đồng bộ Lịch Âm Việt Nam chuẩn xác tối giản">
<meta name="keywords" content="lich am viet nam, pinkie lunar calendar, dong bo lich am, lich am ics, justduyen, pinkie suite">
<meta name="author" content="justduyen">

## 🌸 Lịch Âm Việt Nam Tự Động Đồng Bộ 🌸
<img width="1574" height="785" alt="screenshot-licham" src="https://github.com/user-attachments/assets/64fc3e3d-d883-4504-84a3-e5f797dbb7e2" />

### 1. Giới thiệu

`Lịch Âm Việt Nam Tự Động Đồng Bộ` giúp tự động đồng bộ Lịch Âm Việt Nam trực tiếp vào Google Calendar và thiết bị của bạn. Chỉ cần đăng ký một lần bằng đường dẫn URL là lịch tự chạy và cập nhật trọn đời, không cần cài đặt phức tạp.

Lịch bao gồm đầy đủ thông tin:
- Các ngày lễ truyền thống Việt Nam và Quốc tế 
- Ngày cúng gia tiên theo văn hoá người Việt (Mùng 1 & Rằm)
- Các thông tin về Can Chi và 24 Tiết khí thiên văn.

---

### 2. Cách dùng

#### 🎈 Cách 1: Đồng bộ tự động qua URL(dễ nhất & khuyên dùng)
Copy link đăng ký lịch → thêm lịch mới:

```text
https://raw.githubusercontent.com/justduyen/lich-am-viet-nam/main/output/viet_lunar_latest.ics
```

- iPhone/iPad: Cài đặt → Lịch → Tài khoản → Thêm tài khoản → Khác → Thêm lịch đã đăng ký → Dán link → Lưu.

- PC/Laptop: Vào calendar.google.com → Nhấn + tại Lịch khác → Từ URL → Dán link.

- Outlook: File → Open & Export → Import/Export → Import an iCalendar (.ics) → Dán link.

#### 🛠️ Cách 2: Chạy Code / Tùy biến(dành cho dev)

```Bash
pip install -r requirements.txt
python main.py          # Chạy Web GUI (localhost:8000) tự động tạo file theo ý muốn
python main.py --cli    # Chạy nhanh qua dòng lệnh (CLI)
```
### 3. Chức năng

* 📅 Đồng bộ trực quan, tiện lợi:
    * Hiển thị Lịch Âm trực tiếp dưới Lịch Dương trên Google Calendar, Apple Calendar, Outlook vô cùng gọn gàng.
    * Tự động cập nhật trọn đời, không cần thao tác thủ công hàng năm.
* 🧧 Đầy đủ các ngày lễ truyền thống Việt Nam:
    * Tết cổ truyền: Đêm Giao Thừa, Tết Nguyên Đán (Mùng 1 - Mùng 3), Cúng Ông Công Ông Táo (23 Chạp), Ngày Vía Thần Tài (Mùng 10 tháng Giêng).
    * Lễ hội dân gian: Giỗ Tổ Hùng Vương (10/3 âm lịch), Tết Đoan Ngọ (5/5 âm lịch), Tết Trung Thu (Rằm tháng 8).
    * Tâm linh & Phật giáo: Rằm Tháng Giêng (Tết Nguyên Tiêu), Đại Lễ Phật Đản (15/4 âm lịch), Lễ Vu Lan báo hiếu (Rằm tháng 7).
* 🌑 Tiện ích nhắc nhở định kỳ:
    * Tự động nhắc nhở ngày Mùng 1 (Sóc) và Ngày Rằm (Vọng) hàng tháng để bạn tiện sửa soạn đi chùa, ăn chay.
* 🌌 Thiên văn & Can Chi học:
    * Xem chính xác Can Chi của ngày (ví dụ: Giáp Tý, Ất Sửu,...).
    * Cập nhật chuẩn xác 24 Tiết khí thiên văn học (Lập Xuân, Xuân Phân, Hạ Chí, Thu Phân, Đông Chí,...).

### 4. Kết nối & Bản quyền
- Phát hành hoàn toàn miễn phí dưới giấy phép MIT.
- Mọi ý tưởng hoặc báo lỗi, vui lòng gửi Issue / Pull Request.
