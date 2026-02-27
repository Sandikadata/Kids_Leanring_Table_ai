import streamlit as st

st.set_page_config(page_title="Basic SARAL Math")

st.title("🧮 Kids Basic Maths App")
number = st.number_input("Enter the number", min_value=1, step=1)
# ------------------------
# Sidebar
# ----------------------#
Mode = st.sidebar.selectbox(
    "Select Mode",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)
st.write("Selected mode =", Mode)

start=1
end=10

for i in range(start, end + 1):

    # default operands
    left = number
    right = i

    if Mode == "Multiplication":
        correct = left * right
        symbol = "×"

    elif Mode == "Addition":
        correct = left + right
        symbol = "+"

    elif Mode == "Subtraction":
        # always bigger minus smaller
        left = max(number, i)
        right = min(number, i)
        correct = left - right
        symbol = "-"

    elif Mode == "Division":
        # do not show when divisor is greater than numerator
        if i > number:
            continue
        correct = round(number / i, 2)
        symbol = "÷"

    user_ans = st.text_input(
        f"{left} {symbol} {right} = ?",
        key=f"{Mode}_{i}"
    )

    if st.button("Check", key=f"check_{Mode}_{i}"):

        try:
            if abs(float(user_ans) - float(correct)) < 0.01:
                st.success("Correct ✅")
            else:
                st.error(f"Wrong ❌  Correct answer is {correct}")
        except:
            st.warning("Please enter a valid number")



