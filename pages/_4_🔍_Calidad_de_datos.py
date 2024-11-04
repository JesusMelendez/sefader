import pandas as pd
import numpy 
# from ydata_profiling import ProfileReport
import streamlit as st

# from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout="wide",page_icon=f'🌽')

logo = './src/img/sefader_logo.png'
# cimmyt = './src/img/cimmyt_new.png'
cl,cl1,cl3,cl4 = st.columns(4)
cl.image(logo)
cimmyt_logo = "./src/img/cimmyt.png"
cl4.image(cimmyt_logo)
st.write('Sitio en construcción :gear:')
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
  
    </style>
""", unsafe_allow_html=True)