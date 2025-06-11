from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a telecom engineer writing MoPs."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
    max_tokens=1500
)
