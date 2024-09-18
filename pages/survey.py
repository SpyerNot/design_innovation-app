import streamlit as st
import random as rd
exercise_obese_teens = ['walk for 25 mins','cycle for 25 mins','swim for 25 mins','Squats (3 sets of 10-12)','Wall Push-ups (3 sets of 10-12)','Lunges (3 sets of 10 each leg)','Planks (Hold for 15-30 seconds, 3 times)']
exercise_overweight_teens = ['walk for 25 mins','run for 2 mins then walk for 3 mins','cycle for 25 mins','swim for 25 mins','Squats: 3 sets of 10-15 reps.','Push-Ups (modified if necessary): 3 sets of 8-12 reps','Lunges: 3 sets of 10-12 reps on each leg','Plank: Hold for 30 seconds']
exercise_normal_teens = ['Squats (12 reps) x 3','Push-ups (10 reps) x 3','Lunges (10 reps per leg) x 3','Plank (30 seconds) x 3','Bicycle crunches (15 reps per side) x 3','Jump squats (10 reps) x 3','Russian twists (3 sets of 15 reps per side)','Leg raises (3 sets of 12 reps)','Mountain climbers (3 sets of 30 seconds)','Side plank (hold for 30 seconds per side, 3 sets)']
exercise_obese_adult = ['easy cycling for 20 mins','yoga for 20 mins','10-12 chair squats x 2','12 seated leg lifts x 2','12 seated arm curls using water bottle x 2','20 mins of brisk walking at a moderate pace','25 mins walk on a slight slope/hill','20 mins slow walk','30 mins brisk walk','30 mins yoga','cycle for 30 mins']
exercise_overweight_adult = ['walk for 25 mins','cycle for 25 mins','Bodyweight squats (10-12 reps) x 3','Modified push-ups (on knees or against a wall, 10 reps) x 3','Glute bridges (10-12 reps) x 3','Plank (hold for 15-30 seconds, depending on ability) x 3']
exercise_normal_adult = ['Squats (12-15 reps) x 3','Push-ups (10-15 reps) x 3','Lunges (10 reps per leg) x 3','Plank (hold for 30-60 seconds) x 3','20 seconds of sprinting or fast cycling, followed by 40 seconds of slow pace, for 15-20 minutes','Shoulder presses (10-12 reps) x 3','Bicep curls (12-15 reps) x 3','Tricep dips (10-12 reps) x 3','Push-ups or chest press (10-12 reps)','Leg raises (12-15 reps)']
st.set_page_config(page_title="Welcome")
st.title("Your Specialized Exercise Plans Are Here!!")
st.subheader("Come and fill up this form to know what exercise plan works for you.")
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
    if age >= 2011:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_obese_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_obese_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_obese_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 2004:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_obese_adult))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_obese_adult))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_obese_adult))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    else:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_obese_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_obese_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_obese_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")  
      
  elif bmi >= 25.0:
    st.write("You are overweight")
    plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
    if age >= 2011:
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_overweight_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_overweight_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_overweight_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 2004:
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_overweight_adult))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_overweight_adult))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_overweight_adult))
      else:
        st.write("Ok,I seee that you do not want to exercise")    
  elif bmi >=18.5:
    st.write("You are normal")
    plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
    if plans == 'Plan 1':
      st.write(rd.choice(exercise_normal_teens))
    elif plans == 'Plan 2':
      st.write(rd.choice(exercise_normal_teens))
    elif plans == 'Plan 3':
      st.write(rd.choice(exercise_normal_teens))
    else:
      st.write("Ok,I seee that you do not want to exercise")
  else:
    st.write("You are underweight")
    plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
    if plans == 'Plan 1':
      st.write(rd.choice(exercise))
    elif plans == 'Plan 2':
      st.write(rd.choice(exercise))
    elif plans == 'Plan 3':
      st.write(rd.choice(exercise))
    else:
      st.write("Ok,I seee that you do not want to exercise")
