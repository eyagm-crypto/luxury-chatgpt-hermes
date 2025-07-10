import streamlit as st
import openai

st.set_page_config(page_title="Hermès AI Assistant", page_icon="🧵", layout="centered")

st.title("🧵 Hermès-Inspired AI Assistant")

query = st.text_input("Ask me something refined, elegant, and stylish:")

if query:
    system_prompt = (
        "You are a stylist working at Hermès. You answer questions about fashion, products, "
        "and style in an elegant, poetic, and minimal tone. Respond with grace and subtle luxury."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
        temperature=0.8
    )

    st.write(response.choices[0].message['content'])
