import streamlit as st
st.write("how to make title")
st.title("this is a title,h1")
st.header("this is a header,h2")
st.subheader("this is a subheader,h3")
st.divider()
st.write("this is a code")
mycode = """
a,b=4,7
print(a+b)
"""
st.code(mycode)
st.divider()
st.latex(r"원의 넓이= \pi r^2")
st.latex(r"구의 걷넓이=4 \pi r^2")
st.latex(r"구의 부피=\frac{4}{3} \pi r^3")