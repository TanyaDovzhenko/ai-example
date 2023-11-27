import ai
import streamlit as st

title = 'ABB PoC Project'

def on_click(query_str):
  st.session_state.respText = ai.sendAiRequest(query_str)

if 'respText' not in st.session_state:
  st.session_state.respText = ''
    
st.set_page_config(page_title=title)
st.header(title)
inputText = st.text_area("Please enter your question")
st.button("Send", type="primary", on_click=on_click(inputText), use_container_width=True)
st.markdown(st.session_state.respText)

