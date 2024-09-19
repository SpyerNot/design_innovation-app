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
    if age >= 2005:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_obese_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_obese_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_obese_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 1975:
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
    if age >= 2005:
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_overweight_teens))
        st.write(":red[Day 1\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach and mushrooms\nWhole grain toast (1 slice)\n1 small apple\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g) topped with mixed berries\nLunch (450 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nSteamed broccoli\nSnack (100 kcal)\nBaby carrots with hummus (2 tbsp)\nDinner (450 kcal)\nBaked salmon (120g)\nBrown rice (½ cup cooked)\nMixed green salad with olive oil dressing\nSnack (100 kcal)\nCottage cheese (100g) with cucumber slices\nTotal Calories: ~1570 kcal]\n:blue[Day 2\nBreakfast (370 kcal)\nOatmeal (½ cup cooked) with almond butter (1 tbsp)\n2 boiled eggs\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nTurkey breast (120g) on whole wheat wrap with lettuce, tomato, and mustard\nCucumber slices\nSnack (80 kcal)\n1 orange\nDinner (500 kcal)\nGrilled lean beef (120g)/nSteamed asparagus/nSweet potato (1 small, baked)/nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1650 kcal\n]:yellow[Day 3\nBreakfast (400 kcal)\n2 boiled eggs with whole grain toast\n1 banana\nSnack (120 kcal)/nLow-fat Greek yogurt (unsweetened, 150g) with chia seeds\nLunch (450 kcal)\nTuna salad (in water) with lettuce, cucumber, and avocado\nWhole grain crackers (4-5 pieces)\nSnack (100 kcal)\n1 small pear\nDinner (500 kcal)\nStir-fried chicken with bell peppers, onions, and zucchini\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nSliced veggies with hummus (2 tbsp)\nTotal Calories: ~1670 kcal]\n:purple[Day 4\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with tomatoes and spinach\n1 slice of whole grain toast\nSnack (150 kcal)\n1 boiled egg with sliced cucumbers\nLunch (500 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nMixed greens with olive oil and lemon dressing\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (480 kcal)\nBaked cod (120g)\nSteamed broccoli and carrots\nSweet potato (1 small, baked)\nSnack (100 kcal)\nCottage cheese (100g) with sliced bell peppers\nTotal Calories: ~1700 kcal]\n:grey[Day 5 (Asian-Inspired Meal)\nBreakfast (380 kcal)\nHard-boiled eggs (2) with avocado slices\nWhole wheat toast\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (500 kcal)\nTeriyaki grilled chicken breast (120g)\nStir-fried vegetables (bell peppers, onions, carrots)\nBrown rice (½ cup cooked)\nSnack (80 kcal)\n1 orange\nDinner (450 kcal)\nChicken and vegetable stir-fry (chicken breast, broccoli, mushrooms) with garlic and ginger\nSteamed jasmine rice (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nTotal Calories: ~1680 kcal\n:purple[Day 6\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach\nWhole grain toast (1 slice)\nSnack (150 kcal)\n1 boiled egg with cucumber slices\nLunch (500 kcal)\nGrilled turkey breast (120g) with quinoa salad (quinoa, cucumber, tomato, olive oil)\nSnack (100 kcal)\n1 small apple\nDinner (480 kcal)\nBaked salmon (120g) with a side of steamed broccoli\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nCottage cheese (100g) with bell pepper strips\nTotal Calories: ~1680 kcal]\nDay 7\nBreakfast (350 kcal)\nOmelet with mushrooms, onions, and spinach (3 large eggs)\nWhole grain toast (1 slice)\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nChicken breast (120g) with mixed greens, cherry tomatoes, and olive oil dressing\nQuinoa (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (500 kcal)\nGrilled lean beef (120g)\nSteamed carrots and green beans\nSweet potato (1 small, baked)\nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1670 kcal")
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_overweight_teens))
        st.write("Day 1\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach and mushrooms\nWhole grain toast (1 slice)\n1 small apple\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g) topped with mixed berries\nLunch (450 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nSteamed broccoli\nSnack (100 kcal)\nBaby carrots with hummus (2 tbsp)\nDinner (450 kcal)\nBaked salmon (120g)\nBrown rice (½ cup cooked)\nMixed green salad with olive oil dressing\nSnack (100 kcal)\nCottage cheese (100g) with cucumber slices\nTotal Calories: ~1570 kcal\nDay 2\nBreakfast (370 kcal)\nOatmeal (½ cup cooked) with almond butter (1 tbsp)\n2 boiled eggs\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nTurkey breast (120g) on whole wheat wrap with lettuce, tomato, and mustard\nCucumber slices\nSnack (80 kcal)\n1 orange\nDinner (500 kcal)\nGrilled lean beef (120g)/nSteamed asparagus/nSweet potato (1 small, baked)/nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1650 kcal\nDay 3\nBreakfast (400 kcal)\n2 boiled eggs with whole grain toast\n1 banana\nSnack (120 kcal)/nLow-fat Greek yogurt (unsweetened, 150g) with chia seeds\nLunch (450 kcal)\nTuna salad (in water) with lettuce, cucumber, and avocado\nWhole grain crackers (4-5 pieces)\nSnack (100 kcal)\n1 small pear\nDinner (500 kcal)\nStir-fried chicken with bell peppers, onions, and zucchini\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nSliced veggies with hummus (2 tbsp)\nTotal Calories: ~1670 kcal\nDay 4\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with tomatoes and spinach\n1 slice of whole grain toast\nSnack (150 kcal)\n1 boiled egg with sliced cucumbers\nLunch (500 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nMixed greens with olive oil and lemon dressing\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (480 kcal)\nBaked cod (120g)\nSteamed broccoli and carrots\nSweet potato (1 small, baked)\nSnack (100 kcal)\nCottage cheese (100g) with sliced bell peppers\nTotal Calories: ~1700 kcal\nDay 5 (Asian-Inspired Meal)\nBreakfast (380 kcal)\nHard-boiled eggs (2) with avocado slices\nWhole wheat toast\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (500 kcal)\nTeriyaki grilled chicken breast (120g)\nStir-fried vegetables (bell peppers, onions, carrots)\nBrown rice (½ cup cooked)\nSnack (80 kcal)\n1 orange\nDinner (450 kcal)\nChicken and vegetable stir-fry (chicken breast, broccoli, mushrooms) with garlic and ginger\nSteamed jasmine rice (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nTotal Calories: ~1680 kcal\nDay 6\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach\nWhole grain toast (1 slice)\nSnack (150 kcal)\n1 boiled egg with cucumber slices\nLunch (500 kcal)\nGrilled turkey breast (120g) with quinoa salad (quinoa, cucumber, tomato, olive oil)\nSnack (100 kcal)\n1 small apple\nDinner (480 kcal)\nBaked salmon (120g) with a side of steamed broccoli\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nCottage cheese (100g) with bell pepper strips\nTotal Calories: ~1680 kcal\nDay 7\nBreakfast (350 kcal)\nOmelet with mushrooms, onions, and spinach (3 large eggs)\nWhole grain toast (1 slice)\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nChicken breast (120g) with mixed greens, cherry tomatoes, and olive oil dressing\nQuinoa (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (500 kcal)\nGrilled lean beef (120g)\nSteamed carrots and green beans\nSweet potato (1 small, baked)\nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1670 kcal")
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_overweight_teens))
        st.write("Day 1\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach and mushrooms\nWhole grain toast (1 slice)\n1 small apple\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g) topped with mixed berries\nLunch (450 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nSteamed broccoli\nSnack (100 kcal)\nBaby carrots with hummus (2 tbsp)\nDinner (450 kcal)\nBaked salmon (120g)\nBrown rice (½ cup cooked)\nMixed green salad with olive oil dressing\nSnack (100 kcal)\nCottage cheese (100g) with cucumber slices\nTotal Calories: ~1570 kcal\nDay 2\nBreakfast (370 kcal)\nOatmeal (½ cup cooked) with almond butter (1 tbsp)\n2 boiled eggs\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nTurkey breast (120g) on whole wheat wrap with lettuce, tomato, and mustard\nCucumber slices\nSnack (80 kcal)\n1 orange\nDinner (500 kcal)\nGrilled lean beef (120g)/nSteamed asparagus/nSweet potato (1 small, baked)/nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1650 kcal\nDay 3\nBreakfast (400 kcal)\n2 boiled eggs with whole grain toast\n1 banana\nSnack (120 kcal)/nLow-fat Greek yogurt (unsweetened, 150g) with chia seeds\nLunch (450 kcal)\nTuna salad (in water) with lettuce, cucumber, and avocado\nWhole grain crackers (4-5 pieces)\nSnack (100 kcal)\n1 small pear\nDinner (500 kcal)\nStir-fried chicken with bell peppers, onions, and zucchini\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nSliced veggies with hummus (2 tbsp)\nTotal Calories: ~1670 kcal\nDay 4\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with tomatoes and spinach\n1 slice of whole grain toast\nSnack (150 kcal)\n1 boiled egg with sliced cucumbers\nLunch (500 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nMixed greens with olive oil and lemon dressing\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (480 kcal)\nBaked cod (120g)\nSteamed broccoli and carrots\nSweet potato (1 small, baked)\nSnack (100 kcal)\nCottage cheese (100g) with sliced bell peppers\nTotal Calories: ~1700 kcal\nDay 5 (Asian-Inspired Meal)\nBreakfast (380 kcal)\nHard-boiled eggs (2) with avocado slices\nWhole wheat toast\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (500 kcal)\nTeriyaki grilled chicken breast (120g)\nStir-fried vegetables (bell peppers, onions, carrots)\nBrown rice (½ cup cooked)\nSnack (80 kcal)\n1 orange\nDinner (450 kcal)\nChicken and vegetable stir-fry (chicken breast, broccoli, mushrooms) with garlic and ginger\nSteamed jasmine rice (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nTotal Calories: ~1680 kcal\nDay 6\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach\nWhole grain toast (1 slice)\nSnack (150 kcal)\n1 boiled egg with cucumber slices\nLunch (500 kcal)\nGrilled turkey breast (120g) with quinoa salad (quinoa, cucumber, tomato, olive oil)\nSnack (100 kcal)\n1 small apple\nDinner (480 kcal)\nBaked salmon (120g) with a side of steamed broccoli\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nCottage cheese (100g) with bell pepper strips\nTotal Calories: ~1680 kcal\nDay 7\nBreakfast (350 kcal)\nOmelet with mushrooms, onions, and spinach (3 large eggs)\nWhole grain toast (1 slice)\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nChicken breast (120g) with mixed greens, cherry tomatoes, and olive oil dressing\nQuinoa (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (500 kcal)\nGrilled lean beef (120g)\nSteamed carrots and green beans\nSweet potato (1 small, baked)\nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1670 kcal")
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 1975:
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
    if age >= 2005:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_normal_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_normal_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_normal_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 1975:      
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
    if age >= 2005:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write("You should start eating more man")
      elif plans == 'Plan 2':
        st.write("You should start eating more man")
      elif plans == 'Plan 3':
        st.write("You should start eating more man")
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 1975:      
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write("You should start eating more man")
      elif plans == 'Plan 2':
        st.write("You should start eating more man")
      elif plans == 'Plan 3':
        st.write("You should start eating more man")
      else:
        st.write("Ok,I seee that you do not want to exercise")
    else:      
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write("You should start eating more man")
      elif plans == 'Plan 2':
        st.write("You should start eating more man")
      elif plans == 'Plan 3':
        st.write("You should start eating more man")
      else:
        st.write("Ok,I seee that you do not want to exercise")
