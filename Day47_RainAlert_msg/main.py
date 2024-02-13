import requests
from twilio.rest import Client
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
import os

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

weather_params = {
    "lat" : 24.792480,
    "lon" : 85.007713,
    "appid" : os.environ.get('API_KEY'),
    "cnt" : 4
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params= weather_params)
# print(response.status_code)

response.raise_for_status()

data = response.json()

# for i in range(0, 4):
will_rain = False
if data["list"][0 or 1 or 2 or 3]['weather'][0]['id'] < 700:
    will_rain = True
if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = { 'https': os.environ['http proxy']}
    # client = Client(account_sid, auth_token, http_client = proxy_client)
    client = Client(account_sid, auth_token,)
    message = client.messages \
    .create(
        body = "It is going to rain today, Remember to bring an umberalla☔️",
        from_= "+17622131855",
        to = "+917321843138"
    )
    print(message.status)
    