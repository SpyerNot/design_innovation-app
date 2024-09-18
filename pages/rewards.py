import streamlit as st
st.title("REWARDS!!")
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Food voucher")
    st.image("https://d1csarkz8obe9u.cloudfront.net/posterpreviews/breakfast-food-voucher-design-template-22ff8b1bc7e11ecad0fbab76ced8bceb_screen.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
