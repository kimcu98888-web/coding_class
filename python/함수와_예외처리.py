import streamlit as st
st.title("함수")
if "동물리스트" not in st.session_state:
    st.session_state.동물리스트 = []
강아지링크 = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Golde33443.jpg/330px-Golde33443.jpg"
고양이링크 = "https://i.namu.wiki/i/d1A_wD4kuLHmOOFqJdVlOXVt1TWA9NfNt_HA0CS0Y_N0zayUAX8olMuv7odG2FiDLDQZIRBqbPQwBSArXfEJlQ.webp"


def 멍멍이():
    st.session_state.동물리스트.append(강아지링크)
def 고양이():
    st.session_state.동물리스트.append(고양이링크)



if st.button("강아지 불러오기"):
    멍멍이()
if st.button("고양이 불러오기"):
    고양이()

# print(st.session_state.동물리스트)
for 링크 in st.session_state.동물리스트:
    st.image(링크)

st.divider()
st.title("예외처리")
st.subheader("에러의 종류")
if st.button("ZeroDivisionError"):
    st.write("코드에서는 0으로 나눌수 없다")
    st.code("10/0")

if st.button("IndexError"):
    st.write("리스트나 문자열 등애서 없는순서를 불렀을떄 생긴다")
    st.code("""a=[10,20,30]
print(a[100])""")

if st.button("IndentationError"):
    st.write("들여쓰기를 하지 않을 경우나 이상하게 들여쓰기를 해도 나타난다")
    st.code("""a = int(input())
if a>1:
  print(123456789)
else:
print(-1)""")

if st.button("TypeError"):
    st.write("""어올리지 않는 재료끼리 섞으려고 할때 발생

            예1 숫자와 문자를 더할때
            예2 문자열과 숫자를 비교할때""")
    st.code("""print("a"+1)
5 < "10" """)

if st.button("SyntaxError"):
    st.write("문법이 틀릴때 나옴")
    st.code('''print("hi"''')
    st.code('''a = int(input())
if a>1
  print(123456789)
else:
  print(-1)''')

st.divider()
st.subheader("try를 쓰면 에러를 무시할수 있다")
st.code('''try:
  print("a"+132)
except:
  print("틀린 코드")''')