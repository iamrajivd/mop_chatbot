import os
import openai
import streamlit as st  # ✅ required for secrets

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_mop(node, action, feature):
    full_text = ""

    # Folder check
    if not os.path.exists("docs"):
        return "❗️'docs' folder not found. Please upload CLI guide."

    files = os.listdir("docs")
    if not files:
        return "⚠️ No CLI guide uploaded. Please upload a .pdf or .txt file."

    for fname in files:
        path = os.path.join("docs", fname)
        if fname.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                full_text += f.read()
        elif fname.endswith(".pdf"):
            from chatbot.document_parser import extract_text_from_pdf
            full_text += extract_text_from_pdf(path)

    if not full_text.strip():
        return "📄 Uploaded file is empty or unreadable."

    # Prompt and OpenAI logic
    ...
