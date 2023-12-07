import ai
import streamlit as st
from PIL import Image

title = 'Minespider - Powered ABB Demo AI Chatbot'
image = Image.open('src/img/motor.png')
st.set_page_config(page_title=title, page_icon=image, layout="centered", initial_sidebar_state="auto", menu_items=None)

st.header(title)
st.write("Revolutionising Electric Motors: Empowering Efficiency, "
        "Enhancing Aftermarket Service, and Ensuring Compliance")
st.write("The AI chatbot demo was built using publicly available "
          "ABB materials for electrical machine types, in both motor "
          "and generator operations as follows:")

col1, col2 = st.columns(2)
with col1:
  st.image(image, width=300)
with col2:
  st.write("- Low voltage motors installation, operation, maintenance and safety manual (2022)")
  st.write("- Low voltage motors motor guide (2019)")
  st.write("- End-of-life instructions for low voltage motors (2023)")
  st.write("- Environmental Product Declaration for Synchronous reluctance (incl. increased safety) motors (55 kW-315 kW) (2023)")

def on_click(query_str):
  st.session_state.respText = ai.sendAiRequest(query_str)

if 'respText' not in st.session_state:
  st.session_state.respText = ''
 
st.write("Ask your question now and experience the power of enhanced interaction! " 
         "Discover how our Minespider-powered ABB Demo AI Chatbot can elevate your " 
         "electric motor interaction and provide instant troubleshooting and support "
         "as just one of the aspects that can be covered.")   

inputText = st.text_area("Please enter your question")
st.button("Send", type="primary", on_click=on_click(inputText), use_container_width=True)
st.markdown(st.session_state.respText)