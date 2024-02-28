import requests
from bs4 import BeautifulSoup

time = input("Which year do you want to travel to , type the date in this formate YYYY-MM-DD :  ")
response = requests.get(url=f'https://www.billboard.com/charts/hot-100/{time}/')
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
print(soup.find(name = 'h3', id="title-of-a-story"))  


