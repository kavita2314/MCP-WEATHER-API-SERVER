from flask import Flask
from weather.weather_server import weather_bp  # import blueprint

app = Flask(__name__)
app.register_blueprint(weather_bp)

if __name__ == '__main__':
    app.run(debug=True)
