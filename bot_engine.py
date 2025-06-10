from chatbot.bot_engine import generate_mop

from chatbot.document_parser import extract_text_from_pdf, extract_text_from_txt

def generate_mop(node, action, feature):
    full_text = ""
    for fname in os.listdir("docs"):
        path = os.path.join("docs", fname)
        if fname.endswith(".pdf"):
            full_text += extract_text_from_pdf(path)
        elif fname.endswith(".txt"):
            full_text += extract_text_from_txt(path)
    # build prompt and send to GPT...

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_mop(node, action, feature, full_text):
    prompt = f"""Generate a Method of Procedure (MoP) for:
- Node: {node}
- Action: {action}
- Feature: {feature}

Refer to the CLI content:
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
            {"role": "system", "content": "You are a telecom engineer writing MoPs for Nokia CMM."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1500
    )

    return response.choices[0].message.content
