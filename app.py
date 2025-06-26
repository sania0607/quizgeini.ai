import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai
import json

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

if not api_key:
    st.error("⚠️ API Key not found. Please set GEMINI_API_KEY in your .env file.")


# Extract text from PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "".join(page.get_text() for page in doc)

# Get Gemini Response
def get_mcqs(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text  # way to extract content
    except Exception as e:
        return f"❌ Error: {e}"

# Parse MCQs from Gemini's JSON
def parse_json_mcqs(response_text):
    try:
        json_start = response_text.find("[")
        json_end = response_text.rfind("]") + 1
        json_text = response_text[json_start:json_end].strip()
        mcqs = json.loads(json_text)
        return mcqs
    except Exception as e:
        st.error("⚠️ Failed to parse JSON. Check Gemini's response format.")
        st.text_area("Gemini Response (for debugging)", response_text, height=300)
        return []

#  Streamlit UI
st.set_page_config(page_title=" QuizGeini.ai")
st.title("🧞 QuizGeini.ai")
st.markdown("**Upload a PDF. Get Instant MCQs. Ace Your Prep — Powered by Gemini + Magic ✨**")


uploaded_file = st.file_uploader("📄 Upload a PDF", type="pdf")

num_mcqs = st.number_input("🧠 How many MCQs do you want?", min_value=1, max_value=20, value=5, step=1)

if uploaded_file:
    extracted_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ Text Extracted!")

    with st.expander("📖 View Extracted Text"):
        st.text_area("Extracted Text", extracted_text, height=200)

    if st.button("🚀 Generate Quiz"):
        with st.spinner("Creating MCQs...."):
            prompt = f"""
Generate {num_mcqs} multiple choice questions based on the text below.

Each question must follow this JSON format:
[
  {{
    "question": "What is photosynthesis?",
    "options": {{
      "A": "A process to make water",
      "B": "A way to absorb CO2",
      "C": "A process by which plants make food",
      "D": "None of the above"
    }},
    "correct": "C"
  }},
  ...
]

Do NOT add any explanation or commentary. Just return the pure JSON list.

Text:
{extracted_text}
"""
            gemini_response = get_mcqs(prompt)
            mcqs = parse_json_mcqs(gemini_response)

            if mcqs:
                st.session_state["mcqs"] = mcqs
                st.session_state["submitted"] = False
                st.session_state["score"] = 0
            else:
                st.error("❌ Could not extract MCQs from Gemini response.")

#  Show Quiz Form
if "mcqs" in st.session_state and not st.session_state.get("submitted", False):
    st.subheader("📝 Your Quiz")
    with st.form("quiz_form"):
        user_answers = {}
        for idx, mcq in enumerate(st.session_state["mcqs"]):
            st.write(f"**Q{idx+1}. {mcq['question']}**")
            user_answers[idx] = st.radio(
                "Choose an answer:",
                options=list(mcq["options"].keys()),
                format_func=lambda k: f"{k}) {mcq['options'][k]}",
                key=f"q{idx}"
            )
        submitted = st.form_submit_button("✅ Submit Answers")

        if submitted:
            score = 0
            for i, mcq in enumerate(st.session_state["mcqs"]):
                if user_answers[i] == mcq["correct"]:
                    score += 1
            st.session_state["score"] = score
            st.session_state["submitted"] = True

# Show Result
if st.session_state.get("submitted", False):
    st.success(f"🎉 Your Score: {st.session_state['score']} / {len(st.session_state['mcqs'])}")
    if st.button("🔁 Retake Quiz"):
        st.session_state.clear()
        st.rerun()
#  Footer
st.markdown(
    """
    <hr style="margin-top: 50px; border: none; border-top: 1px solid #ddd;">
    <div style='text-align: center; color: grey; font-size: 14px;'>
        Made with 💚 by <strong>Sania Rajput</strong> | Powered by <a href="https://deepmind.google/technologies/gemini/" target="_blank">Gemini</a> 🚀
    </div>
    """,
    unsafe_allow_html=True
)



