import streamlit as st
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))

st.title("Stroke Predictor 🧠")
disclaimer = "Disclaimer: The predictions provided here are for educational purposes only and may not be accurate. Please consult a healthcare professional for personalized advice."
st.markdown(f"*{disclaimer}*")


gender = st.selectbox('Select your gender', ['Male', 'Female'])
age = st.slider('Choose your age', 1, 100, 30)
hypertension = st.selectbox('Have you been diagnosed with hypertension?', ['Yes', 'No'])

if hypertension == 'Yes':
    hypertension = 1
else:
    hypertension = 0
    
heart_disease = st.selectbox('Have you ever been diagnosed with heart disease?', ['Yes', 'No'])

if heart_disease == 'Yes':
    heart_disease = 1
else:
    heart_disease = 0

ever_married = st.selectbox("Are you married ?", ['Yes', 'No'])
work_type = st.selectbox("Choose your work type ?", ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
Residence_type = st.selectbox("Choose your residence type", ['Urban', 'Rural'])
glucose_level = st.slider("Choose your glucose level.", 50, 272, 120)
bmi = st.slider("Choose your body mass index.", 9, 98, 20)
smoking = st.selectbox("Do you smoke ?", ['formerly smoked', 'never smoked', 'smokes'])
ok = st.button("Predict")


if ok:
    prediction = model.predict(pd.DataFrame(columns=['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
                                    'work_type', 'Residence_type', 'avg_glucose_level', 'bmi',
                                    'smoking_status'],
                            data=[[gender, age, hypertension, heart_disease, ever_married,
                                    work_type, Residence_type, glucose_level, bmi, smoking]]))
    if prediction[0] == 1:
        prediction_text = "**Warning:** You have a **high risk of stroke**. Please consult a healthcare professional immediately! 🚨❗"
    else:
        prediction_text = "Great news! Your risk of stroke is **low**. Keep up the healthy lifestyle! 😄👍"

    st.markdown(prediction_text)
