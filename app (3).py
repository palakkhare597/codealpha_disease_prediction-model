import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("disease_model.pkl")

# Page Configuration
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# Title
st.title("❤️ Heart Disease Prediction")
st.write("Enter the patient's details below and click Predict.")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=50)

sex = st.selectbox(
    "Sex",
    ["Male", "Female"]
)
sex = 1 if sex == "Male" else 0

chest_pain = st.selectbox(
    "Chest Pain Type",
    [1, 2, 3, 4]
)

bp = st.number_input(
    "Resting Blood Pressure (BP)",
    min_value=50,
    max_value=250,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=100,
    max_value=700,
    value=200
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    ["No", "Yes"]
)
fbs = 1 if fbs == "Yes" else 0

ekg = st.selectbox(
    "Resting ECG Results",
    [0, 1, 2]
)

max_hr = st.number_input(
    "Maximum Heart Rate",
    min_value=50,
    max_value=250,
    value=150
)

exercise_angina = st.selectbox(
    "Exercise Induced Angina",
    ["No", "Yes"]
)
exercise_angina = 1 if exercise_angina == "Yes" else 0

st_depression = st.number_input(
    "ST Depression",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

slope = st.selectbox(
    "Slope of ST Segment",
    [1, 2, 3]
)

vessels = st.selectbox(
    "Number of Major Vessels",
    [0, 1, 2, 3]
)

thal = st.selectbox(
    "Thallium Test",
    [3, 6, 7]
)

# Prediction Button
if st.button("Predict"):

    input_data = np.array([[
        age,
        sex,
        chest_pain,
        bp,
        cholesterol,
        fbs,
        ekg,
        max_hr,
        exercise_angina,
        st_depression,
        slope,
        vessels,
        thal
    ]])

    prediction = model.predict(input_data)

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")