import streamlit as st

st.set_page_config(
    page_title="DeepSeek-R1 Chatbot",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 DeepSeek-R1 Chatbot")

# Ollama API 설정
OLLAMA_BASE_URL = "http://localhost:11434"
DEEPSEEK_MODEL = "deepseek-r1:8b"