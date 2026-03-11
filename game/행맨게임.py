
import streamlit as st
import random
import wordfreq

st.title("Hangman")

# 세션 초기화
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.word = ""
    st.session_state.ans = []
    st.session_state.hp = 10
    st.session_state.guessed = []


def start_game(d):
    words = wordfreq.top_n_list("en", 100000)

    if d == 1:
        pool = words[0:10]
    elif d == 2:
        pool = words[10:100]
    elif d == 3:
        pool = words[100:1000]
    elif d == 4:
        pool = words[1000:10000]
    else:
        pool = words[10000:100000]

    word = random.choice(pool)

    st.session_state.word = word
    st.session_state.ans = ["_"] * len(word)
    st.session_state.hp = 10
    st.session_state.guessed = []
    st.session_state.started = True

    st.chat_message("assistant").write(f"게임 시작! 길이 {len(word)} 글자")
    st.chat_message("assistant").write(" ".join(st.session_state.ans))
    st.chat_message("assistant").write(f"hp = {st.session_state.hp}")


# 게임 시작 전
if not st.session_state.started:
    st.chat_message("assistant").write("난이도 1~5 중 하나를 입력하세요.")


msg = st.chat_input("입력")

if msg:

    st.chat_message("user").write(msg)

    # 게임 시작 전 → 난이도 입력
    if not st.session_state.started:

        try:
            d = int(msg)

            if 1 <= d <= 5:
                start_game(d)
            else:
                st.chat_message("assistant").write("1~5 사이 숫자를 입력하세요.")

        except:
            st.chat_message("assistant").write("숫자를 입력하세요.")

    # 게임 진행
    else:

        word = st.session_state.word
        ans = st.session_state.ans
        hp = st.session_state.hp
        guessed = st.session_state.guessed

        alphabet = msg.lower()

        if alphabet in guessed:
            st.chat_message("assistant").write("이미 입력한 글자입니다.")
            st.chat_message("assistant").write(f"입력한 글자: {', '.join(guessed)}")

        else:
            guessed.append(alphabet)

            if alphabet in word:
                st.chat_message("assistant").write("있음")

                for i in range(len(word)):
                    if word[i] == alphabet:
                        ans[i] = alphabet

            else:
                st.chat_message("assistant").write("없음")
                hp -= 1

        st.session_state.hp = hp
        st.session_state.ans = ans
        st.session_state.guessed = guessed

        st.chat_message("assistant").write(" ".join(ans))
        st.chat_message("assistant").write(f"입력한 글자: {', '.join(guessed)}")
        st.chat_message("assistant").write(f"hp = {hp}")

        if hp == 0:
            st.chat_message("assistant").write(f"실패! 정답: {word}")
            st.session_state.started = False

        elif "_" not in ans:
            st.chat_message("assistant").write("단어 완성! 🎉")
            st.session_state.started = False