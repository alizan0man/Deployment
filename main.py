import streamlit as st 

st.title("Simple Streamlit App")

user_input = st.text_input("Enter Some Text:")

if st.button("Show Text"):
    st.write(f"You Entered: {user_input}")
