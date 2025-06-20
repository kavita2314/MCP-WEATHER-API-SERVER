#from flask import Blueprint, jsonify, render_template
#from weather.weather_utils import get_weather

#weather_bp = Blueprint('weather', __name__)

#API_KEY = "YOUR API"  # Replace with your actual API key
#CITY = "Haldwani,IN"

# ✅ Serve frontend page
#@weather_bp.route('/', methods=['GET'])
#def home():
 #   return render_template('index.html')  # Load HTML page

# ✅ Temperature API
#@weather_bp.route('/temperature', methods=['GET'])
#def temperature():
 #   return jsonify(get_weather(CITY, API_KEY))






from flask import Blueprint, jsonify, render_template, request
from weather.weather_utils import get_weather

weather_bp = Blueprint('weather', __name__)

API_KEY = "47dba9f1bd58f3030bb9b263382ff763" 
 # Replace with your real key

@weather_bp.route('/')
def home():
    return render_template('index.html')

@weather_bp.route('/temperature', methods=['GET'])
def temperature():
    city = request.args.get('city', 'Haldwani,IN')  # Default: Haldwani
    weather_data = get_weather(city, API_KEY)
    return jsonify(weather_data)
