import streamlit as st

pages={
    "about me":[
        st.Page("about me/Me.py",title="자기소개"),
    ],
    "python":[
        st.Page("python/print와_input.py",title="print와_input"),
        st.Page("python/if.py",title="if"),
        st.Page("python/for.py",title="for"),
        st.Page("python/range.py",title="range"),
        st.Page("python/while.py",title="while"),
        st.Page("python/함수와_예외처리.py",title="함수와_예외처리"),
    ],
    "game":[
        st.Page("game/가위바위보.py",title="가위바위보"),
        st.Page("game/랜덤박스.py",title="랜덤박스"),
    ],
     "스트림릿실습":[
        st.Page("스트림릿실습/미디어.py",title="미디어"),
        st.Page("스트림릿실습/text.py",title="text"),
    ],   
    "선생님_팁":[
        st.Page("선생님_팁/게임은_나쁜건가.py",title="게임은_나쁜건가.py"),
    ],   
}
pg=st.navigation(pages)
pg.run()