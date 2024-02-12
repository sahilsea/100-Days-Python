import requests

weather_params = {
    "lat" : 24.792480,
    "lon" : 85.007713,
    "appid" :"04760548080bdd546e94b7b36d8f8012"
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params= weather_params)
print(response.status_code)

# response.raise_for_status()

# data = response.json()
# print(data)
