import streamlit as st
from groq import Groq

# إعدادات الواجهة
st.set_page_config(page_title="NeoAI العالمي", layout="centered")

# تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 محرك NeoAI العالمي")

# إحضار المفتاح السري من الإعدادات
try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
except:
    st.error("يرجى إضافة GROQ_API_KEY في إعدادات Secrets")
    st.stop()

# نظام الدردشة
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("تحدث معي بأي لغة..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=st.session_state.messages
        )
        answer = response.choices[0].message.content
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
