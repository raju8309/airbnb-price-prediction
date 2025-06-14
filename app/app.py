# app/app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =========================
# ✅ Custom Professional CSS
# =========================
st.markdown("""
    <style>
        .stApp {
            background-color: #f4f6f8;
            font-family: 'Segoe UI', sans-serif;
        }
        section[data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #dee2e6;
            padding: 2rem 1rem;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        .stMarkdown {
            text-align: center;
            font-size: 1.1rem;
            color: #5c636a;
        }
        .stButton>button {
            background-color: #0069d9;
            color: white;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            border: none;
            font-size: 1rem;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0053aa;
        }
        .stAlert-success {
            background-color: #d1e7dd;
            border: 1px solid #badbcc;
            color: #0f5132;
        }
        .stSlider label {
            font-weight: bold;
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

# =========================
# ✅ Load model and columns
# =========================
model = joblib.load("../models/price_model.pkl")
model_columns = joblib.load("../models/model_columns.pkl")

# =========================
# ✅ Title & Info
# =========================
st.title("🏠 Airbnb Price Prediction App (NYC)")
st.markdown("Use this tool to predict the nightly price of an Airbnb listing in New York City.")

# =========================
# ✅ Sidebar Inputs
# =========================
st.sidebar.header("Enter Listing Details")

room_type = st.sidebar.selectbox("Room Type", ["Private room", "Entire home/apt", "Shared room"])
neighbourhood_group = st.sidebar.selectbox("Neighbourhood Group", ["Brooklyn", "Manhattan", "Queens", "Staten Island", "Bronx"])
latitude = st.sidebar.slider("Latitude", 40.50, 40.95, 40.75)
longitude = st.sidebar.slider("Longitude", -74.25, -73.70, -73.95)
minimum_nights = st.sidebar.slider("Minimum Nights", 1, 30, 3)
number_of_reviews = st.sidebar.slider("Number of Reviews", 0, 300, 10)
reviews_per_month = st.sidebar.slider("Reviews per Month", 0.0, 10.0, 1.0)
availability_365 = st.sidebar.slider("Availability (days/year)", 0, 365, 180)
calculated_host_listings_count = st.sidebar.slider("Host Listing Count", 1, 10, 1)

# =========================
# ✅ Prepare Input Data
# =========================
input_data = {
    'latitude': latitude,
    'longitude': longitude,
    'minimum_nights': minimum_nights,
    'number_of_reviews': number_of_reviews,
    'reviews_per_month': reviews_per_month,
    'calculated_host_listings_count': calculated_host_listings_count,
    'availability_365': availability_365,
    'neighbourhood_group_Brooklyn': 0,
    'neighbourhood_group_Manhattan': 0,
    'neighbourhood_group_Queens': 0,
    'neighbourhood_group_Staten Island': 0,
    'room_type_Private room': 0,
    'room_type_Shared room': 0
}

if neighbourhood_group != 'Bronx':
    input_data[f'neighbourhood_group_{neighbourhood_group}'] = 1

if room_type != 'Entire home/apt':
    input_data[f'room_type_{room_type}'] = 1

input_df = pd.DataFrame([input_data], columns=model_columns)
input_df = input_df.fillna(0)

# =========================
# ✅ Prediction Output
# =========================
if st.button("Predict Price 💰"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price: **${prediction:.2f} per night**")
