import requests

def get_weather(city="Hyderabad"):
 HEAD
    api_key = "cf9614f54438cc6bb359d40a1892b64b"
=======
    api_key = "cf9614f54438cc6bb359d40a1892b64b"  # ✅ Your API key
 f1e8d30 (Add GitHub Actions workflow for deployment)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return f"Weather data not found for {city}"

        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"{city} Weather: {weather}, {temperature}°C"
    except Exception as e:
        return f"Error retrieving weather data: {str(e)}"
 HEAD
=======
ssss
 f1e8d30 (Add GitHub Actions workflow for deployment)
