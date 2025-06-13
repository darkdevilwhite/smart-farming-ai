# Trigger Streamlit redeploy
import streamlit as st
import pandas as pd
import pickle
from weather_forecast import get_weather  # ✅ Correct import

# Load model
try:
    with open("crop_price_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Make sure 'crop_price_model.pkl' is in the project root.")
    st.stop()

st.title("🚜 Smart Tractor Rental & Crop Price Forecast")

menu = st.sidebar.radio("Select", ["Crop Price Prediction", "Find Tractor", "Weather Forecast"])

if menu == "Crop Price Prediction":
    st.subheader("Predict Crop Price")
    crop = st.selectbox("Crop", ["Wheat", "Rice", "Maize"])
    region = st.selectbox("Region", [101, 102, 103])
    doy = st.slider("Day of Year", 1, 366)
    rainfall = st.slider("Rainfall (mm)", 0, 200)

    df_input = pd.DataFrame(
        [[crop, region, doy, rainfall]],
        columns=["crop_type", "region_code", "day_of_year", "rainfall_mm"]
    )
    df_input = pd.get_dummies(df_input)

    features = model.feature_names_in_
    for feat in features:
        if feat not in df_input.columns:
            df_input[feat] = 0
    df_input = df_input[features]

    pred_price = model.predict(df_input)[0]
    st.success(f"Estimated Crop Price: ₹{pred_price:.2f}")

elif menu == "Find Tractor":
    st.subheader("Available Tractors Near You")
    try:
        tractors = pd.read_csv("tractor_data.csv")
        st.map(tractors[["latitude", "longitude"]])
        st.dataframe(tractors)
    except FileNotFoundError:
        st.error("Tractor data not found. Make sure 'tractor_data.csv' is in the project root.")

elif menu == "Weather Forecast":
    st.subheader("Weather for Your Location")
    city = st.text_input("Enter City", "Hyderabad")
 HEAD
    forecast = get_weather(city)
    if forecast:
        st.write(forecast)
# Force redeploy on Streamlit
    st.write(get_weather(city))
 f1e8d30 (Add GitHub Actions workflow for deployment)
