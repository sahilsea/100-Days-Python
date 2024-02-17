import requests
from datetime import datetime as dt

current_day = dt.now()
day = current_day.day
month = current_day.month
year = current_day.year
print(year)

Habit_track_APIENDPOINT = "https://pixe.la/v1/users"
USERNAME = 'sahilsea12'
TOKEN = 'kfslfkslfjsljeirr'

paramss = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
paramss_ad = {
    'id' : 'Graph4sahil3@',
    'name' : 'Graph4sahil3',
    'unit' : 'km',
    'type' : 'int',
    "color": 'sora',
    # 'data': f'{year}{month}{day}',
    # 'quantity': '5'

}
headers = {
    "X-USER-TOKEN" : TOKEN
}
data = requests.post(url= Habit_track_APIENDPOINT, json= paramss)
data2 = requests.post(url= f"{Habit_track_APIENDPOINT}/USERNAME/graphs",headers= headers,json= paramss_ad)
print(data2)
