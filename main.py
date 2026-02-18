import streamlit as st
import random

st.set_page_config(page_title="Kids Math Tables App")

st.title("🧮 Kids Multiplication Tables App")

# ------------------------
# Sidebar
# ------------------------
mode = st.sidebar.selectbox(
    "Select Mode",
    ["Practice"]
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


