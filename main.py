import os
import json
import re
import pandas as pd
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import ollama

# -----------------------------
#  Setup
# -----------------------------
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

MODEL = "gemma3:1b"

# -----------------------------
#  JSON Handling
# -----------------------------
def extract_and_clean_json(text: str) -> str:
    """Extracts and sanitizes a JSON block from messy LLM output."""
    text = text.replace("```json", "").replace("```", "")
    if "{" in text and "}" in text:
        start = text.find("{")
        end = text.rfind("}") + 1
        text = text[start:end]

    # 🧹 Remove invisible characters and trailing commas
    text = re.sub(r"[^\x09\x0A\x0D\x20-\x7E\u0600-\u06FF]", "", text)
    text = re.sub(r",\s*}", "}", text)   # ✅ Remove trailing commas
    text = re.sub(r",\s*]", "]", text)
    text = re.sub(r"(?<!\\)'", '"', text)  # Replace single quotes
    return text.strip()


def safe_parse_json(text: str) -> dict:
    """Parses and returns JSON safely, even if it's malformed."""
    text = extract_and_clean_json(text)
    try:
        data = json.loads(text)
        return data.get("results", data)
    except Exception:
        # Try to fix broken keys or partial JSON
        repaired = re.sub(r'([{,]\s*)([A-Za-z0-9_]+)\s*:', r'\1"\2":', text)
        repaired = re.sub(r",\s*}", "}", repaired)
        try:
            data = json.loads(repaired)
            return data.get("results", data)
        except Exception as e:
            return {"خطا در پردازش پاسخ": f"{type(e).__name__}: {e}", "raw_output": text[:4000]}

# -----------------------------
#  AI Analysis
# -----------------------------
def analyze_with_ai(products_data, batch_size=4):
    """Analyzes products in smaller batches for performance."""
    system_prompt = (
        "تو یک تحلیلگر حرفه‌ای نظرات مشتریان هستی. "
        "لیستی از محصولات و نظرات آن‌ها داده می‌شود. "
        "برای هر محصول یک پاراگراف کوتاه به زبان فارسی بنویس "
        "(۴ تا ۶ جمله). فقط خروجی JSON زیر را بده:\n"
        "{ \"results\": { \"نام محصول\": \"تحلیل کوتاه\" } }"
    )

    all_results = {}

    for i in range(0, len(products_data), batch_size):
        batch = products_data[i : i + batch_size]
        user_prompt = f"لیست محصولات و نظرات:\n{json.dumps(batch, ensure_ascii=False)}"

        try:
            response = ollama.chat(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                options={"temperature": 0.3},
            )
            raw = response["message"]["content"]
        except Exception as e:
            all_results[f"⚠️ خطا در دسته {i//batch_size+1}"] = str(e)
            continue

        # ✅ Parse safely without crashing
        batch_results = safe_parse_json(raw)
        if isinstance(batch_results, dict):
            all_results.update(batch_results)

    return all_results

# -----------------------------
#  Routes
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": None, "error": None})


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, file: UploadFile = File(...)):
    try:
        if file.filename.endswith(".xlsx"):
            df = pd.read_excel(file.file)
        elif file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)
        else:
            return templates.TemplateResponse("index.html", {"request": request, "error": "فرمت فایل باید Excel یا CSV باشد", "results": None})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "error": f"خطا در خواندن فایل: {e}", "results": None})

    # Validate columns
    df.columns = [c.lower().strip() for c in df.columns]
    if not {"product", "comment"}.issubset(df.columns):
        return templates.TemplateResponse("index.html", {"request": request, "error": "ستون‌های لازم: product و comment", "results": None})

    # Group comments by product
    products_data = []
    for product, group in df.groupby("product"):
        comments = group["comment"].dropna().astype(str).tolist()[:20]
        if comments:
            products_data.append({"product": product, "comments": comments})

    if not products_data:
        return templates.TemplateResponse("index.html", {"request": request, "error": "هیچ داده‌ای برای تحلیل وجود ندارد.", "results": None})

    # Run the AI analysis
    results = analyze_with_ai(products_data, batch_size=4)

    return templates.TemplateResponse("index.html", {"request": request, "results": results, "error": None})
