from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests
from datetime import datetime

app = FastAPI()

API_KEY = "84abc0d847ac429ebad21043251705"
LAT, LON = 18.55, -64.36

def get_weather():
    url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={LAT},{LON}&days=1&aqi=no&alerts=no"
    response = requests.get(url)
    data = response.json()

    location = data['location']['name']
    forecast = data['forecast']['forecastday'][0]['day']
    astro = data['forecast']['forecastday'][0]['astro']

    today = datetime.strptime(data['location']['localtime'], "%Y-%m-%d %H:%M")
    date_str = today.strftime("%A, %B %d, %Y")

    weather_text = f"""📅 Today in BVI: {date_str}

Necker Island Weather Forecast:

| Time       | Rain % & Intensity        | Wind (knots + dir) | Waves     | Temp (°C/°F) | UV Index |
|------------|---------------------------|--------------------|-----------|--------------|----------|
| Morning    | {forecast['daily_chance_of_rain']}% – Showers        | ↘ 13 kt            | SW / 1.3m | {forecast['mintemp_c']}°C / {round(forecast['mintemp_c']*9/5+32)}°F | 🟡 {forecast['uv']}  |
| Afternoon  | {forecast['daily_chance_of_rain']}% – Partly Cloudy  | ↘ 11 kt            | SW / 1.4m | {forecast['avgtemp_c']}°C / {round(forecast['avgtemp_c']*9/5+32)}°F | 🟡 {forecast['uv']}  |
| Evening    | {forecast['daily_chance_of_rain']}% – Cloudy         | → 10 kt            | SW / 1.4m | {forecast['maxtemp_c']}°C / {round(forecast['maxtemp_c']*9/5+32)}°F | ⚪ N/A   |

🌇 Sunset in BVI: {astro['sunset']}

🚩 The Baths 🟡 Yellow Flag (Exercise Caution) — Last update: May 16, 2025, at 07:50 AM (BVI Time)
"""
    return weather_text

@app.get("/goodmorning")
def good_morning():
    try:
        report = get_weather()
        return PlainTextResponse(report)
    except Exception as e:
        return PlainTextResponse(f"Error fetching weather data: {e}")
