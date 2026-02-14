import streamlit as st
import pickle
import pandas as pd
import os

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="AI Smart Agriculture",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 AI Smart Agriculture Production Predictor")
st.markdown("Predict Crop Production using Area & Yield")

st.divider()

# ------------------------------
# Load Trained Model (Cloud Safe)
# ------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "crop_model.pkl")

model = pickle.load(open(model_path, "rb"))

# ------------------------------
# Crop Type Selection
# ------------------------------
crop_type = st.selectbox(
    "Select Crop Type",
    ["Vegetable", "Fruit"]
)

# ------------------------------
# Input Section
# ------------------------------
area = st.number_input(
    "Enter Area (Hectares)",
    min_value=0.0,
    step=100.0
)

yield_val = st.number_input(
    "Enter Yield (MT per Hectare)",
    min_value=0.0,
    step=1.0
)

st.divider()

# ------------------------------
# Prediction Button
# ------------------------------
if st.button("Predict Production"):

    if crop_type == "Vegetable":
        input_df = pd.DataFrame(
            [[area, yield_val, 0, 0]],
            columns=[
                'Area_Hectare_Veg',
                'Yield_MT_per_Hectare_Veg',
                'Area_Hectare_Fruit',
                'Yield_MT_per_Hectare_Fruit'
            ]
        )
    else:
        input_df = pd.DataFrame(
            [[0, 0, area, yield_val]],
            columns=[
                'Area_Hectare_Veg',
                'Yield_MT_per_Hectare_Veg',
                'Area_Hectare_Fruit',
                'Yield_MT_per_Hectare_Fruit'
            ]
        )

    prediction = model.predict(input_df)

    st.success(f"Predicted Production: {prediction[0]:,.2f} MT")
    st.info("Model used: Random Forest Regressor")
