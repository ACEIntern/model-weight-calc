import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model_pipeline.pkl")

st.title("ACE Model Weight Predictor")

st.markdown("### Enter Model Specifications Below")

col1, col2 = st.columns(2)

with col1:
    length = st.number_input("Model Length (m)", step=1.0)
    breadth = st.number_input("Model Breadth (m)", step=1.0)
    height = st.number_input("Model Height (m)", step=1.0)

with col2:
    tiers = st.number_input("Number of Vertical Separations in Model", step=1)
    compartments = st.number_input("Number of Compartments in Model", step=1)

material = st.selectbox("Material", ["Aluminium (Al)", "Mild Steel (MS)"])

# Extract short code
material_code = "Al" if "Aluminium" in material else "MS"
density = 2700 if material_code == "Al" else 7850

if st.button("Predict Weight"):
    inputs = pd.DataFrame([{
        "Model Length": length,
        "Model Breadth": breadth,
        "Model Height": height,
        "Number of Tiers in Model": tiers,
        "Number of Compartments in Model": compartments,
        "Density": density
    }])

    prediction = model.predict(inputs)[0] * 1.1
    st.success(f"Predicted Weight : **{prediction:.2f} kg**")

st.markdown("---")
st.caption("Made by ACE Switchboards © 2025")
