import streamlit as st
from groq import Groq

st.set_page_config(page_title="NeoAI Chat", layout="centered")
st.title("🤖 NeoAI: المحرك العالمي")

# الربط مع المفتاح السري
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("المفتاح السري GROQ_API_KEY مفقود!")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("تحدث معي..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=st.session_state.messages
    )
    answer = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
  
