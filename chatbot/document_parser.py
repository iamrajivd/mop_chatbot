import os
import pdfplumber

def extract_text_from_pdf(pdf_path):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    return full_text

def extract_text_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        return f.read()

def upload_and_process_docs(files):
    os.makedirs("docs", exist_ok=True)
    for file in files:
        file_path = os.path.join("docs", file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
