import streamlit as st
색깔 = st.radio(
    "좋아하는 색깔은?",
    ["black","pink","orange"]
)

if 색깔=="black":
    st.write("black")
if 색깔=="pink":
    st.write("pink")
if 색깔=="orange":
    st.write("orange")                                              

효과 = st.text_input("원하는 효과는?")
if 효과 == "snow":
    st.snow()
elif 효과 == "balloons":
    st.balloons()
else :
    st.error("없는 명령어 입니다." ,icon="🚨")