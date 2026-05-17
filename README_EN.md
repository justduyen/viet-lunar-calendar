# 🌸 Lịch Âm Việt Nam Tự Động Đồng Bộ — Pinkie Lunar Calendar 🌸

[Tiếng Việt](README.md) | **English**

![Update Lunar Calendar ICS](https://github.com/justduyen/viet-lunar-calendar/actions/workflows/main.yml/badge.svg)

> [!quote] **Motto of JustDuyen**
> *For all the cute girls who aren't super tech-savvy and the sweetest, gentlest boys out there~ (´｡• ᵕ •｡`) ♡*

Welcome to **Pinkie Lunar Calendar**! An ultra-premium, cute, pastel pink iCalendar generator & Web GUI dashboard designed with love for cute girls and gentle boys ~ ♡

This project provides an easy way to **generate and automatically subscribe/sync the Vietnamese Lunar Calendar** to your devices: iPhone, iPad, Android, Google Calendar, Apple Calendar, and Microsoft Outlook.

Featuring a gorgeous, glassmorphic Web GUI styled after the **Pinkie Suite**, the calendar integrates all traditional Vietnamese holidays, monthly new moon/full moon reminders, and 24 solar terms from **2026 to 2060** with astronomical precision.

---

## ⚡ OPTION 1: Automatic Subscription via URL (EASIEST & RECOMMENDED)
*No installation, no code execution, and the calendar updates itself automatically every single year!*

Simply copy the raw subscription URL below:

📌 **Subscription URL:** 
`https://raw.githubusercontent.com/justduyen/viet-lunar-calendar/main/output/viet_lunar_latest.ics`

### 📱 How to Subscribe on Your Devices:

* **On iPhone / iPad (Apple Calendar):**
  1. Open **Settings** on your iOS device &rarr; Tap **Calendar**.
  2. Tap **Accounts** &rarr; Select **Add Account**.
  3. Select **Other** at the bottom &rarr; Choose **Add Subscribed Calendar**.
  4. Paste the Subscription URL above into the Server field and tap **Next** &rarr; **Save**. *All done! The lunar dates will now sync immediately.*
  
* **On Google Calendar (Android Phones / Desktop):**
  1. Open [calendar.google.com](https://calendar.google.com) on your computer's browser.
  2. On the left sidebar, find the **Other calendars** section and click the plus **`+`** icon.
  3. Select **From URL**.
  4. Paste the Subscription URL above and click **Add calendar**. The calendar will automatically sync down to all your connected Android devices!

* **On Microsoft Outlook:**
  1. Select **File** &rarr; **Open & Export** &rarr; **Import/Export**.
  2. Choose **Import an iCalendar (.ics) or vCalendar file (.vcs)**.
  3. Paste the Subscription URL above and follow the prompts to sync.

---

## 🎨 OPTION 2: Customize Calendar via Web GUI Dashboard (MEDIUM)
*Perfect if you want to generate a custom year range, split calendars into individual years, or pack a consolidated ZIP archive using a cute visual panel.*

### 🛠️ Execution Steps:

1. **Install Python 3.8+** on your computer.
2. Open your terminal/PowerShell and navigate to the project directory:
   ```bash
   cd "D:\Obsidian\1 dự án\Mini Apps\viet-lunar-calendar"
   ```
3. Activate the virtual environment and install dependencies:
   ```bash
   .venv\Scripts\activate        # On Windows
   # or: source .venv/bin/activate on Linux/macOS
   
   pip install -r requirements.txt
   ```
4. **Launch the application:**
   ```bash
   python main.py
   ```
   *The local server will start and **automatically open your web browser** at `http://localhost:8000` showing a gorgeous, pastel-pink control dashboard!*
5. Select your desired year range, tick options, and click **Tạo Lịch Âm Việt Nam 🌸**. Then click the sweet pink **Tải về** button on any of the generated cards!

---

## 💻 OPTION 3: Command Line Interface (CLI) Mode (ADVANCED)
*Designed for developers running scripts, custom cron jobs, or automated CI/CD pipelines.*

To bypass the web dashboard and execute calendar generation directly in your terminal, pass the `--cli` flag:

```bash
# Generate the aggregate calendar via CLI (2026 to 2031 by default)
python main.py --cli

# Generate aggregate calendar + split yearly files consolidated in a ZIP
python main.py --cli --split

# Generate calendar only for a specific year
python main.py --cli --year 2026

# Generate calendar for a custom year range
python main.py --cli --start 2026 --end 2035
```
*Generated files will be saved in the `output/` directory.*

---

## 📅 Supported Traditional Holidays & Reminders

Your synced calendar integrates these beautifully formatted events:
- **🧧 Lunar New Year (Tết Nguyên Đán):** 1st to 3rd of the 1st lunar month.
- **💰 God of Wealth Day (Vía Thần Tài):** 10th of the 1st lunar month.
- **🏮 Lantern Festival (Rằm Tháng Giêng):** Temple visits for early-year blessings.
- **🌾 Hung Kings Commemoration Day:** 10th of the 3rd lunar month.
- **🪷 Vesak (Buddha's Birthday):** 15th of the 4th lunar month.
- **🛶 Double Fifth Festival (Tết Đoan Ngọ):** 5th of the 5th lunar month.
- **🕯️ Ghost Festival / Vu Lan:** 15th of the 7th lunar month.
- **🥮 Mid-Autumn Festival (Tết Trung Thu):** 15th of the 8th lunar month.
- **🍳 Kitchen Gods Day (Ông Công Ông Táo):** 23rd of the 12th lunar month.
- **🌌 New Year's Eve (Giao Thừa):** Final day of the lunar year.
- **🌑 Monthly 1st & 🌕 15th (Full Moon):** Automatic temple and vegetarian diet reminders!

---

## 📜 License

This project is released under the **MIT License**. For more details, see the [LICENSE](./LICENSE) file.

---

## 🧸 Contribution

All premium UI styling ideas, functional suggestions, or improvements to match the Pinkie Ecosystem are highly welcome! Feel free to open a cute Issue or submit a Pull Request! (´｡• ᵕ •｡`) ♡
