# 🧠 Prescription Scan App

A full-stack AI-powered app for scanning and understanding medical prescriptions using **Amazon Bedrock** for intelligent document processing. Built with Flask, this app helps clinics, pharmacists, and patients extract structured data from scanned prescriptions with ease.

---

## 🚀 Features

- 📤 Upload scanned prescriptions (handwritten or printed)
- ☁️ Server-side AI text extraction via **Amazon Bedrock**
- 🔍 Detects medicine names, dosages, frequencies, instructions
- 📄 Clean structured output (e.g., JSON or table)
- 🧩 Modular architecture with Flask backend

---

## 🛠️ Tech Stack

### ⚙️ Backend:
- **Python + Flask**
- **Amazon Bedrock** for LLM-powered extraction
- `utils/` for helper functions (e.g., file parsing, request handling)
- `models/` for Bedrock integration logic

### 💻 Frontend:
- HTML templates in `templates/`
- CSS and JS assets in `static/`

---

## 📂 Folder Structure

📁 static/         # JS, CSS, and assets  
📁 templates/      # Jinja2 HTML templates  
📁 models/         # Bedrock integration logic  
📁 utils/          # Helper functions (file handling, API formatting)  
📄 app.py          # Main Flask app  
📄 config.py       # Bedrock config & credentials  
📄 LICENSE  
📄 requirements.txt  
📄 README

---

## ⚙️ How It Works

1. User uploads a prescription via the UI.
2. Flask handles the file and passes it to Amazon Bedrock.
3. Bedrock processes and extracts relevant data using foundation models (e.g., Claude or Titan).
4. Parsed output is returned and displayed on-screen.

---

## 🌐 API Endpoints

| Method | Route       | Description                          |
|--------|-------------|--------------------------------------|
| POST   | `/upload`   | Accepts prescription image or PDF    |
| GET    | `/results`  | Returns parsed JSON output           |

---

## 🔐 Environment Setup

Create a `.env` or `config.py` file:
```
BEDROCK_ACCESS_KEY=
BEDROCK_SECRET_KEY=
BEDROCK_REGION=
FOUNDATION_MODEL_ID=
```

---

## 📦 Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

---

## 📄 License

Licensed under the [MIT License](LICENSE)

---

## ✨ Future Features

- 🧾 Export results to CSV or PDF
- 🧬 Drug interaction detection (via LLM)
- 🧠 Memory of past scans (per user)
- 📊 Dashboard analytics for clinics

---

## 👨‍⚕️ Author

Built with 💊 by [Divyansh723](https://github.com/Divyansh723)

---

> ✨ If you’re looking to host it for free (e.g., on Render or Replit) or connect Bedrock securely via AWS IAM roles, I can help you set it up step by step.
