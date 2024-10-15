import streamlit as st
import random as rd
exercise_obese_teens = ['Goal: Improve cardiovascular health and flexibility.Duration: 30 minutes/day, 5 days/week.Week Layout: Day 1-5:Warm-up: 5 minutes of brisk walking.Main Exercise: 20 minutes of moderate walking.Cool-down: 5 minutes of full-body stretching.Day 6-7: Rest or light stretching.','Goal: Increase heart rate without putting too much strain on joints.Duration: 30-40 minutes/day, 4 days/week.Week Layout: Day 1 & 3: Warm-up: 5 minutes of marching in place.Main Exercise: 20 minutes of low-impact aerobics (step-touch, side-steps, light dance moves).Cool-down: 5 minutes of stretching.Day 2 & 4:20 minutes of gentle swimming or water walking (if available).Day 5-7: Rest or light stretching.','Goal: Build strength using bodyweight exercises.Duration: 20-30 minutes/day, 3 days/weekWeek Layout: Day 1, 3, 5: Warm-up: 5 minutes of walking. Circuit (3 rounds with 1-minute rest between rounds):10 squats,10 wall push-ups,10-second plank,10 glute bridges.Cool-down: 5 minutes of stretching. Day 2, 4, 6-7: Rest or light walking.','Goal: Make exercise fun with dance routines. Duration: 20-30 minutes/day, 5 days/week. Week Layout: Day 1-5: Warm-up: 5 minutes of light dancing. Main Exercise: 20 minutes of following a simple dance workout (YouTube, or a dance-based app). Cool-down: 5 minutes of stretching. Day 6-7: Rest or casual dance for fun.']
exercise_overweight_teens = ['Exercise Plan: Day 1: 30-minute brisk walk + 15-minute bodyweight exercises (squats, lunges, push-ups). Day 2: 20-minute light jogging + 10-minute stretching (hamstrings, quads, calves). Day 3: Rest day or gentle yoga (20 minutes). Day 4: 30-minute cycling or swimming + 10-minute core workout (plank, crunches). Day 5: 20-minute interval running (30 sec sprint/1 min walk) + 15-minute strength workout (planks, burpees). Day 6: Fun outdoor activity (soccer, basketball, or dance) for 45 minutes.Day 7: Rest or 15-minute yoga/stretching. Eating Plan: Breakfast: Greek yogurt with mixed berries and a handful of oats. Lunch: Grilled chicken wrap with whole grain tortillas, veggies, and a light dressing. Snack: Apple slices with almond butter. Dinner: Baked salmon with quinoa and steamed vegetables. Hydration: Drink 6-8 cups of water a day. Limit: Sugary drinks and processed snacks','Exercise Plan: Day 1: 25-minute run + 15-minute bodyweight circuit (push-ups, squats, plank). Day 2: Rest or 30 minutes of stretching/yoga. Day 3: 30-minute strength workout (using light weights or resistance bands). Day 4: 40-minute brisk walk or moderate cycling. Day 5: High-intensity interval training (HIIT): 20 seconds work, 40 seconds rest, for 25 minutes (jumping jacks, squats, mountain climbers). Day 6: 45-minute swimming or dancing. Day 7: Active recovery day (light walk or stretching for 20 minutes). Eating Plan: Breakfast: Scrambled eggs with whole-grain toast and a side of fruit. Lunch: Turkey and avocado sandwich on whole wheat bread with side salad. Snack: A banana or handful of nuts. Dinner: Stir-fry tofu or chicken with brown rice and mixed veggies. Hydration: 6-8 cups of water daily. Limit: Fried and fast foods','Exercise Plan: Day 1: 40-minute light jog or power walk. Day 2: 25-minute stair climbing or hill sprints. Day 3: Rest or 20-minute yoga session. Day 4: 30-minute bike ride or rollerblading. Day 5: 45-minute dance workout (Zumba or any fun dance routines). Day 6: Play a sport of your choice (soccer, basketball, or tennis) for 60 minutes. Day 7: Rest or stretching (15 minutes).Eating Plan: Breakfast: Smoothie with spinach, banana, almond milk, and chia seeds. Lunch: Grilled chicken salad with mixed greens, avocado, and olive oil dressing. Snack: Mixed nuts or carrots with hummus. Dinner: Grilled lean beef or turkey burger (without bun) with a sweet potato and steamed vegetables. Hydration: 7-9 cups of water daily. Limit: Sugary treats and processed foods','Exercise Plan: Day 1: 20-minute jump rope session + 10 minutes of ab exercises (planks, crunches). Day 2: 30-minute bodyweight strength workout (lunges, squats, push-ups). Day 3: Rest or gentle stretching for 15 minutes. Day 4: 30-minute interval running (1 minute sprint, 2 minutes jog). Day 5: Strength training using light weights or resistance bands (20-25 minutes). Day 6: 45-minute brisk walk or swimming. Day 7: Fun outdoor activity (bike ride, hike, or sports) for 60 minutes. Eating Plan. Breakfast: Oatmeal with almond milk, nuts, and a drizzle of honey. Lunch: Whole grain pasta with grilled chicken, olive oil, and vegetables. Snack: Greek yogurt or fruit salad. Dinner: Baked chicken or turkey breast with roasted vegetables and brown rice. Hydration: 6-8 cups of water.Limit: Soda and sugary cereals','Exercise Plan: Day 1: 25-minute yoga/stretching session + 10 minutes of light bodyweight exercises. Day 2: 30-minute moderate-intensity cardio (jogging, biking). Day 3: Rest or stretching (15 minutes). Day 4: 40-minute swimming or brisk walk. Day 5: HIIT workout (jump squats, burpees, push-ups) for 20 minutes. Day 6: Fun sports activity (basketball, tennis, soccer) for 60 minutes.Day 7: Rest or stretching/yoga for 20 minutes.Eating Plan: Breakfast: Whole-grain cereal with almond milk and fresh fruit. Lunch: Tuna or chicken salad sandwich on whole-grain bread. Snack: A small handful of almonds or a piece of fruit. Dinner: Grilled fish with quinoa and sautéed vegetables. Hydration: 7-9 cups of water daily.Limit: Junk food and heavy sauces']
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
        st.write(":red[Day 1\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach and mushrooms\nWhole grain toast (1 slice)\n1 small apple\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g) topped with mixed berries\nLunch (450 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nSteamed broccoli\nSnack (100 kcal)\nBaby carrots with hummus (2 tbsp)\nDinner (450 kcal)\nBaked salmon (120g)\nBrown rice (½ cup cooked)\nMixed green salad with olive oil dressing\nSnack (100 kcal)\nCottage cheese (100g) with cucumber slices\nTotal Calories: ~1570 kcal]\n:blue[Day 2\nBreakfast (370 kcal)\nOatmeal (½ cup cooked) with almond butter (1 tbsp)\n2 boiled eggs\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nTurkey breast (120g) on whole wheat wrap with lettuce, tomato, and mustard\nCucumber slices\nSnack (80 kcal)\n1 orange\nDinner (500 kcal)\nGrilled lean beef (120g)\nSteamed asparagus\nSweet potato (1 small, baked)\nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1650 kcal]\n:red[Day 3\nBreakfast (400 kcal)\n2 boiled eggs with whole grain toast\n1 banana\nSnack (120 kcal)/nLow-fat Greek yogurt (unsweetened, 150g) with chia seeds\nLunch (450 kcal)\nTuna salad (in water) with lettuce, cucumber, and avocado\nWhole grain crackers (4-5 pieces)\nSnack (100 kcal)\n1 small pear\nDinner (500 kcal)\nStir-fried chicken with bell peppers, onions, and zucchini\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nSliced veggies with hummus (2 tbsp)\nTotal Calories: ~1670 kcal]\n]:blue[Day 4\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with tomatoes and spinach\n1 slice of whole grain toast\nSnack (150 kcal)\n1 boiled egg with sliced cucumbers\nLunch (500 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nMixed greens with olive oil and lemon dressing\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (480 kcal)\nBaked cod (120g)\nSteamed broccoli and carrots\nSweet potato (1 small, baked)\nSnack (100 kcal)\nCottage cheese (100g) with sliced bell peppers\nTotal Calories: ~1700 kcal]\n:red[Day 5 (Asian-Inspired Meal)\nBreakfast (380 kcal)\nHard-boiled eggs (2) with avocado slices\nWhole wheat toast\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (500 kcal)\nTeriyaki grilled chicken breast (120g)\nStir-fried vegetables (bell peppers, onions, carrots)\nBrown rice (½ cup cooked)\nSnack (80 kcal)\n1 orange\nDinner (450 kcal)\nChicken and vegetable stir-fry (chicken breast, broccoli, mushrooms) with garlic and ginger\nSteamed jasmine rice (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nTotal Calories: ~1680 kcal\n]:blue[Day 6\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach\nWhole grain toast (1 slice)\nSnack (150 kcal)\n1 boiled egg with cucumber slices\nLunch (500 kcal)\nGrilled turkey breast (120g) with quinoa salad (quinoa, cucumber, tomato, olive oil)\nSnack (100 kcal)\n1 small apple\nDinner (480 kcal)\nBaked salmon (120g) with a side of steamed broccoli\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nCottage cheese (100g) with bell pepper strips\nTotal Calories: ~1680 kcal]\n:red[Day 7\nBreakfast (350 kcal)\nOmelet with mushrooms, onions, and spinach (3 large eggs)\nWhole grain toast (1 slice)\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nChicken breast (120g) with mixed greens, cherry tomatoes, and olive oil dressing\nQuinoa (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (500 kcal)\nGrilled lean beef (120g)\nSteamed carrots and green beans\nSweet potato (1 small, baked)\nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1670 kcal]")
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_overweight_teens))
        st.write(":red[Day 1\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach and mushrooms\nWhole grain toast (1 slice)\n1 small apple\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g) topped with mixed berries\nLunch (450 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nSteamed broccoli\nSnack (100 kcal)\nBaby carrots with hummus (2 tbsp)\nDinner (450 kcal)\nBaked salmon (120g)\nBrown rice (½ cup cooked)\nMixed green salad with olive oil dressing\nSnack (100 kcal)\nCottage cheese (100g) with cucumber slices\nTotal Calories: ~1570 kcal]\n:blue[Day 2\nBreakfast (370 kcal)\nOatmeal (½ cup cooked) with almond butter (1 tbsp)\n2 boiled eggs\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nTurkey breast (120g) on whole wheat wrap with lettuce, tomato, and mustard\nCucumber slices\nSnack (80 kcal)\n1 orange\nDinner (500 kcal)\nGrilled lean beef (120g)\nSteamed asparagus\nSweet potato (1 small, baked)\nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1650 kcal]\n:red[Day 3\nBreakfast (400 kcal)\n2 boiled eggs with whole grain toast\n1 banana\nSnack (120 kcal)/nLow-fat Greek yogurt (unsweetened, 150g) with chia seeds\nLunch (450 kcal)\nTuna salad (in water) with lettuce, cucumber, and avocado\nWhole grain crackers (4-5 pieces)\nSnack (100 kcal)\n1 small pear\nDinner (500 kcal)\nStir-fried chicken with bell peppers, onions, and zucchini\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nSliced veggies with hummus (2 tbsp)\nTotal Calories: ~1670 kcal]\n]:blue[Day 4\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with tomatoes and spinach\n1 slice of whole grain toast\nSnack (150 kcal)\n1 boiled egg with sliced cucumbers\nLunch (500 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nMixed greens with olive oil and lemon dressing\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (480 kcal)\nBaked cod (120g)\nSteamed broccoli and carrots\nSweet potato (1 small, baked)\nSnack (100 kcal)\nCottage cheese (100g) with sliced bell peppers\nTotal Calories: ~1700 kcal]\n:red[Day 5 (Asian-Inspired Meal)\nBreakfast (380 kcal)\nHard-boiled eggs (2) with avocado slices\nWhole wheat toast\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (500 kcal)\nTeriyaki grilled chicken breast (120g)\nStir-fried vegetables (bell peppers, onions, carrots)\nBrown rice (½ cup cooked)\nSnack (80 kcal)\n1 orange\nDinner (450 kcal)\nChicken and vegetable stir-fry (chicken breast, broccoli, mushrooms) with garlic and ginger\nSteamed jasmine rice (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nTotal Calories: ~1680 kcal\n]:blue[Day 6\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach\nWhole grain toast (1 slice)\nSnack (150 kcal)\n1 boiled egg with cucumber slices\nLunch (500 kcal)\nGrilled turkey breast (120g) with quinoa salad (quinoa, cucumber, tomato, olive oil)\nSnack (100 kcal)\n1 small apple\nDinner (480 kcal)\nBaked salmon (120g) with a side of steamed broccoli\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nCottage cheese (100g) with bell pepper strips\nTotal Calories: ~1680 kcal]\n:red[Day 7\nBreakfast (350 kcal)\nOmelet with mushrooms, onions, and spinach (3 large eggs)\nWhole grain toast (1 slice)\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nChicken breast (120g) with mixed greens, cherry tomatoes, and olive oil dressing\nQuinoa (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (500 kcal)\nGrilled lean beef (120g)\nSteamed carrots and green beans\nSweet potato (1 small, baked)\nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1670 kcal]")
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_overweight_teens))
        st.write(":red[Day 1\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach and mushrooms\nWhole grain toast (1 slice)\n1 small apple\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g) topped with mixed berries\nLunch (450 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nSteamed broccoli\nSnack (100 kcal)\nBaby carrots with hummus (2 tbsp)\nDinner (450 kcal)\nBaked salmon (120g)\nBrown rice (½ cup cooked)\nMixed green salad with olive oil dressing\nSnack (100 kcal)\nCottage cheese (100g) with cucumber slices\nTotal Calories: ~1570 kcal]\n:blue[Day 2\nBreakfast (370 kcal)\nOatmeal (½ cup cooked) with almond butter (1 tbsp)\n2 boiled eggs\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nTurkey breast (120g) on whole wheat wrap with lettuce, tomato, and mustard\nCucumber slices\nSnack (80 kcal)\n1 orange\nDinner (500 kcal)\nGrilled lean beef (120g)\nSteamed asparagus\nSweet potato (1 small, baked)\nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1650 kcal]\n:red[Day 3\nBreakfast (400 kcal)\n2 boiled eggs with whole grain toast\n1 banana\nSnack (120 kcal)/nLow-fat Greek yogurt (unsweetened, 150g) with chia seeds\nLunch (450 kcal)\nTuna salad (in water) with lettuce, cucumber, and avocado\nWhole grain crackers (4-5 pieces)\nSnack (100 kcal)\n1 small pear\nDinner (500 kcal)\nStir-fried chicken with bell peppers, onions, and zucchini\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nSliced veggies with hummus (2 tbsp)\nTotal Calories: ~1670 kcal]\n]:blue[Day 4\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with tomatoes and spinach\n1 slice of whole grain toast\nSnack (150 kcal)\n1 boiled egg with sliced cucumbers\nLunch (500 kcal)\nGrilled chicken breast (120g)\nQuinoa (½ cup cooked)\nMixed greens with olive oil and lemon dressing\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (480 kcal)\nBaked cod (120g)\nSteamed broccoli and carrots\nSweet potato (1 small, baked)\nSnack (100 kcal)\nCottage cheese (100g) with sliced bell peppers\nTotal Calories: ~1700 kcal]\n:red[Day 5 (Asian-Inspired Meal)\nBreakfast (380 kcal)\nHard-boiled eggs (2) with avocado slices\nWhole wheat toast\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (500 kcal)\nTeriyaki grilled chicken breast (120g)\nStir-fried vegetables (bell peppers, onions, carrots)\nBrown rice (½ cup cooked)\nSnack (80 kcal)\n1 orange\nDinner (450 kcal)\nChicken and vegetable stir-fry (chicken breast, broccoli, mushrooms) with garlic and ginger\nSteamed jasmine rice (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nTotal Calories: ~1680 kcal\n]:blue[Day 6\nBreakfast (350 kcal)\nScrambled eggs (3 large eggs) with spinach\nWhole grain toast (1 slice)\nSnack (150 kcal)\n1 boiled egg with cucumber slices\nLunch (500 kcal)\nGrilled turkey breast (120g) with quinoa salad (quinoa, cucumber, tomato, olive oil)\nSnack (100 kcal)\n1 small apple\nDinner (480 kcal)\nBaked salmon (120g) with a side of steamed broccoli\nBrown rice (½ cup cooked)\nSnack (100 kcal)\nCottage cheese (100g) with bell pepper strips\nTotal Calories: ~1680 kcal]\n:red[Day 7\nBreakfast (350 kcal)\nOmelet with mushrooms, onions, and spinach (3 large eggs)\nWhole grain toast (1 slice)\nSnack (150 kcal)\nHandful of almonds (15-20 pieces)\nLunch (450 kcal)\nChicken breast (120g) with mixed greens, cherry tomatoes, and olive oil dressing\nQuinoa (½ cup cooked)\nSnack (120 kcal)\nGreek yogurt (unsweetened, 150g)\nDinner (500 kcal)\nGrilled lean beef (120g)\nSteamed carrots and green beans\nSweet potato (1 small, baked)\nSnack (100 kcal)\nLow-fat string cheese\nTotal Calories: ~1670 kcal]")
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
