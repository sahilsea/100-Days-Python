from requests import get

parameters = {
    'lat': 24.786238,
    'lng': 85.018988,
    'formatted': 1
}

response = get("https://api.sunrise-sunset.org/json", params= parameters)
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(f"Sunrise : {sunrise} \n Sunset : {sunset}")


