import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Lucky Draw", layout="wide")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0;}
    iframe {display: block;}
    </style>
    """, unsafe_allow_html=True)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # 높이를 2500px로 넉넉하게 설정하여 엽서 리스트가 잘리지 않게 함
    components.html(html_content, height=2500, scrolling=True)
except Exception as e:
    st.error(f"에러 발생: {e}")
