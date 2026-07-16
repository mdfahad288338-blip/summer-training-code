import streamlit as st
import joblib
import numpy as np
import pandas as pd
model = joblib.load("student_performance_model.pkl","rb")
st.set_page_config(
    page_title ="Student Performance Prediction",
    layout = "centered"
)
st.title("Student Prediction")
st.write("This is for Prediction")

studytime = st.slider("Study Time",1,4,2)
failures = st.number_input("Past Class Failures", min_value=0, max_value=4, value=0)
absences = st.number_input("Number of Absences", min_value=0, value=2)
G1 = st.number_input("First Period Grade (0-20)", min_value=0, max_value=20, value=10)
G2 = st.number_input("Second Period Grade (0-20)", min_value=0, max_value=20, value=10)
if(st.button)("Predict Final Grade"):
    new_student = pd.DataFrame({
        "studytime": [studytime],
        "failures": [failures],
        "absences": [absences],
        "G1": [G1],
        "G2": [G2]
    })
    prediction = model.predict(new_student)
    grade = prediction[0]
    st.metric("📚 Predicted Final Grade", f"{grade:.2f}/20")
    if grade >= 18:
        st.success("🏆 Outstanding!")
        st.write("🎉 Excellent work! Keep up the amazing performance. Continue your hard work and aim even higher.")
    elif grade >= 16:
        st.success("🌟 Excellent")
        st.write("👏 You are performing very well. Stay consistent and keep practicing.")
    elif grade >= 14:
        st.info("😊 Very Good")
        st.write("👍 Good job! With a little more effort, you can achieve excellent grades.")
    elif grade >= 10:
        st.warning("📖 Average")
        st.write("💪 You are passing, but you should spend more time studying and revising regularly.")
    elif grade >= 5:
        st.error("⚠️ Needs Improvement")
        st.write("📚 Focus on your weak subjects, reduce distractions, and follow a proper study schedule.")
    else:
        st.error("🚨 At Risk")
        st.write("❗ Your predicted grade is very low. Seek help from your teachers, study consistently, and don't lose confidence.")


