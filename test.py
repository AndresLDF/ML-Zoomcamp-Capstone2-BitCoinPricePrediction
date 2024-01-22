import requests
import json

url = 'http://localhost:9696/predict'

data = {
    "open": 39891.00,
    "volume_btc": 388.639180,
    "volume_eur": 1.549699e+07,
    "7_days_a": -123.11,
    "30_days_a": 235.62,
    "90_days_a": 183.82,
}

response = requests.post(url, json=data).json()

print(json.dumps(response, indent=1))