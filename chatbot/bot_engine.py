import os
import openai
from chatbot.document_parser import extract_text_from_pdf

# Ensure your OpenAI key is set as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_mop(node, action, feature):
    # Combine all uploaded PDF docs
    full_text = ""
    for fname in os.listdir("docs"):
        if fname.endswith(".pdf"):
            full_text += extract_text_from_pdf(os.path.join("docs", fname))

    # Construct GPT prompt
    prompt = f"""You are a Nokia CMM expert. Use the below CLI/documentation content to write a professional Method of Procedure in .txt format.

Documents:
{full_text[:6000]}

Task:
Generate a MoP for the following:
- Node: {node}
- Action: {action}
- Feature: {feature}

Include:
- Objective
- Pre-checks
- Step-by-step commands
- Rollback steps
- Reference section (if available)
"""

    # GPT Completion
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if needed
        messages=[
            {"role": "system", "content": "You are a professional telecom engineer writing Methods of Procedure."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1500
    )

    return response['choices'][0]['message']['content']
