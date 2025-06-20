# MCP-WEATHER-API-SERVER
# 🌤️ MCP Weather API Server – India Edition 🇮🇳

A modular Flask application that provides the **current temperature of any Indian city** using the OpenWeatherMap API. Built for learning, showcasing Flask APIs, and frontend-backend interaction.

> 🔗 [GitHub Repo](https://github.com/kavita2314/MCP-WEATHER-API-SERVER)

---

## 📌 Features

- 🔍 Search any Indian city (like Delhi, Mumbai, Haldwani)
- 🌡️ Displays real-time temperature using OpenWeatherMap API
- ⚙️ Modular Python structure using Flask Blueprints
- 🎨 Clean frontend with HTML, CSS, and JavaScript
- ⚠️ Error messages for invalid city names

---

## 📁 Project Structure
MCP-WEATHER-API-SERVER/
├── main.py # App entry point
├── templates/
│ └── index.html # Frontend UI
├── weather/
│ ├── weather_server.py # Flask routes (Blueprint)
│ └── weather_utils.py # Weather-fetching logic
└── requirements.txt


---

## 🧠 How It Works

1. User opens the app in the browser
2. Types an Indian city name (like "Lucknow")
3. App sends a GET request to `/temperature?city=Lucknow`
4. Backend fetches temperature using OpenWeatherMap API
5. Temperature is shown on the screen

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/kavita2314/MCP-WEATHER-API-SERVER.git
cd MCP-WEATHER-API-SERVER

## 2 . Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # For Windows

## 3. Install Requirements
pip install -r requirements.txt

## 4. Add Your API Key
Open weather/weather_server.py and replace:
API_KEY = "your_actual_api_key_here"

Run the App
python main.py
Then open your browser and go to:
http://127.0.0.1:5000



Sample Output
Searching for Mumbai gives:
🌡️ Temperature in Mumbai is 31°C
Searching for Tokyo returns:
❌ City 'Tokyo' not found in India.
