import requests
import streamlit as st
from datetime import datetime

api_key = "cf9614f54438cc6bb359d40a1892b64b"

def get_weather(city):
    """
    Get weather data for a given city
    """
    try:
        # OpenWeatherMap API endpoint
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        # Make API request
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            return {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon']
            }
        else:
            return None
            
    except Exception as e:
        st.error(f"Error fetching weather data: {str(e)}")
        return None

def get_forecast(city):
    """
    Get 5-day weather forecast for a given city
    """
    try:
        # OpenWeatherMap 5-day forecast API endpoint
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        
        # Make API request
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            forecast_list = []
            for item in data['list']:
                forecast_list.append({
                    'datetime': datetime.fromtimestamp(item['dt']),
                    'temperature': item['main']['temp'],
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon']
                })
            return forecast_list
        else:
            return None
            
    except Exception as e:
        st.error(f"Error fetching forecast data: {str(e)}")
        return None