# 🌸 Pinkie Lunar Calendar — Vietnamese Lunar Calendar 🌸

[Tiếng Việt](README.md) | **English**

![Update Lunar Calendar ICS](https://github.com/justduyen/viet-lunar-calendar/actions/workflows/main.yml/badge.svg)

> [!quote] **Brand Motto**
> *For all the cute girls who aren't super tech-savvy and the sweetest, gentlest boys out there~ (´｡• ᵕ •｡`) ♡*
> — **JustDuyen**

Welcome to **Pinkie Lunar Calendar**! An ultra-premium, cute, pastel pink iCalendar generator & Web GUI dashboard designed with love for cute girls and gentle boys ~ ♡ 

It generates beautiful `.ics` calendar files containing Vietnamese Lunar Calendar information (traditional holidays, monthly reminders, lunar phases, Can Chi, and Solar Terms) from **2026 to 2060** with a single click! 

These files can be imported effortlessly into Google Calendar, Apple Calendar (iPhone/Macbook), or Microsoft Outlook!

---

## ✨ Key Features (Pinkie Edition)

| Feature | Icon | Detailed Description |
| :--- | :---: | :--- |
| **🌸 Pinkie Web Dashboard** | `🧸` | A gorgeous, glassmorphic local Web GUI featuring custom year sliders, soft card curves, and an adorable **Light/Dark Mode** switcher. |
| **💖 Absolute Accuracy** | `✨` | Uses the highly precise astronomical `lunar-python` library based on Jean Meeus' algorithms. |
| **🎀 Ultra-Clean UI** | `🍃` | Keeps your calendar view pristine by placing technical details (Can Chi, Solar Terms) into the event Description rather than cluttering titles. |
| **🐾 Daily Lunar Display** | `🌱` | Displays daily lunar dates (e.g., `15/7`) directly on your devices with a soft pastel pink bar. |
| **⚙️ Monthly Automation** | `🔮` | Pre-integrated with **GitHub Actions** to automatically roll the calendar every month so you never have to reload. |

---

## 🚀 Installation

Requires **Python 3.8+** installed on your system.

```bash
# 1. Navigate to the project directory
cd "D:\Obsidian\1 dự án\Mini Apps\viet-lunar-calendar"

# 2. Activate virtual environment (recommended)
.venv\Scripts\activate        # On Windows
source .venv/bin/activate     # On Linux/macOS

# 3. Install required packages
pip install -r requirements.txt
```

---

## ▶️ Usage

By default, **Pinkie Lunar Calendar** starts a local web server and **automatically opens your web browser** in our sweet pink dashboard:

```bash
# 🌸 Run the gorgeous Pinkie Web GUI (Default)
python main.py
```
*Your browser will automatically launch at: `http://localhost:8000`*

---

### ⚙️ Backward-Compatible Command Line (CLI Mode):
If you want to run the calendar generator directly in your terminal for scripting or automation, pass the `--cli` flag:

```bash
# Generate the aggregate file via CLI
python main.py --cli

# Generate aggregate file + zip archive of split yearly files
python main.py --cli --split

# Generate calendar only for a specific year
python main.py --cli --year 2026

# Generate calendar for a custom year range
python main.py --cli --start 2026 --end 2035
```
*Generated files will be saved in the `output/` directory.*

---

## 🔗 Permanent Subscription Link (Highly Recommended)

To subscribe to a rolling calendar that automatically updates every month without manual re-imports, copy-paste this raw URL into your calendar app's subscription field:

📌 **Subscription URL:** `https://raw.githubusercontent.com/justduyen/viet-lunar-calendar/main/output/viet_lunar_latest.ics`

---

## 📅 Supported Traditional Holidays & Reminders

- **🧧 Lunar New Year (Tết Nguyên Đán):** 1st to 3rd of the 1st lunar month.
- **💰 God of Wealth Day (Vía Thần Tài):** 10th of the 1st lunar month.
- **🏮 Lantern Festival (Rằm Tháng Giêng):** Go to temples for blessings.
- **🌾 Hung Kings Commemoration Day:** 10th of the 3rd lunar month.
- **🪷 Vesak (Buddha's Birthday):** 15th of the 4th lunar month.
- **🛶 Double Fifth Festival (Tết Đoan Ngọ):** 5th of the 5th lunar month.
- **🕯️ Ghost Festival / Vu Lan:** 15th of the 7th lunar month.
- **🥮 Mid-Autumn Festival (Tết Trung Thu):** 15th of the 8th lunar month.
- **🍳 Kitchen Gods Day (Ông Công Ông Táo):** 23rd of the 12th lunar month.
- **🌌 New Year's Eve (Giao Thừa):** Final day of the lunar year.
- **🌑 Monthly 1st & 🌕 15th (Full Moon):** Prayers, temple visits, and vegetarian diet reminders.

---

## 📥 How to Import Into Your Devices

> [!tip]
> You can read interactive instructions directly on the **Pinkie Web Dashboard** when running!

* **Google Calendar:** Go to [calendar.google.com](https://calendar.google.com) &rarr; Click **⚙️ Settings** &rarr; Select **Import & Export** &rarr; Choose the downloaded `.ics` file and press **Import**.
* **Apple Calendar (iPhone/Macbook):**
  - *On Mac:* Open Calendar app &rarr; Go to **File** &rarr; Select **Import...** &rarr; Choose the `.ics` file.
  - *On iPhone:* Send the `.ics` file to yourself via Email/Zalo &rarr; Tap the file directly &rarr; Select **Add All Events**.
* **Microsoft Outlook:** Go to **File** &rarr; Select **Open & Export** &rarr; Select **Import/Export** &rarr; Choose **Import an iCalendar (.ics)** file to sync!

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 🧸 Contribution

Any cute ideas, styling suggestions, or premium additions to match the Pinkie Ecosystem are highly welcome! Feel free to open an Issue or submit a pull request! (´｡• ᵕ •｡`) ♡
