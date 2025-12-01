import streamlit as st
st.write("내가 제일좋아하는 음식은?")
st.title("퀴즈 맞추기")
코드 = '''
정답 = "망고"
while True:
    대답 = input("정답을 써줘")
    if 정답 == 대답:
        break'''
st.code(코드)