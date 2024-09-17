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
    if gender == 'Female' and age >= 2005:
      popover = st.popover("exercise plans")
      plan1 = popover.checkbox("Show Plan 1")
      plan2 = popover.checkbox("Show Plan 2")
      plan3 = popover.checkbox("Show Plan 3")
      if plan1 == True:
        st.write(rd.choice(exercise))
      elif plan2 == True:
        st.write(rd.choice(exercise))
      elif plan3 == True:
        st.write(rd.choice(exercise))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif gender == 'Female' and age >= 1975:
      popover = st.popover("exercise plans")
      plan1 = popover.checkbox("Show Plan 1")
      plan2 = popover.checkbox("Show Plan 2")
      plan3 = popover.checkbox("Show Plan 3")
      if plan1 == True:
        st.write(rd.choice(exercise))
      elif plan2 == True:
        st.write(rd.choice(exercise))
      elif plan3 == True:
        st.write(rd.choice(exercise))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif gender == 'Female' and age >= 1944:
      popover = st.popover("exercise plans")
      plan1 = popover.checkbox("Show Plan 1")
      plan2 = popover.checkbox("Show Plan 2")
      plan3 = popover.checkbox("Show Plan 3")
      if plan1 == True:
        st.write(rd.choice(exercise))
      elif plan2 == True:
        st.write(rd.choice(exercise))
      elif plan3 == True:
        st.write(rd.choice(exercise))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif gender == 'Male' and age >= 2005:
      popover = st.popover("exercise plans")
      plan1 = popover.checkbox("Show Plan 1")
      plan2 = popover.checkbox("Show Plan 2")
      plan3 = popover.checkbox("Show Plan 3")
      if plan1 == True:
        st.write(rd.choice(exercise))
      elif plan2 == True:
        st.write(rd.choice(exercise))
      elif plan3 == True:
        st.write(rd.choice(exercise))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif gender == 'Male' and age >= 1975:
      popover = st.popover("exercise plans")
      plan1 = popover.checkbox("Show Plan 1")
      plan2 = popover.checkbox("Show Plan 2")
      plan3 = popover.checkbox("Show Plan 3")
      if plan1 == True:
        st.write(rd.choice(exercise))
      elif plan2 == True:
        st.write(rd.choice(exercise))
      elif plan3 == True:
        st.write(rd.choice(exercise))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif gender == 'Male' and age >= 1944:
      popover = st.popover("exercise plans")
      plan1 = popover.checkbox("Show Plan 1")
      plan2 = popover.checkbox("Show Plan 2")
      plan3 = popover.checkbox("Show Plan 3")
      if plan1 == True:
        st.write(rd.choice(exercise))
      elif plan2 == True:
        st.write(rd.choice(exercise))
      elif plan3 == True:
        st.write(rd.choice(exercise))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    else:
      True
  elif bmi >= 25.0:
    st.write("You are overweight")
    st.write(rd.choice(exercise))
  elif bmi >=18.5:
    st.write("You are normal")
    st.write(rd.choice(exercise))
  else:
    st.write("You are underweight")
    st.write(rd.choice(exercise))
