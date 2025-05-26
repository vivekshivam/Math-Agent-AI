# 🤖 Math AI Agent – Human-in-the-Loop Math Tutor

An AI-powered math assistant that combines a curated **Knowledge Base (KB)** with **GPT-4 fallback** to solve mathematical queries step-by-step. Designed to simulate a professor-like tutor, it also includes **human-in-the-loop feedback** and **guardrails** for safe, accurate responses.

---

## 🚀 Features

- 📚 Knowledge-first search for faster and verified answers  
- 🤖 Fallback to OpenAI GPT-4 for complex/unknown problems  
- 🧠 Step-by-step solution generation like a math tutor  
- 🔁 Human-in-the-loop feedback system to improve performance  
- 🛡️ Guardrails to detect hallucinations or unsafe content  
- 🌗 Dark mode compatible UI (Flask/HTML or Streamlit-ready)

---

## 🗂️ Project Structure

```
math-agent/
├── app.py                # Main Flask app
├── templates/index.html  # Frontend UI
├── utils/                # KB search & feedback handler
│   ├── kb_search.py
│   ├── web_search.py
│   └── feedback_handler.py
├── .env                  # Stores API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Vivekshivam/Math-Agent-AI.git
cd Math-Agent-AI
```

### 2. Create & Activate Virtual Environment

**On Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your `.env` File
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your-openai-key-here
SERPER_API_KEY=your-serper-key-here  # Optional, for web search
```

---

## ▶️ Running the App

Run the Flask app:
```bash
python app.py
```

Then open your browser and go to:  
`http://127.0.0.1:5000`

---

## 🛡️ Security Notes

- Kee
