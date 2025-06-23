import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')
st.title("🤯 Student Result Predictor")

# take the input 
gender = st.selectbox('Gender', ['Female','Male'])
ethinic = st.selectbox('ethinic',['Group A','Group B','Group C','Group D', 'Group E'])
parent_education = st.selectbox('parent education',["bachelor's degree","Associate's Degree","some college","high school","master's degree","some high school"])
lunch = st.selectbox('Lunch', ['standard', 'free/reduced'])
test_preparation = st.selectbox('Test Preparation', ['Completed','None'])
math_score = st.number_input('Math Score',0, 100)
Reading_score = st.number_input('Reading Score',0, 100)
Writing_score = st.number_input('Writing Score',0, 100)

# ethinic case
group_A = group_B = group_C = group_D = group_E = 0
if ethinic == 'Group B':
    group_B = 1
elif ethinic == 'Group C':
    group_C = 1
elif ethinic == 'Group D':
    group_D = 1
else:
    group_E = 1

# parent education case,
associate = bachelor = highschool = master = some_college = some_school = 0
if parent_education == "bachelor's degree":
    bachelor = 1
elif parent_education == "some college":
    some_college = 1
elif parent_education == "high school":
    highschool = 1
elif parent_education == "master's degree":
    master = 1
elif parent_education == "associate's degree":
    associate = 1
else:
    some_school = 1

# gender case
if gender == 'male':
    gender = 1
else:
    gender = 0

# lunch case
if lunch == 'standard':
    lunch = 1
else:
    lunch = 0

# test Preparation
if test_preparation == 'None':
    test_preparation = 1
else:
    test_preparation = 0


input_data = pd.DataFrame({
    "gender":[gender],
    "group_B":[group_B],
    "group_C":[group_C],
    "group_D":[group_D],
    "group_E":[group_E],
    "parent_education_bachelor's degree":[bachelor],
    "parent_education_high school":[highschool],
    "parent_education_master's degree":[master],
    "parent_education_some college":[some_college],
    "parent_education_some high school":[some_school],
    'lunch':[lunch],
    'preparation':[test_preparation],
    'math score':[math_score],
    'reading score':[Reading_score],
    'writing score':[Writing_score]
})


# predict output
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success("🥳 Pass" if prediction == 1 else "⛔ Fail,Try Hard")