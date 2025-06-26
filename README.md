# 🧞 QuizGeini.ai

**AI-powered MCQ quiz generator from PDFs – built with Gemini API and Streamlit.**

> _"Upload a PDF. Get Instant MCQs. Ace Your Prep — Powered by Gemini + Magic ✨"_

---

## 📚 What is QuizGeini.ai?

**QuizGeini.ai** is a smart quiz generator that takes your class notes, lecture slides, or textbook content in **PDF form** and turns them into **auto-generated MCQs** you can practice instantly — with scoring!

Whether you're preparing for exams or brushing up on concepts, QuizGeini.ai saves you time and makes studying more interactive.

---

## ✨ Features

- 📄 Upload any **PDF file**
- 🤖 Uses **Google Gemini 1.5 Flash** to generate high-quality MCQs
- 📝 Take the quiz right in the app
- ✅ See your **score instantly**
- 🔁 Option to **regenerate** questions or **retake** the quiz
- 🎨 Clean UI + friendly experience

---

## 🛠️ Tech Stack

| Tool           | Use                                      |
|----------------|-------------------------------------------|
| Python         | Core programming                         |
| Streamlit      | Web UI frontend                          |
| Google Generative AI (Gemini) | MCQ generation            |
| PyMuPDF (fitz) | PDF text extraction                      |
| JSON           | MCQ formatting & quiz structure          |

---

## 🚀 Getting Started

Follow these steps to run QuizGeini.ai locally on your system:

1. **Clone the Repository**

```sh
git clone https://github.com/sania0607/quizgeini.ai.git
cd quizgeini.ai
```

2. **Install dependencies**  
```sh
pip install -r requirements.txt
```

3. **Create a `.env` file**  
In the project root, create a file named `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your-gemini-api-key-here
```

4. **Run the Streamlit app**  
```sh
streamlit run app.py
```

5. **Open the app in your browser**  
Go to [http://localhost:8501](http://localhost:8501) to use QuizGeini.ai.

---

**Note:**  
- You need a valid Gemini API key from Google.  
- Make sure your `.env` file is in the same directory as `app.py`.