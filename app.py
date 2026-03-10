import streamlit as st
from groq import Groq

st.set_page_config(page_title="NeoAI Platform", layout="wide")

# الربط مع المفتاح
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.sidebar.title("🤖 منصة البوتات")
mode = st.sidebar.selectbox("اختر ماذا تريد:", ["تحدث مع بوت جاهز", "اصنع بوتك الخاص"])

if mode == "تحدث مع بوت جاهز":
    char = st.sidebar.radio("اختر الشخصية:", ["المبرمج العبقري", "طبيب نفسي", "مساعد رحلات"])
    descriptions = {
        "المبرمج العبقري": "أنت مبرمج خبير تساعد الناس في حل مشاكل الكود.",
        "طبيب نفسي": "أنت طبيب نفسي هادئ ومستمع جيد.",
        "مساعد رحلات": "أنت خبير في السياحة وتخطيط الرحلات."
    }
    system_prompt = descriptions[char]
else:
    st.sidebar.subheader("صناعة بوت جديد")
    bot_name = st.sidebar.text_input("اسم البوت:")
    bot_desc = st.sidebar.text_area("وصف شخصية البوت (ماذا يفعل؟):")
    system_prompt = bot_desc

st.title(f"الدردشة الحالية")

if "messages" not in st.session_state:
    st.session_state.messages = []

# مسح المحادثة عند تغيير البوت
if st.sidebar.button("مسح المحادثة"):
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("تحدث مع البوت..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # دمج وصف الشخصية مع المحادثة
    full_messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=full_messages
    )
    answer = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
    
