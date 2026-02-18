from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
api_key = os.getenv("GEMINI_API_KEY")
import re


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)


def generate_multiplication_questions_with_answers(number):

    template = """
    Create 10 multiplication questions for table of {number}.
    Format each question exactly like:
    {number} x 1 = ?
    {number} x 2 = ?
    ...
    """

    prompt = PromptTemplate(
        input_variables=["number"],
        template=template
    )

    chain = prompt | llm | StrOutputParser()

    questions_text = chain.invoke(
        {"number": number}
    )

    questions = []
    answers = []

    for line in questions_text.split("\n"):
        line = line.strip()
        if not line:
            continue

        # Extract numbers using regex
        match = re.search(r"(\d+)\s*x\s*(\d+)", line)
        if match:
            a = int(match.group(1))
            b = int(match.group(2))
            questions.append(line)
            answers.append(f"{a} x {b} = {a*b}")

    return {
        "questions": questions,
        "answers": answers
    }
