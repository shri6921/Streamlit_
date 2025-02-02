import streamlit as st

# Set page title
st.set_page_config(page_title="Simple Streamlit App")

# Title of the app
st.title("Welcome to My Streamlit App")

# Add a slider
number = st.slider("Select a number", 1, 100)

# Display the selected number
st.write(f"You selected: {number}")

# Add a text input box
name = st.text_input("What's your name?")

# Display a personalized greeting
if name:
    st.write(f"Hello, {name}! 👋")
