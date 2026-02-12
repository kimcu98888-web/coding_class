import streamlit as st
st.subheader("버튼")
클릭 = st.button("이걸 눌러봐")
st.write(클릭)
if 클릭 == True:
    st.balloons()
st.divider()
st.subheader("페이지 링크")
st.page_link("http://www.google.com", label="Google", icon="🌎")
st.divider()
st.subheader("체크박스")
a = st.checkbox("동의하십니까?")
if a == True:
    st.write("당신의 기기는 점령당했습니다")
st.divider()
st.subheader("설렉트 박스")
choose = st.selectbox("골라봐",[1,2,3,4])
st.write("You selected:", choose)