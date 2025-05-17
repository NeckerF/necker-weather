from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from datetime import datetime

app = FastAPI()

@app.get("/goodmorning")
def good_morning():
    today = datetime.utcnow().strftime("%A, %B %d, %Y")

    forecast = f"""📅 Today in BVI: {today}

Necker Island Weather Forecast:

| Time       | Rain % & Intensity            | Wind (knots + dir) | Waves (dir/m/s)     | Temp (°C/°F) | UV Index |
|------------|-------------------------------|--------------------|---------------------|--------------|----------|
| Morning    | 🌧 60% – Heavy T-storms        | ↘ 13 kt            | SW / 1.3m / 12s     | 27°C / 81°F  | 🟡 High  |
| Afternoon  | 🌦 30% – Light Showers         | ↘ 11 kt            | SW / 1.4m / 16s     | 29°C / 84°F  | 🟡 High  |
| Evening    | 🌧 40% – Scattered Showers     | → 10 kt            | SW / 1.4m / 18s     | 26°C / 79°F  | ⚪ N/A   |

🌇 Sunset in BVI: 6:45 PM (AST)

🚩 The Baths 🟡 Yellow Flag (Exercise Caution) — Last update: May 16, 2025, at 07:50 AM (BVI Time)
"""
    return PlainTextResponse(forecast)
