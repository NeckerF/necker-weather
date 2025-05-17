from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def root():
    return PlainTextResponse("OK")

@app.get("/goodmorning")
def good_morning():
    return PlainTextResponse("""
📅 Today in BVI: Saturday, May 17, 2025

| Time       | Rain % & Intensity            | Wind (knots + dir) | Waves (dir/m/s)     | Temp (°C/°F) | UV Index |
|------------|-------------------------------|--------------------|---------------------|--------------|----------|
| Morning    | 🌧 60% – Heavy T-storms        | ↘ 13 kt            | SW / 1.3m / 12s     | 27°C / 81°F  | 🟡 High  |
| Afternoon  | 🌦 30% – Light Showers         | ↘ 11 kt            | SW / 1.4m / 16s     | 29°C / 84°F  | 🟡 High  |
| Evening    | 🌧 40% – Scattered Showers     | → 10 kt            | SW / 1.4m / 18s     | 26°C / 79°F  | ⚪ N/A   |

🌇 Sunset in BVI: 6:45 PM (AST)

The Baths 🟡 Yellow Flag (Exercise Caution) — Last update: May 16, 2025, at 07:50 AM (BVI Time)

Schedule for Today — "Future of Work":

- 6:30 AM – Boat transfer from MSK to NKR
- 7:00 AM – Yoga + Meditation (GH)
- 7:00 AM – Breakfast (GH Roof Terrace)
- 8:00 AM – Island walk + Unite BVI arrival
- 9:00 AM – Programming begins
- 10:15 AM – Break
- 10:30 AM – Resume sessions
- 1:00 PM – Lunch (Eastern Med Menu)
- 2:00 PM – Lemur Feeding / Transfers
- 3:30 PM – Tennis + Tea
- 6:00 PM – Cocktails
- 6:15 PM – Q&A with Richard
- 7:00 PM – Dinner (Scarlet Night)
- 9:00 PM – Boat Transfer
""")
