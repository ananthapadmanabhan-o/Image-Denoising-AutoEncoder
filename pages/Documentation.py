import streamlit as st

st.set_page_config(
    page_title="Documentation",
    page_icon="📄",
)

st.header('Welcome to Documentation! 👋', divider='rainbow')
st.sidebar.success("Select a demo above.")

with open('README.md','r') as f:
    body = f.read()

st.markdown(body)