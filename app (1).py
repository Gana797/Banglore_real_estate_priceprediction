import streamlit as st
import pickle
import numpy as np

# Load the model
with open('real_estate_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏠 Real Estate Price Prediction")

# Input fields
sqft = st.number_input('Total Square Feet', min_value=0)
bhk = st.number_input('Number of BHKs', min_value=0)
bath = st.number_input('Number of Bathrooms', min_value=0)
location_code = st.number_input('Location Code (or 0)', min_value=0)

# Predict button
if st.button("Predict Price"):
    features = np.array([[sqft, bhk, bath, location_code]])
    prediction = model.predict(features)
    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")
