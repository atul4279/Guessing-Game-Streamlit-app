import streamlit as st
import random

st.title("🎯 Guess the Number")

# Initialize session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = 50
    st.session_state.guesses = []
    st.session_state.feedback = ""

# User input
guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    num = st.session_state.secret_number
    st.session_state.guesses.append(guess)

    # Correct guess
    if guess == num:
        st.session_state.feedback = f"🎉 Congratulations! You guessed the number correctly in {len(st.session_state.guesses)} attempts."
    
    # First guess
    elif len(st.session_state.guesses) == 1:
        if abs(guess - num) <= 10:
            st.session_state.feedback = "Warm ❤️‍🔥"
        else:
            st.session_state.feedback = "Cold ❄️"
    
    # Second guess onward
    else:
        prev_guess = st.session_state.guesses[-2]
        if abs(guess - num) < abs(prev_guess - num):
            st.session_state.feedback = "Warmer 🔥"
        else:
            st.session_state.feedback = "Colder 🥶"

# Show feedback
st.write(st.session_state.feedback)

# Restart button
if st.button("Restart Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.guesses = []
    st.session_state.feedback = ""
    st.experimental_rerun()