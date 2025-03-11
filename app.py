import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("rf_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define the Streamlit app
st.title("Water Quality Prediction")
st.write("Enter the water sample parameters to predict potability (0 = Not Potable, 1 = Potable)")

# Input fields
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, step=0.1)
Hardness = st.number_input("Hardness", min_value=0.0)
Solids = st.number_input("Solids (ppm)", min_value=0.0)
Chloramines = st.number_input("Chloramines", min_value=0.0)
Sulfate = st.number_input("Sulfate", min_value=0.0)
Conductivity = st.number_input("Conductivity", min_value=0.0)
Organic_carbon = st.number_input("Organic Carbon", min_value=0.0)
Trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0)
Turbidity = st.number_input("Turbidity", min_value=0.0)

# Predict button
if st.button("Predict Water Quality"):
    # Prepare input for model
    input_data = np.array([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
    prediction = model.predict(input_data)[0]
    
    # Display result
    if prediction == 1:
        st.success("The water is Potable (Safe to Drink).")
    else:
        st.error("The water is Not Potable (Unsafe to Drink).")
