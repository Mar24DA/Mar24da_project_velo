import streamlit as st
import utils.velo_load_datas as datas

def page_config(title):
    st.set_page_config(
    page_title=title,
    page_icon="🚴‍♀️",
    layout="wide"
)

def page_css():
        st.markdown(
            f'''
            <style>
                h1 {{
                  color: #001219;
                }}
                div.block-container {{
                    padding-top: 25px;
                }}
            </style>
            ''',
            unsafe_allow_html=True,
        )

def load_velo():
    df_velo = datas.load_velo()
    st.session_state.df_velo = df_velo

def menu():
  with st.sidebar:
      st.image('assets/logo-velo2.png', caption='Lena GUILLOUX, Mélissa CHEMMAMA, Myriam MAHDJOUB, Eléonore HERMAND')
      st.page_link('streamlit_velo.py', label="Introduction", icon="🏠")
      st.page_link('pages/1_exploration.py', label="Exploration des données", icon="📑")
      st.page_link('pages/2_dataviz.py', label="Data Visualisation", icon="📈")
      st.page_link('pages/3_modelisation.py', label="Modélisation", icon="🤖")
      st.page_link('pages/4_predictions.py', label="Prédictions", icon="🗓️")
      st.page_link('pages/5_conclusion.py', label="Conclusion", icon="📌")