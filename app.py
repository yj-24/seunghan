import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 기본 설정
st.set_page_config(page_title="Lucky Draw", layout="wide")

# 2. 스트림릿 상단/하단 메뉴 숨기기 (아이패드 풀스크린용)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0;}
    iframe {display: block;}
    </style>
    """, unsafe_allow_html=True)

# 3. index.html 파일을 읽어서 화면에 띄우기
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # 아이패드 해상도에 맞춰 높이 조절 (보통 1000~1200px)
    components.html(html_content, height=1200)
except Exception as e:
    st.error(f"에러 발생: {e}. index.html 파일이 같은 폴더에 있는지 확인하세요.")
