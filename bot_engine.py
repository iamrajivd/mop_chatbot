from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_mop(node, action, feature, full_text=""):
    prompt = f"""Generate a Method of Procedure (MoP) for:
Node: {node}
Action: {action}
Feature: {feature}

Reference CLI content:
{full_text[:6000]}

Include:
- Objective
- Pre-checks
- Step-by-step commands
- Rollback steps
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ✅ Switch from "gpt-4"
        messages=[
            {"role": "system", "content": "You are a telecom engineer writing professional MoPs."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1500
    )

    return response.choices[0].message.content
