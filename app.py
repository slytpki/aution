import streamlit as st

# --- 隱藏 Streamlit 預設物件的 CSS ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display:none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ---主程式 ---
st.title("我的法務部士林分署拍賣")
# ...
