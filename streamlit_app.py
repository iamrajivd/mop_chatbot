
import streamlit as st
from chatbot.bot_engine import generate_mop
from chatbot.document_parser import upload_and_process_docs

st.title("📄 Nokia CMM MoP Generator")

uploaded_files = st.file_uploader("Upload CLI/Product Guides", type=['pdf', 'txt'], accept_multiple_files=True)
if uploaded_files:
    upload_and_process_docs(uploaded_files)
    st.success("Documents processed and indexed!")

st.subheader("Create MoP")
node = st.text_input("Node Name")
action = st.text_input("Action Type (e.g., SRVCC enable)")
feature = st.text_input("Feature/Service (Optional)")

if st.button("Generate MoP"):
    mop_text = generate_mop(node, action, feature)
    with open(f"output/{node}_{action}.txt", "w") as f:
        f.write(mop_text)
    st.download_button("Download MoP", mop_text, file_name=f"{node}_{action}.txt")
