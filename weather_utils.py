import requests

def get_weather(CITY, API_KEY):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("main"):
        return {
            "city": CITY,
            "temperature_celsius": data["main"]["temp"]
        }
    else:
        return {"error": "Unable to fetch weather data"}
