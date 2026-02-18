import streamlit as st
import random

st.set_page_config(page_title="Kids Math Tables App")

st.title("🧮 Kids Multiplication Tables App")

# ------------------------
# Sidebar
# ------------------------
mode = st.sidebar.selectbox(
    "Select Mode",
    ["Practice", "Examination"]
)

table = st.sidebar.selectbox(
    "Select Table",
    list(range(2, 21))
)

# ------------------------
# PRACTICE MODE
# ------------------------
if mode == "Practice":

    st.subheader("Practice Mode")

    a = st.number_input("Enter a number (1 to 10)", min_value=1, max_value=10, step=1)

    st.write(f"Question:  {table} × {a} = ?")

    answer = st.number_input("Write your answer", step=1, key="practice_answer")

    if st.button("Check Answer"):
        correct = table * a

        if answer == correct:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong. Correct answer is {correct}")



# ------------------------
# EXAM MODE
# ------------------------
if mode == "Examination":

    st.subheader("Examination Mode")

    # -------- session state --------
    if "q_no" not in st.session_state:
        st.session_state.q_no = 1

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "a" not in st.session_state:
        st.session_state.a = random.randint(1, 10)

    if "exam_input" not in st.session_state:
        st.session_state.exam_input = 0

    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    total_questions = 5

    # -------- exam finished --------
    if st.session_state.q_no > total_questions:

        st.success(
            f"Exam finished! Your score is {st.session_state.score} / {total_questions}"
        )

        if st.button("Restart Exam"):
            st.session_state.q_no = 1
            st.session_state.score = 0
            st.session_state.a = random.randint(1, 10)
            st.session_state.exam_input = 0
            st.session_state.submitted = False

    else:

        st.write(f"Question {st.session_state.q_no} of {total_questions}")
        st.write(f"{table} × {st.session_state.a} = ?")

        # ----- answer input (always visible) -----
        st.number_input(
            "Write your answer",
            step=1,
            key="exam_input"
        )

        col1, col2 = st.columns(2)

        # ----- Submit -----
        with col1:
            if st.button("Submit"):

                correct = table * st.session_state.a

                if st.session_state.exam_input == correct:
                    st.success("✅ Correct")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Wrong. Correct answer is {correct}")

                st.session_state.submitted = True

        # ----- Next Question -----
        with col2:
            if st.button("Next Question"):

                # move only if already submitted
                if st.session_state.submitted:

                    st.session_state.q_no += 1
                    st.session_state.a = random.randint(1, 10)

                    # reset answer for next question
                    st.session_state.exam_input = 0
                    st.session_state.submitted = False

                else:
                    st.warning("Please submit your answer first.")

    
