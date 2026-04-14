import os
import json
import traceback
import pandas as pd
import streamlit as st

from dotenv import load_dotenv

# LangChain callback
from langchain_community.callbacks import get_openai_callback

# Custom modules
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging


# -------------------- LOAD ENV --------------------
load_dotenv()


# -------------------- LOAD RESPONSE JSON --------------------
file_path = os.path.join(os.getcwd(), "Response.json")

with open(file_path, 'r') as file:
    RESPONSE_JSON = json.load(file)


# -------------------- UI TITLE --------------------
st.title("📚 AI MCQ Generator")
st.markdown("Generate MCQs from PDF/TXT using AI 🚀")


# -------------------- FORM --------------------
with st.form("user_inputs"):

    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50, value=5)

    subject = st.text_input("Insert Subject", placeholder="e.g. Machine Learning")

    tone = st.selectbox("Complexity Level", ["Simple", "Medium", "Hard"])

    button = st.form_submit_button("🚀 Create MCQs")


# -------------------- MAIN LOGIC --------------------
if button and uploaded_file is not None and subject and tone:

    with st.spinner("Generating MCQs... ⏳"):
        try:
            text = read_file(uploaded_file)

            with get_openai_callback() as cb:

                response = generate_evaluate_chain({
                    "text": text,
                    "number": mcq_count,
                    "subject": subject,
                    "tone": tone,
                    "response_json": json.dumps(RESPONSE_JSON)
                })

            # -------------------- OUTPUT --------------------
            quiz = response["quiz"]
            review = response["review"]

            st.success("MCQs generated successfully ✅")

            # -------------------- TABLE --------------------
            table_data = get_table_data(quiz)

            if table_data:
                df = pd.DataFrame(table_data)
                df.index = df.index + 1

                st.subheader("📊 MCQ Table")
                st.table(df)

                # -------------------- REVIEW (CLEAN FIX) --------------------
                # sirf analysis part nikalo
                # -------------------- REVIEW CLEAN FIX --------------------
                analysis = review.split("{")[0].strip()

                st.subheader("🧠 Review")
                st.write(analysis)
                # -------------------- DOWNLOAD --------------------
                csv = df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    "📥 Download MCQs",
                    csv,
                    "mcqs.csv",
                    "text/csv"
                )

            else:
                st.error("Error in converting quiz to table")

            # -------------------- TOKEN INFO --------------------
            st.subheader("📈 Usage Info")
            st.write("Total Tokens:", cb.total_tokens)
            st.write("Prompt Tokens:", cb.prompt_tokens)
            st.write("Completion Tokens:", cb.completion_tokens)
            st.write("Total Cost:", cb.total_cost)

        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            st.error("Something went wrong ❌")


# -------------------- FALLBACK --------------------
elif button:
    st.warning("Please fill all fields and upload a file ⚠️")