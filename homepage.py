import streamlit as st
st.header("Our Health App!!")
st.page_link("homepage.py", label="Home", icon="🏠")
st.page_link("pages/survey.py", label="Survey (Must do first)", icon="1️⃣")
st.page_link("pages/rewards.py", label="Rewards", icon="2️⃣")
st.page_link("pages/game.py",label="Games")
st.divider()
st.subheader("Know more about us")

