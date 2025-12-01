import streamlit as st
st.subheader("비디오 만들기")
pop = "https://www.youtube.com/watch?v=eny0BqmSwmM&list=RDeny0BqmSwmM&start_radio=1"
st.video(pop)

st.subheader("이미지")
image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3R6oPvpwWp2GSQ2vYPimEt8tJKWg3jmZjrw&s"
st.image(image,caption="soda pop")

st.subheader("오디오")
audio = "https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg"
st.audio(audio)