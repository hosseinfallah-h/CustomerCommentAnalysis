# 📊 Customer Comment Analyzer — Local AI with Ollama

Analyze customer comments about multiple products **locally** with AI — no internet required.

This app uses **FastAPI + Gemma 3:1B (via Ollama)** to read product reviews (Excel / CSV), summarize insights, and display each product’s summary beautifully on a modern web interface.

---

## 🚀 Features

- 📂 Upload Excel (`.xlsx`) or CSV files with `product` and `comment` columns  
- 🤖 Analyze comments locally using `gemma3:1b`  
- 🧠 Automatic grouping by product  
- ⚡ Robust JSON handling (no crashes, even with malformed responses)  
- 💎 Glassmorphic Persian UI  
- 🖥️ Works fully **offline**

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | FastAPI |
| **Frontend** | HTML + Jinja2 + Tailwind |
| **AI Engine** | Ollama (Gemma 3:1B) |
| **Data** | Pandas |
| **Server** | Uvicorn |

---

## ⚙️ Installation & Run Guide

### 🪄 Step 1 – Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/CustomerCommentAnalyzer.git
cd CustomerCommentAnalyzer
🧩 Step 2 – Create a virtual environment
bash
Copy code
python -m venv .venv
Activate it:

Windows PowerShell

bash
Copy code
.venv\Scripts\Activate.ps1
Linux / macOS

bash
Copy code
source .venv/bin/activate
📦 Step 3 – Install dependencies
bash
Copy code
pip install -r requirements.txt
🤖 Step 4 – Install the AI model
Make sure Ollama is installed and running, then pull the model:

bash
Copy code
ollama pull gemma3:1b
🧠 Step 5 – Run the app
bash
Copy code
uvicorn main:app --reload
Visit → http://127.0.0.1:8000

📂 Project Structure
cpp
Copy code
CustomerCommentAnalyzer/
├── main.py
├── templates/
│   └── index.html
├── static/
├── uploads/
│   └── .gitkeep
├── requirements.txt
├── .gitignore
└── README.md
📊 Example Dataset
product	comment
iPhone 13	عملکرد عالی و شارژ سریع
iPhone 14 Pro	طراحی زیبا ولی باتری ضعیف
iPhone 15 Pro Max	گران ولی فوق‌العاده قدرتمند

Save this as dataset.xlsx or dataset.csv and upload it in the app.

🧠 Local Model Notes
You can switch the model easily in main.py:

python
Copy code
MODEL = "gemma3:1b"
Other working local models (if installed):

python
Copy code
MODEL = "qwen2.5:1.5b"
MODEL = "deepseek-coder:6b"
🧾 License
MIT License © 2025 Hossein Fallah

🧭 Upcoming Updates
Here are 20 planned improvements already structured for GitHub milestones:

✨ Add real-time progress bar during batch analysis

📊 Add product sentiment score visualization (positive/negative)

🧾 Export results as Excel or PDF

💬 Multilingual support (English, Arabic, Persian)

🧠 Choose model dynamically from UI

🖥️ Dockerfile for easy deployment

📦 Add REST API endpoint for programmatic access

📈 Include token usage and model speed metrics

🔐 Add optional login system for users

🎨 Add dark / light mode switch

⚙️ Configurable batch size from UI

🌐 Add file upload progress indicator

📂 Store previous analyses locally

📡 WebSocket live updates (no reload needed)

🪶 Responsive UI improvements for mobile

📊 Add chart view for keyword frequency

🧮 Implement sentiment classification heatmap

🧱 Convert to Progressive Web App (PWA)

🧰 Add command-line interface (CLI) tool

🤝 Integrate HuggingFace local models option

⭐ Contribute
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to improve.

📧 Author
Hossein Fallah
GitHub @hosseinfallah-h



---
