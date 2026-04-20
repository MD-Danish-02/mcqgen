# 📚 AI MCQ Generator (LLM Powered)

An AI-powered application that generates multiple-choice questions (MCQs) from PDF/TXT files using Large Language Models.

---

## 🚀 Live Demo

👉 https://mddanishgenai01-mcqgen-ai.hf.space

---

## 💡 About the Project

This project converts raw text into structured MCQs using AI.
It supports file uploads, difficulty selection, and generates downloadable quizzes.

---

## ✨ Features

* 📄 Upload PDF or TXT files
* 🤖 AI-generated MCQs
* 🎯 Difficulty levels (Simple, Medium, Hard)
* 📊 Tabular output
* 📥 CSV download
* 🧠 AI-based evaluation

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* OpenAI API
* Pandas

---

## 📁 Project Structure

```bash
mcqgen/
│
├── streamlit_app.py          # Main app (entry point)
├── Response.json             # Output format template
├── requirements.txt
├── setup.py
├── test.py
├── data.txt
│
├── src/
│   └── mcqgenerator/
│       ├── MCQGenerator.py
│       ├── utils.py
│       ├── logger.py
│       └── __init__.py
│
├── logs/                     # Logging files
├── experiment/               # Experimental code
└── mcqgenerator.egg-info/
```

---

## ⚠️ Important Note

👉 The **production-ready version** is deployed on Hugging Face
👉 Some folders like `experiment/` and `logs/` are for learning and testing purposes

---

## ⚙️ Run Locally

```bash
git clone https://github.com/your-username/mcqgen.git
cd mcqgen
pip install -r requirements.txt
```

Create `.env` file:

```bash
OPENAI_API_KEY=your_api_key_here
```

Run:

```bash
streamlit run streamlit_app.py
```

---

## 🌐 Deployment

Deployed on Hugging Face Spaces (Docker + Streamlit)

👉 Live App:
https://mddanishgenai01-mcqgen-ai.hf.space

---

## 📌 Learnings

* Handling file uploads in Streamlit
* Integrating LLMs using LangChain
* Debugging Docker & deployment issues
* Managing project structure for production

---

## 🔮 Future Improvements

* UI enhancement
* Multi-language support
* Authentication system
* Better evaluation logic

---

## 👨‍💻 Author

**Mohammad Daanish**

---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub!
