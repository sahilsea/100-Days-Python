import requests


response = requests.get(url="https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
response.raise_for_status()
data = response.json()

# print(data['results'])

question_data = data['results']
