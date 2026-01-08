import os
import requests
import streamlit as st

API_GATEWAY_URL = os.getenv("API_GATEWAY_URL", "http://api-gateway:8000")

st.set_page_config(page_title="Pizza Chat", page_icon="🍕")
st.title("🍕 Pizza LLM Chat (Streamlit)")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.markdown("### Config")
    api_url = st.text_input("API Gateway URL", API_GATEWAY_URL)
    st.caption("Ex.: http://localhost:8000 (host) ou http://api-gateway:8000 (compose)")

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

prompt = st.chat_input("Digite seu pedido…")

def call_chat(message: str) -> str:
    # ajuste o endpoint conforme seu api-gateway
    # tentativas: /chat ou /api/chat etc.
    for path in ("/chat", "/api/chat"):
        try:
            r = requests.post(f"{api_url}{path}", json={"message": message}, timeout=30)
            if r.status_code == 200:
                data = r.json()
                # tente padrões comuns
                return data.get("reply") or data.get("answer") or data.get("message") or str(data)
        except Exception:
            pass
    return "Falha ao chamar o API Gateway. Verifique URL/endpoint e logs."

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            reply = call_chat(prompt)
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
