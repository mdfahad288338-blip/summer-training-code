import streamlit as st
import pickle
import numpy as np

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Student Performance Predictor")

studytime = st.slider("Study Time", 1, 4, 2)
failures = st.slider("Failures", 0, 4, 0)
absences = st.slider("Absences", 0, 100, 5)

age = st.slider("Age", 15, 22, 17)
traveltime = st.slider("Travel Time", 1, 4, 2)
famrel = st.selectbox(
    "Family Relationship",
    [
        "Very Bad",
        "Bad",
        "Average",
        "Good",
        "Excellent"
    ]
)

famrel_map = {
    "Very Bad": 1,
    "Bad": 2,
    "Average": 3,
    "Good": 4,
    "Excellent": 5
}

famrel = famrel_map[famrel]
freetime = st.selectbox(
    "Free Time After School",
    [
        "Very Low",
        "Low",
        "Average",
        "High",
        "Very High"
    ]
)

freetime_map = {
    "Very Low": 1,
    "Low": 2,
    "Average": 3,
    "High": 4,
    "Very High": 5
}

freetime = freetime_map[freetime]
goout = st.selectbox(
    "Social Activity (Going Out with Friends)",
    [
        "Rarely",
        "Sometimes",
        "Average",
        "Often",
        "Very Often"
    ]
)

goout_map = {
    "Rarely": 1,
    "Sometimes": 2,
    "Average": 3,
    "Often": 4,
    "Very Often": 5
}

goout = goout_map[goout]

G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)
if st.button("Predict Grade"):

    features = np.array([[
        studytime,
        failures,
        absences,
        age,
        traveltime,
        famrel,
        freetime,
        goout,
        G1,
        G2
    ]])

    prediction = model.predict(features)

    st.success(
        f"Predicted Final Grade: {prediction[0]:.2f}/20"
    )