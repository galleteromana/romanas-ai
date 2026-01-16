import streamlit as st
import logic

st.set_page_config(page_title="Romana's AI ૮꒰˶• ༝ •˶꒱ა ", page_icon="૮꒰˶ᵔ ᵕ ᵔ˶꒱ა")

st.title("Romana's AI Assistant ૮꒰˶• ༝ •˶꒱ა")
st.caption("I can do math or chat with you!")

if not logic.HF_TOKEN:
    st.error("Error: HF_TOKEN not found in environment.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("૮꒰っ˕ -｡꒱১ Thinking..."):
            if logic.is_math_question(prompt):
                response_text = logic.calculate(prompt)
                display_text = f"૮꒰˶ᵔ ᵕ ᵔ˶꒱ა **Math detected!**\n\nThe result is {response_text}."
            else:
                display_text = logic.get_ai_response(prompt)
            
            st.markdown(display_text)
            
    st.session_state.messages.append({"role": "assistant", "content": display_text})