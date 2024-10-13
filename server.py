from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Зберігаємо поточні дані про погоду
weather_data = {
    "precipitation": "відсутні",  # тип опадів
    "day_type": "сонячний",       # тип дня
    "wind_speed": 0.0,            # швидкість вітру
    "temperature": 20.0,          # температура (в градусах Цельсія)
    "humidity": 50                # вологість (у %)
}

@app.route('/update', methods=['POST'])
def update_weather():
    global weather_data
    data = request.json
    weather_data['precipitation'] = data.get('precipitation', weather_data['precipitation'])
    weather_data['day_type'] = data.get('day_type', weather_data['day_type'])
    weather_data['wind_speed'] = data.get('wind_speed', weather_data['wind_speed'])
    weather_data['temperature'] = data.get('temperature', weather_data['temperature'])
    weather_data['humidity'] = data.get('humidity', weather_data['humidity'])
    return jsonify({"status": "success"}), 200

@app.route('/current_weather', methods=['GET'])
def get_weather():
    return jsonify(weather_data), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

