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
        st.write("Day 1\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach and mushrooms\nWhole grain toast (1 slice)\n1 small apple\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g) topped with mixed berries\nLunch (450 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nSteamed broccoli\nSnack (100 kcal)\nBaby carrots with hummus (2 tbsp)\nDinner (450 kcal)\nBaked salmon (120g)\nBrown rice (½ cup cooked)\nMixed green salad with olive oil dressing\nSnack (100 kcal)\nCottage cheese (100g) with cucumber slices\nTotal Calories: ~1570 kcal\nDay 2\nBreakfast (370 kcal)\nOatmeal (½ cup cooked) with almond butter (1 tbsp)\n
2 boiled eggs
Snack (150 kcal)

Handful of almonds (15-20 pieces)
Lunch (450 kcal)

Turkey breast (120g) on whole wheat wrap with lettuce, tomato, and mustard
Cucumber slices
Snack (80 kcal)

1 orange
Dinner (500 kcal)

Grilled lean beef (120g)
Steamed asparagus
Sweet potato (1 small, baked)
Snack (100 kcal)

Low-fat string cheese
Total Calories: ~1650 kcal

Day 3
Breakfast (400 kcal)

2 boiled eggs with whole grain toast
1 banana
Snack (120 kcal)

Low-fat Greek yogurt (unsweetened, 150g) with chia seeds
Lunch (450 kcal)

Tuna salad (in water) with lettuce, cucumber, and avocado
Whole grain crackers (4-5 pieces)
Snack (100 kcal)

1 small pear
Dinner (500 kcal)

Stir-fried chicken with bell peppers, onions, and zucchini
Brown rice (½ cup cooked)
Snack (100 kcal)

Sliced veggies with hummus (2 tbsp)
Total Calories: ~1670 kcal

Day 4
Breakfast (350 kcal)

Scrambled eggs (3 large eggs) with tomatoes and spinach
1 slice of whole grain toast
Snack (150 kcal)

1 boiled egg with sliced cucumbers
Lunch (500 kcal)

Grilled chicken breast (120g)
Quinoa (½ cup cooked)
Mixed greens with olive oil and lemon dressing
Snack (120 kcal)

Greek yogurt (unsweetened, 150g)
Dinner (480 kcal)

Baked cod (120g)
Steamed broccoli and carrots
Sweet potato (1 small, baked)
Snack (100 kcal)

Cottage cheese (100g) with sliced bell peppers
Total Calories: ~1700 kcal

Day 5 (Asian-Inspired Meal)
Breakfast (380 kcal)

Hard-boiled eggs (2) with avocado slices
Whole wheat toast
Snack (150 kcal)

Handful of almonds (15-20 pieces)
Lunch (500 kcal)

Teriyaki grilled chicken breast (120g)
Stir-fried vegetables (bell peppers, onions, carrots)
Brown rice (½ cup cooked)
Snack (80 kcal)

1 orange
Dinner (450 kcal)

Chicken and vegetable stir-fry (chicken breast, broccoli, mushrooms) with garlic and ginger
Steamed jasmine rice (½ cup cooked)
Snack (120 kcal)

Greek yogurt (unsweetened, 150g)
Total Calories: ~1680 kcal

Day 6
Breakfast (350 kcal)

Scrambled eggs (3 large eggs) with spinach
Whole grain toast (1 slice)
Snack (150 kcal)

1 boiled egg with cucumber slices
Lunch (500 kcal)

Grilled turkey breast (120g) with quinoa salad (quinoa, cucumber, tomato, olive oil)
Snack (100 kcal)

1 small apple
Dinner (480 kcal)

Baked salmon (120g) with a side of steamed broccoli
Brown rice (½ cup cooked)
Snack (100 kcal)

Cottage cheese (100g) with bell pepper strips
Total Calories: ~1680 kcal

Day 7
Breakfast (350 kcal)

Omelet with mushrooms, onions, and spinach (3 large eggs)
Whole grain toast (1 slice)
Snack (150 kcal)

Handful of almonds (15-20 pieces)
Lunch (450 kcal)

Chicken breast (120g) with mixed greens, cherry tomatoes, and olive oil dressing
Quinoa (½ cup cooked)
Snack (120 kcal)

Greek yogurt (unsweetened, 150g)
Dinner (500 kcal)

Grilled lean beef (120g)
Steamed carrots and green beans
Sweet potato (1 small, baked)
Snack (100 kcal)

Low-fat string cheese
Total Calories: ~1670 kcal")
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
    else:      
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
    if age >= 2011:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_normal_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_normal_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_normal_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 2004:      
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_normal_adult))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_normal_adult))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_normal_adult))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    else:      
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
      st.write("start eating more man" )
    elif plans == 'Plan 2':
      st.write(rd.choice("Start eating more man")
    elif plans == 'Plan 3':
      st.write(rd.choice("Start eating more man")
    else:
      st.write("Ok,I seee that you do not want to exercise")
