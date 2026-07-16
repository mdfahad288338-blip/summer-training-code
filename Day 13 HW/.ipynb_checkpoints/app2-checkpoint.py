import streamlit as st
import joblib
import pandas as pd
import numpy as np


model = joblib.load("mushrooms_model.pkl","rb")

st.set_page_config(
    page_title="Mushroom Classification",
    layout="centered"
)

st.title("🍄 Mushrooms Classification")
st.write("Predict whether a mushroom is Edible or not!")

odor = st.selectbox(
    "Odor",
    [0, 1, 2, 3, 4, 5]
)

gill_size = st.selectbox(
    "Gill Size",
    [0, 1]
)

gill_color = st.selectbox(
    "Gill Color",
    list(range(12))
)

bruises = st.selectbox(
    "Bruises",
    [0, 1]
)

ring_type = st.selectbox(
    "Ring Type",
    list(range(8))
)

spore_print_color = st.selectbox(
    "Spore Print Color",
    list(range(9))
)

if st.button("Predict Mushroom"):

    mushroom_data = pd.DataFrame({
        "odor": [odor],
        "gill-size": [gill_size],
        "gill-color": [gill_color],
        "bruises": [bruises],
        "ring-type": [ring_type],
        "spore-print-color": [spore_print_color]
    })

    prediction = model.predict(mushroom_data)

    if prediction[0] == 0:
        st.success("🍄 Edible Mushroom")
        st.write("This mushroom is safe to eat.")
    else:
        st.error("☠️ Poisonous Mushroom")
        st.write("Warning! Dont ever eat these kinda mashrooms,This mushroom is predicted to be poisonous.")