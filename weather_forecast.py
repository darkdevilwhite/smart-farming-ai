import requests

def get_weather(city):
    api_key = "your_openweather_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    res = requests.get(url).json()
    if res.get("main"):
        temp = res["main"]["temp"] - 273.15
<<<<<<< HEAD
        desc = res["weather"][0]["description"]
        return f"Temperature: {temp:.1f}°C, {desc}"
    else:
        return "City not found or API limit reached"
=======
        weather = res["weather"][0]["description"]
        return f"Temperature: {temp:.2f}°C | Weather: {weather}"
    else:
        return "City not found"
>>>>>>> 7adf10164b4cefe70af37a31b935d9bcc1037ae9
