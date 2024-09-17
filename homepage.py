import streamlit as st
st.header("Our Health App!!")
know_more = st.columns(1,vertical_alignment="top")
with know_more:
  st.header("Getting to know more about our app!!")
st.page_link("homepage.py", label="Home", icon="🏠")
st.page_link("pages/survey.py", label="Survey", icon="1️⃣")
st.page_link("pages/rewards.py", label="Rewards", icon="2️⃣")
st.page_link("pages/game.py",label="Games")

