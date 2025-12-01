import streamlit as st
import random



# 가위,바위,보를 낼수있는 창을 만든다
choose = st.radio("당신의 선택은?",["가위","바위","보"])

if st.button("결과확인"):

    st.write(f"당신은 {choose}를 골랐다")
    컴 = random.choice(["가위","바위","보"])
    st.write(f"컴퓨터는 {컴}를 골랐다")

    # 누가 이겼는지 판정한다
    if choose == '가위' and 컴 == "보":
        st.write("내가 이겼다!")

    elif choose == '보' and 컴 == '가위':
        st.write("내가 졌다")

    elif choose == '바위' and 컴 == '보':
        st.write("내가 졌다")

    elif choose == '바위' and 컴 == '가위':
        st.write("내가 이겼다!")

    elif choose == '가위' and 컴 == '보':
        st.write("내가 이겼다!")

    elif choose == '보' and 컴 == '바위':
        st.write("내가 이겼다!")


    elif choose == '가위' and 컴 == '바위':
        st.write("내가 졌다")

    else:
        st.write("비겼다")