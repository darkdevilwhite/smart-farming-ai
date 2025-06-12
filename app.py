import streamlit as st
import pandas as pd
import pickle
from weather_forecast import get_weather  # ✅ Correct import

# Load model
try:
    with open("app/crop_price_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Make sure 'crop_price_model.pkl' is in 'app/' folder.")
    st.stop()

st.title("🚜 Smart Tractor Rental & Crop Price Forecast")

menu = st.sidebar.radio("Select", ["Crop Price Prediction", "Find Tractor", "Weather Forecast"])

if menu == "Crop Price Prediction":
    st.subheader("Predict Crop Price")
    crop = st.selectbox("Crop", ["Wheat", "Rice", "Maize"])
    region = st.selectbox("Region", [101, 102, 103])
    doy = st.slider("Day of Year", 1, 366)
    rainfall = st.slider("Rainfall (mm)", 0, 200)

    data = pd.DataFrame([[crop, region, doy, rainfall]], columns=["crop_type", "region_code", "day_of_year", "rainfall_mm"])
    data = pd.get_dummies(data)

    model_features = model.feature_names_in_
    for col in model_features:
        if col not in data.columns:
            data[col] = 0
    data = data[model_features]

    pred = model.predict(data)[0]
    st.success(f"Estimated Crop Price: ₹{round(pred, 2)}")

elif menu == "Find Tractor":
    st.subheader("Available Tractors Near You")
    try:
        df = pd.read_csv("app/tractor_data.csv")
        st.map(df[['latitude', 'longitude']])
        st.dataframe(df)
    except FileNotFoundError:
        st.error("Tractor data not found.")

elif menu == "Weather Forecast":
    st.subheader("Weather for Your Location")
    city = st.text_input("Enter City", "Hyderabad")
    forecast = get_weather(city)
    if forecast:
        st.write(forecast)
