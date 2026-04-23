# 🌙 Vietnamese Lunar Calendar — iCalendar Generator

[Tiếng Việt](./README.md) | **English**

![Update Lunar Calendar ICS](https://github.com/justduyen/viet-lunar-calendar/actions/workflows/main.yml/badge.svg)

This **Nature-themed** 🌿 project generates `.ics` files containing Vietnamese Lunar Calendar information (including traditional holidays, Can Chi, and Solar Terms) from **2026 to 2031** (5-year rolling). These files can be easily imported into Google Calendar, Apple Calendar, or Outlook.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| **🌿 High Accuracy** | Uses the `lunar-python` library based on precise astronomical algorithms (Jean Meeus). |
| **🌸 All-in-One** | Includes Lunar holidays, Vietnamese National holidays, and International days (Valentine, 8/3, etc.). |
| **🍃 Clean UI** | Technical details (Can Chi, Solar Terms) are moved to the Description to keep the titles clean. |
| **🌱 Daily Display** | Shows the lunar date for every single day (e.g., `15/7`) with a soft green bar. |
| **⚙️ Automation** | Integrated with GitHub Actions to automatically roll the calendar every month. |

---

## 🔗 Permanent Subscription Link (Recommended)

To keep your calendar updated automatically without manual intervention, use the following Raw URL to subscribe in your calendar app:

**URL:** `https://raw.githubusercontent.com/justduyen/viet-lunar-calendar/main/output/viet_lunar_latest.ics`

---

## 🚀 Installation

Requires **Python 3.8+**.

```bash
# 1. Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# 2. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the following command to generate the calendar files:

```bash
# Generate the 5-year rolling aggregate file (default)
python main.py

# Generate with split yearly files and a zip archive
python main.py --split
```

Results are saved in the `output/` directory.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 🤝 Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.
