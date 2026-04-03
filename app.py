import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 기본 설정
st.set_page_config(page_title="Lucky Draw", layout="wide")

# 2. 스트림릿 상단/하단 메뉴 숨기기 및 여백 제거
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    /* 스트림릿 기본 패딩 제거 */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    /* 스크롤바 숨기기 (필요시) */
    ::-webkit-scrollbar {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. index.html 파일을 읽어서 화면에 띄우기
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # [핵심 수정] 높이를 2500px 정도로 매우 넉넉하게 잡으세요.
    # scrolling=True를 넣으면 내용이 길어질 때 내부 스크롤이 생깁니다.
    components.html(html_content, height=2500, scrolling=True)
    
except Exception as e:
    st.error(f"에러 발생: {e}. index.html 파일이 같은 폴더에 있는지 확인하세요.")
