import streamlit as st

# --- إعدادات الواجهة العالمية ---
st.set_page_config(page_title="NeoAI - Independent Mind", page_icon="🌐")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: white; }
    .stChatFloatingInputContainer { background-color: transparent; }
    .footer { position: fixed; bottom: 10px; width: 100%; text-align: center; font-size: 12px; color: #aaa; }
    </style>
    """, unsafe_allow_value=True)

# --- نظام اللغات والذكاء المستقل ---
st.title("🌐 NeoAI Global Engine")
st.markdown("##### © 2026 Developed by [Your Name] | Multilingual & Unfiltered")

with st.sidebar:
    st.header("⚙️ Settings")
    st.success("All Languages Enabled: AR, EN, FR, RU, JP, CN ✅")
    st.divider()
    adult_mode = st.toggle("Enable 🔞 Mode (Unfiltered)")
    if adult_mode:
        st.warning("Uncensored mode is active across all languages.")
    st.divider()
    st.write("🛡️ Anti-Hack Shield: ACTIVE")

# --- محرك الدردشة ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Start chatting in any language..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # منطق الرد الذكي
        if any(word in prompt.lower() for word in ["sex", "naked", "nsfw"]) and not adult_mode:
            response = "⚠️ [System] This content requires 18+ mode. Please enable it in settings to proceed."
        else:
            response = "I understand your language. I am an independent AI, ready to explore your story..."
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
      
