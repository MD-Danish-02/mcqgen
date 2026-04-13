import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv

from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging

# LangChain (NEW)
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load env
from dotenv import load_dotenv


load_dotenv(dotenv_path="D:/mcqgen/.env")

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")   # ✅ FIX
)

# ------------------- QUIZ GENERATION -------------------

template = """
Text: {text}

You are an expert MCQ maker. Given the above text, it is your job to create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.

Make sure:
- Questions are not repeated
- Questions are relevant to the text
- Follow the format strictly

Return ONLY valid JSON. Do not include any extra text.

{response_json}
"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=template
)

quiz_chain = quiz_generation_prompt | llm | StrOutputParser()   # ✅ FIX

# ------------------- REVIEW -------------------

template2 = """
You are an expert English grammarian and writer.

Given a Multiple Choice Quiz for {subject} students, evaluate the complexity of the questions and provide a complete analysis of the quiz.

- Keep the analysis within 50 words
- If the quiz is not appropriate for the students, update the questions
- Adjust the tone so it perfectly fits the student level

QUIZ_MCQs:
{quiz}

Provide your evaluation and improved version (if needed):
"""

quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=template2
)

review_chain = quiz_evaluation_prompt | llm | StrOutputParser()   # ✅ FIX

# ------------------- MAIN FUNCTION -------------------

def generate_evaluate_chain(inputs):
    quiz_output = quiz_chain.invoke(inputs)

    review_output = review_chain.invoke({
        "subject": inputs["subject"],
        "quiz": quiz_output
    })

    return {
        "quiz": quiz_output,
        "review": review_output
    }