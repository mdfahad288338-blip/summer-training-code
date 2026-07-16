import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("titanic_model.pkl","rb")

# Page Config
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

# Header
st.title("🚢 Titanic Survival Predictor")
st.write(
    "Predict whether a passenger would have survived the Titanic disaster using Machine Learning."
)

# Passenger Form
st.subheader("👤 Passenger Information")

class_option = st.selectbox(
    "🚢 Passenger Class",
    ["🥇 First Class","🥈 Second Class","🥉 Third Class"]
)

sex = st.selectbox(
    label="Gender",
    options=["Male", "Female"]
)
sex = 1 if "Gender" == "Male" else 0
age = st.slider(
    "🎂 Age",
    0,80,25
)

fare = st.number_input(
    "💰 Ticket Fare",
    min_value=0.0,
    value=50.0
)

sibsp = st.number_input(
    "👫 Siblings / Spouse",
    min_value=0,
    max_value=10,
    value=0
)

parch = st.number_input(
    "👨‍👩‍👧 Parents / Children",
    min_value=0,
    max_value=10,
    value=0
)

embarked = st.selectbox(
    "⚓ Embarked Port",
    ["Southampton","Cherbourg","Queenstown"]
)
embarked_map = {
    "Southampton": 0,
    "Cherbourg": 1,
    "Queenstown": 2
}

embarked = embarked_map[embarked]
pclass_map = {
    "🥇 First Class": 1,
    "🥈 Second Class": 2,
    "🥉 Third Class": 3
}

pclass = pclass_map[class_option]

st.markdown("---")

# Prediction

if st.button("🔮 Predict Survival"):

    passenger = pd.DataFrame({
        "Pclass": [pclass],
        "Sex": [sex],
        "Age": [age],
        "SibSp": [sibsp],
        "Parch": [parch],
        "Fare": [fare],
        "Embarked": [embarked]
    })

    prediction = model.predict(passenger)[0]
    probability = model.predict_proba(passenger)[0]

    st.subheader("🎯 Prediction Result")

    if prediction == 1:
        st.success("✅ Passenger Likely To Survive")
    else:
        st.error("❌ Passenger Unlikely To Survive")

    st.metric(
        "Survival Probability",
        f"{probability[1]*100:.2f}%"
    )

    st.progress(float(probability[1]))

st.markdown("---")
st.caption("🚀 Developed by Fahad")
