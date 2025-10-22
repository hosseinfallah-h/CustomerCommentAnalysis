````markdown
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
````

### 🧩 Step 2 – Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**

```bash
.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

### 📦 Step 3 – Install dependencies

```bash
pip install -r requirements.txt
```

---

### 🤖 Step 4 – Install the AI model

Make sure [Ollama](https://ollama.ai) is installed and running, then pull the model:

```bash
ollama pull gemma3:1b
```

---

### 🧠 Step 5 – Run the app

```bash
uvicorn main:app --reload
```

Visit → [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Project Structure

```bash
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
```

---

## 📊 Example Dataset

| product           | comment                     |
| ----------------- | --------------------------- |
| iPhone 13         | عملکرد عالی و شارژ سریع     |
| iPhone 14 Pro     | طراحی زیبا ولی باتری ضعیف   |
| iPhone 15 Pro Max | گران ولی فوق‌العاده قدرتمند |

Save this as `dataset.xlsx` or `dataset.csv` and upload it in the app.

---

## 🧠 Local Model Notes

You can switch the model easily in `main.py`:

```python
MODEL = "gemma3:1b"
```

Other working local models (if installed):

```python
MODEL = "qwen2.5:1.5b"
MODEL = "deepseek-coder:6b"
```

---

## 🧾 License

**MIT License © 2025 Hossein Fallah**

---

## 🧭 Upcoming Updates

Here are 20 planned improvements already structured for GitHub milestones:

1. ✨ Add real-time progress bar during batch analysis
2. 📊 Add product sentiment score visualization (positive/negative)
3. 🧾 Export results as Excel or PDF
4. 💬 Multilingual support (English, Arabic, Persian)
5. 🧠 Choose model dynamically from UI
6. 🖥️ Dockerfile for easy deployment
7. 📦 Add REST API endpoint for programmatic access
8. 📈 Include token usage and model speed metrics
9. 🔐 Add optional login system for users
10. 🎨 Add dark / light mode switch
11. ⚙️ Configurable batch size from UI
12. 🌐 Add file upload progress indicator
13. 📂 Store previous analyses locally
14. 📡 WebSocket live updates (no reload needed)
15. 🪶 Responsive UI improvements for mobile
16. 📊 Add chart view for keyword frequency
17. 🧮 Implement sentiment classification heatmap
18. 🧱 Convert to Progressive Web App (PWA)
19. 🧰 Add command-line interface (CLI) tool
20. 🤝 Integrate HuggingFace local models option

---

## ⭐ Contribute

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to improve.

---

## 📧 Author

**Hossein Fallah**
GitHub: [@hosseinfallah-h](https://github.com/hosseinfallah-h)

---

### ✅ Summary of What This README Includes

| Section              | Purpose                    |
| -------------------- | -------------------------- |
| 🔹 Intro             | What the app does          |
| 🔹 Features          | Key highlights             |
| 🔹 Tech Stack        | Components used            |
| 🔹 Setup & Run       | All exact commands         |
| 🔹 Folder Structure  | Visual project map         |
| 🔹 Dataset Example   | Example table              |
| 🔹 Local Model       | How to change the AI model |
| 🔹 Future Updates    | 20 ready milestone ideas   |
| 🔹 License & Credits | Author info                |

````
