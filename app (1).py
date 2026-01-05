import streamlit as st
import numpy as np
import pickle
import os

st.title("🎓 Student Performance Prediction")

MODEL_PATH = "student_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("Model file not found. Please upload student_model.pkl")
else:
    model = pickle.load(open(MODEL_PATH, "rb"))

    study_hours = st.number_input("Study Hours", 0.0)
    attendance = st.number_input("Attendance (%)", 0.0)
    previous_score = st.number_input("Previous Score", 0.0)
    assignment_score = st.number_input("Assignment Score", 0.0)

    if st.button("Predict"):
        data = np.array([[study_hours, attendance, previous_score, assignment_score]])
        prediction = model.predict(data)
        st.success(f"Predicted Final Score: {prediction[0]:.2f}")
