# 🥬 Ripely - Smart Grocery & Expiry Tracker

Ripely is an AI-powered tool that helps reduce food waste by scanning grocery receipts, tracking expiry dates, and suggesting recipes — all with minimal effort from the user. Designed especially for teens, families, and users with dietary needs like halal or vegetarian preferences.

---

## 🚀 Features

- 📸 **Receipt Scanning (OCR)** – Uses EasyOCR to extract grocery items from images.
- ⏳ **Expiry Date Tracking** – Logs items and sends reminders before expiry.
- 🍲 **Smart Recipe Suggestions** – Get ideas based on your fridge.
- 🏆 **Community Features** – Streaks, leaderboards, and shared dishes.
- 🙌 **Halal & Veg Modes** – Filter recommendations by dietary preference.

---

## 🧪 How to Run Locally

Make sure you have Python installed.

1. **Clone the repo**

```bash
git clone https://github.com/YOUR_USERNAME/ripely.git
cd ripely
Install dependencies

bash
Copy
Edit
pip install flask easyocr numpy pillow
Run the app

bash
Copy
Edit
python app.py
Test with cURL

bash
Copy
Edit
curl -X POST -F image=@sample_receipt.jpg http://localhost:3000/scan
🟢 You should see something like:

json
Copy
Edit
{
  "status": "success",
  "items_detected": ["Milk", "Eggs", "Apples", "Total", "15.99"]
}
🧠 Tech Stack
Frontend: Wix (members area + UI mockup)

Backend: Flask (Python on Replit)

OCR: EasyOCR

Hosting Attempts: Replit, Render, Fly.io

Version Control: GitHub

📊 Dataset & Preprocessing
No fixed dataset used; text dynamically extracted using OCR.

Images converted to RGB before processing.

Lightweight, fast processing pipeline.

🧱 Known Limitations
No database or persistent storage (yet).

Free hosting/storage limits (Replit & Render).

Backend not fully connected to Wix due to plan restrictions.

Needs manual expiry date entry (current OCR does not auto-detect dates).

🔮 Roadmap
✅ OCR prototype completed.

🔄 Link backend to Wix with cloud functions.

🧠 Add GPT-powered recipe suggestions.

📅 Add calendar sync + expiry timeline.

📦 Add barcode scanning for better accuracy.

