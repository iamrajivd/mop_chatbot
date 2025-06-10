import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_mop(node, action, feature):
    full_text = ""

    if not os.path.exists("docs"):
        return "📁 'docs/' folder not found. Please upload at least one CLI guide."

    files = os.listdir("docs")
    if not files:
        return "📂 No files uploaded. Please upload PDF or TXT files to 'docs/' first."

    for fname in files:
        path = os.path.join("docs", fname)
        if fname.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                full_text += f.read()
        elif fname.endswith(".pdf"):
            from chatbot.document_parser import extract_text_from_pdf
            full_text += extract_text_from_pdf(path)

    prompt = f"""Generate a Method of Procedure (MoP) for:
Node: {node}
Action: {action}
Feature: {feature}

Use the following CLI content:
{full_text[:6000]}

Include:
- Objective
- Pre-checks
- Step-by-step commands
- Rollback steps
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a telecom engineer writing professional MoPs."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1500
    )

    return response.choices[0].message.content
