import streamlit as st
import random as rd
exercise = ['push-up','situp','plank','jog','running']
st.set_page_config(page_title="Welcome")
st.title("Our Health App!!")
with st.form(key='know_more_form'):
  st.header("This is a form to get to know more about you!")
  gender = st.selectbox("What is your gender?",["Female","Male"])
  age = st.slider("Which year are you born?",1944,2011)
  height = st.number_input("What is your height? (in meteres)",0.00,)
  weight = st.number_input("What is your weight? (in kilograms)",0.00,)
  st.form_submit_button("Submit")
height = height * height
try:
  bmi = weight / height
except ZeroDivisionError:
  st.write("Please give a valid number")
else:
  if bmi >= 40.0:
    st.write("You are obese")
    st.write(rd.choice(exercise))
  elif bmi >= 25.0:
    st.write("You are overweight")
    st.write(rd.choice(exercise))
  elif bmi >=18.5:
    st.write("You are normal")
    st.write(rd.choice(exercise))
  else:
    st.write("You are underweight")
    st.write(rd.choice(exercise))
