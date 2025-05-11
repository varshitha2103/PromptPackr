import streamlit as st
from ollama_query import compress_chat

st.set_page_config(page_title="🧠 Prompt Memory Compressor", layout="centered")

st.title("🧠 PromptPackr - Prompt Memory Compression Engine")
st.markdown("Upload chat logs and generate compressed memory")

uploaded_file = st.file_uploader("📤 Upload a .txt chat file", type=["txt"])

if uploaded_file:
    chat_text = uploaded_file.read().decode("utf-8")

    with st.spinner("Running locally via Ollama..."):
        result = compress_chat(chat_text)

    st.subheader("🔹 Compressed Summary")
    st.text(result["summary"])

    st.subheader("🧾 Key Instructions")
    st.text(result["instructions"])

    st.subheader("🎭 Tone & Style")
    st.markdown(f"> {result['tone']}")
