import streamlit as st

if st.button("print"):
    st.write("print는 내가 쓴 말을 대신 말해주는 거야")
    st.code("""print("hi")""")

if st.button("input"):
    st.write("input은 내가 입력하는걸 받는거야 ")
    st.code("""이름 = input("이름을 말해주세요"):""")