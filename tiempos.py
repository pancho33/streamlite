import streamlit as st
import time
from datetime import datetime

ahora = datetime.now()
print(ahora)
now = ahora.strftime("%H:%M:%S") # HH:MM:SS


st.write("# La fecha y hora actual es", ahora)
st.markdown(f'<h1 style="color:#1C17E6;font-size:32px;">{"ColorMeBlue text"}</h1>', unsafe_allow_html=True)

def header(url):
     st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

st.markdown("-----------")
header('Hora ' + now)