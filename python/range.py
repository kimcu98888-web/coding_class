import streamlit as st

st.write("range는 가방에 숫자를 빠르게 넣을수 있다")

가방=st.multiselect("가방에 챙길것을 챙기세요",
             [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  
)
클릭=st.button("이 버튼을 눌러서 가방을 확인 해보자 ")

if 클릭:
    for 물건 in 가방:
        st.write(물건)


first=int(st.number_input("처음 수를 써주세요"))
last=int(st.number_input("마지막 수를 써주세요"))
간격=int(st.number_input("간격을 써주세요"))

가방2 = range(first,last+1,간격)
클릭2=st.button("이 버튼을 눌러서 가방2를 확인 해보자")

if 클릭2:
    for 물건 in 가방2:
        st.write(물건)
    