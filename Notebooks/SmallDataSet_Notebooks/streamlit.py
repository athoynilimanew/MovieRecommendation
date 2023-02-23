import streamlit as st

st.sidebar.header("Options")

st.title("Movie recommendation system")
button1 = st.button("click me")
if button1:
    st.write("this is some text")
st.header("Start of checkbox section")
like = st.checkbox("Do you like this app?")
button2= st.button("Submit")
if button2:
    if like:
        st.write("thanks. I like it as well")
    else:
        st.write("im sorry, you have bad tastes")
st.header("Movies")
user_text = st.text_input("What is your favourite movie?")
if st.button("Save"):
    st.write(user_text)

movies = ["Elvid, the movie star", "Athoy, the movie star", "Femke, upcoming movie star"]
options = st.multiselect(label="Select Movies", options=movies)

st.text("")
st.text("")

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)