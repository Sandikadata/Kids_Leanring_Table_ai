import streamlit as st
import langchainanstable

st.title(" Multiplication Table Practice")

number = st.sidebar.selectbox(
    "Pick a number",
    list(range(2, 21))
)

if number:

    if st.button("Generate Questions"):
        response = langchainanstable.generate_multiplication_questions_with_answers(number)

        st.session_state["questions"] = response["questions"]
        st.session_state["answers"] = response["answers"]

# -------------------------
# Show questions
# -------------------------
if "questions" in st.session_state:

    st.subheader("Questions")

    for q in st.session_state["questions"]:
        st.write(q)

    # -------------------------
    # Show answers button
    # -------------------------
    if st.button("Show Answers"):

        st.subheader("Answers")

        for ans in st.session_state["answers"]:
            st.write(ans)
