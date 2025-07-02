import requests

url = "http://127.0.0.1:5000/create_ride"
headers = {
    "Content-Type": "application/json"
}
data = {
    "rider_id": 1,
    "pickup_lat": 19.1,
    "pickup_lng": 72.85,
    "drop_lat": 19.2,
    "drop_lng": 72.95
}

response = requests.post(url, json=data, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
