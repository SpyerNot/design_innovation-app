import streamlit as st
st.header("Our Health App!!")
st.columns(1,vertical_alignment="top")
st.page_link("homepage.py", label="Home", icon="🏠")
st.page_link("pages/survey.py", label="Survey", icon="1️⃣")
st.page_link("pages/rewards.py", label="Rewards", icon="2️⃣")
st.page_link("pages/game.py",label="Games")

