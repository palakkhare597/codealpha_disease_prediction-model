import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "joblib"])

import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("heart_disease_model.pkl")

# Page Configuration
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")

st.title("❤️ Heart Disease Prediction ")
st.write("Fill in the patient's details below and click **Predict**.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 20, 100, 50)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", [1, 2, 3, 4])
    trestbps = st.number_input("Resting Blood Pressure", 80, 220, 120)
    chol = st.number_input("Serum Cholesterol", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar >120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG", [0, 1, 2])

with col2:
    thalach = st.number_input("Maximum Heart Rate", 60, 220, 150)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("Old Peak", 0.0, 10.0, 1.0)
    slope = st.selectbox("Slope", [1, 2, 3])
    ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3])
    thal = st.selectbox("Thal", [3, 6, 7])

if sex == "Male":
    sex = 1
else:
    sex = 0

input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                        restecg, thalach, exang, oldpeak,
                        slope, ca, thal]])

st.markdown("###")

if st.button("❤️ Predict Heart Disease", use_container_width=True):

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    st.markdown("---")

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")

    st.subheader("Prediction Probability")

    st.write(f"Heart Disease: **{probability[0][1]*100:.2f}%**")
    st.progress(float(probability[0][1]))

    st.write(f"No Heart Disease: **{probability[0][0]*100:.2f}%**")

    st.markdown("---")

    st.subheader("Entered Details")

    st.table({
        "Feature": [
            "Age", "Sex", "Chest Pain", "Blood Pressure",
            "Cholesterol", "FBS", "Rest ECG",
            "Max Heart Rate", "Exercise Angina",
            "Old Peak", "Slope", "Major Vessels", "Thal"
        ],
        "Value": [
            age, sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang,
            oldpeak, slope, ca, thal
        ]
    })

