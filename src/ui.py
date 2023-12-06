import ai
import streamlit as st
from PIL import Image

title = 'ABB PoC Project'
image = Image.open('src/img/motors.png')
st.set_page_config(page_title=title, page_icon=image, layout="centered", initial_sidebar_state="auto", menu_items=None)

col1, col2 = st.columns(2)
with col1:
  st.image(image, width=320)
with col2:
   st.write("These information is valid for the following "
            "ABB electrical machine types, in both motor "
            "and generator operation: \n"
            "- series MT*, MXMA, \n"
            "- series M1A*, M2A*/M3A*, M2B*/M3B*, M4B*, \n"
            "M2C*/M3C*, M2F*/M3F*, M2L*/M3L*, M2M*/ \n"
            "M3M*, M2Q*, M2R*/M3R*, M2V*/M3V* \n"
            "- in IEC frame sizes 56-500 \n"
            "- in NEMA frame sizes 58*, 50** \n"
          )

def on_click(query_str):
  st.session_state.respText = ai.sendAiRequest(query_str)

if 'respText' not in st.session_state:
  st.session_state.respText = ''
    
inputText = st.text_area("Please enter your question")
st.button("Send", type="primary", on_click=on_click(inputText), use_container_width=True)
st.markdown(st.session_state.respText)