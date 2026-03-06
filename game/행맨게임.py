import streamlit as st
import random
import wordfreq

st.title("Hangman")

# 세션 초기화
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.logs = []

# 난이도 선택
if not st.session_state.started:
    d = st.number_input("난이도 1~5 선택", min_value=1, max_value=5, step=1)

    if st.button("게임 시작"):
        단어장 = wordfreq.top_n_list("en",100000)

        if d == 1:
            단어범위 = 단어장[0:10]
        elif d == 2:
            단어범위 = 단어장[10:100]
        elif d == 3:
            단어범위 = 단어장[100:1000]
        elif d == 4:
            단어범위 = 단어장[1000:10000]
        else:
            단어범위 = 단어장[10000:100000]

        st.session_state.word = random.choice(단어범위)
        st.session_state.ans = list("_" * len(st.session_state.word))
        st.session_state.hp = 10
        st.session_state.started = True

        st.session_state.logs.append(f"난이도 1~5 선택 {d}")
        st.session_state.logs.append(" ".join(st.session_state.ans))
        st.session_state.logs.append(f"hp = {st.session_state.hp}")

# 게임 진행
if st.session_state.started:

    alphabet = st.text_input("글자 입력")

    if st.button("입력"):
        word = st.session_state.word
        ans = st.session_state.ans
        hp = st.session_state.hp

        st.session_state.logs.append(f"글자 입력: {alphabet}")

        if alphabet in word:
            st.session_state.logs.append("있음")
            for i in range(len(word)):
                if word[i] == alphabet:
                    ans[i] = alphabet
        else:
            st.session_state.logs.append("없음")
            hp -= 1

        st.session_state.hp = hp
        st.session_state.ans = ans

        st.session_state.logs.append(" ".join(ans))
        st.session_state.logs.append(f"hp = {hp}")

        if hp == 0:
            st.session_state.logs.append(word)
            st.session_state.logs.append("실패!")
            st.session_state.started = False

        if "_" not in ans:
            st.session_state.logs.append("단어 완성!")
            st.session_state.started = False

# 로그 출력
for log in st.session_state.logs:
    st.write(log)