import requests

data = {
   "precipitation": 3.2,
   "temp_max": 8,
   "temp_min": 2,
   "wind": 4.5
}

response = requests.post("http://127.0.0.1:5000/predict", json=data)
print(response.json())
