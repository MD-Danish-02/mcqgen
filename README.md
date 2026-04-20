# 📚 AI MCQ Generator (LLM Powered)

An AI-powered application that generates multiple-choice questions (MCQs) from PDF/TXT files using Large Language Models.

---

## 🚀 Live Demo

👉 https://mddanishgenai01-mcqgen-ai.hf.space

---

## 💡 About the Project

This project converts raw text into structured MCQs using AI.
Users can upload PDF or text files and instantly generate quiz questions with answers and evaluation.

---

## ✨ Features

* 📄 Upload PDF or TXT files
* 🤖 AI-generated MCQs with answers
* 🎯 Adjustable difficulty (Simple, Medium, Hard)
* 📊 Structured table output
* 📥 Download MCQs as CSV
* 🧠 AI-based quiz evaluation & analysis
* ⚡ Fast and user-friendly interface

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM Integration:** OpenAI + LangChain
* **Libraries:** Pandas, PyPDF2, Python-dotenv

---

## 📁 Project Structure

```bash
mcqgen/
│
├── streamlit_app.py          # Main application (entry point)
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
├── experiment/               # Experimental/learning code
└── mcqgenerator.egg-info/
```

---

## ⚠️ Important Note

👉 The **production-ready version** is deployed on Hugging Face
👉 Some folders (`experiment/`, `logs/`) are included for learning and testing purposes

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mcqgen.git
cd mcqgen
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Key

Create a `.env` file:

```bash
OPENAI_API_KEY=your_api_key_here
```

### 4. Run the application

```bash
streamlit run streamlit_app.py
```

---

## 🌐 Deployment

This project is deployed using **Hugging Face Spaces (Docker + Streamlit)**

👉 Live App:
https://mddanishgenai01-mcqgen-ai.hf.space

---

## 📌 Use Cases

* 📚 Students for practice quizzes
* 👨‍🏫 Teachers for test creation
* 📖 Content creators
* 🎯 Interview preparation

---

## 📌 Learnings

* Building LLM-powered applications
* Working with LangChain & OpenAI APIs
* Handling file uploads in Streamlit
* Debugging deployment issues (Docker & Hugging Face)
* Structuring real-world AI projects

---

## 🔮 Future Improvements

* Multi-language support
* Better UI/UX
* Authentication system
* PDF export for quizzes
* Advanced evaluation metrics

---

## 👨‍💻 Author

**Md Danish Alam**

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
