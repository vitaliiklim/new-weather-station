import requests
import random
import time

url = 'http://localhost:5000/update'

precipitation_types = ['дощ', 'сніг', 'град', 'відсутні', 'зливи', 'мряка']
day_types = ['сонячний', 'хмарний', 'туман', 'дощовий']

while True:
    data = {
        "precipitation": random.choice(precipitation_types),
        "day_type": random.choice(day_types),
        "wind_speed": round(random.uniform(0, 15), 2),  # Швидкість вітру від 0 до 15 м/с
        "temperature": round(random.uniform(-10, 35), 1),  # Температура від -10 до 35 градусів
        "humidity": random.randint(0, 100)  # Вологість від 0% до 100%
    }
    response = requests.post(url, json=data)
    print(f"Sent data: {data}, Response: {response.status_code}")
    time.sleep(5)  # Відправляємо дані кожні 5 секунд

