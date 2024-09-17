import streamlit as st
from page_functions import page1
st.page_link("homepage.py", label="Home", icon="🏠")
st.page_link("pages/survey.py", label="Survey", icon="1️⃣")
st.page_link("pages/rewards.py", label="Rewards", icon="2️⃣")
st.page_link("pages/game.py",label="Games")
pg = st.navigation([st.Page(page1), st.Page("page2.py")])
pg.run()
