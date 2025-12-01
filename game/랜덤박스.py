import streamlit as st
import random
# 3가지 선택지
# 그중 1 선물 나머지 꽝

#순서
# 버튼 누르면 게임 시작,선택지 3개와 확인 버튼 1개가 만들어짐
# 선택지를 고르고 확인버튼 누르면 결과가 나온다
st.title("랜덤 상자")
choose = st.radio("당신의 선택은?",["1번 상자","2번 상자","3번 상자"])
if st.button("결과확인"):
    당첨 = random.choice(["1번 상자","2번 상자","3번 상자"])
    st.write(당첨)
    if 당첨 == choose:
        st.balloons()
        st.success("축카합니다")
    else:
        st.snow()
        st.error("실패입니다")