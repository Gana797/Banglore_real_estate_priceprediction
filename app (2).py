import streamlit as st
import pickle
import numpy as np

# Load model
with open('real_estate_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load column metadata
with open('columns.pkl', 'rb') as f:
    data = pickle.load(f)
    columns = data['columns']
    locations = data['locations']

st.title("🏠 Real Estate Price Prediction")

sqft = st.number_input("Total Square Feet", min_value=100)
bath = st.number_input("Number of Bathrooms", min_value=1)
bhk = st.number_input("Number of BHKs", min_value=1)
location = st.selectbox("Location", locations)

def predict_price(location, sqft, bath, bhk):
    x = np.zeros(len(columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    try:
        loc_index = columns.index(location.lower())
        x[loc_index] = 1
    except:
        pass
    return model.predict([x])[0]

if st.button("Predict"):
    output = predict_price(location, sqft, bath, bhk)
    st.success(f"💰 Estimated Price: ₹ {output:,.2f}")

