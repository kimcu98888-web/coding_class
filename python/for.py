import streamlit as st

가방=st.multiselect("가방에 챙길것을 챙기세요",
             ["물","기린","코코넛","수박"]  
)
st.write("for는 가방안에 있는것을 하나하나 보여줌니다")

클릭=st.button("이 버튼을 눌러서 for를 실행시켜 보세요")

if 클릭:
    for 물건 in 가방:
        st.write(물건)