from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
hkkr_webpage = response.text

soup = BeautifulSoup(hkkr_webpage, "html.parser")
anch_title = soup.select("span", class_= "titleline")
print(soup.prettify())
# for title in anch_title:
#     print(title)

# for tag in soup.find_all("a"):
#     print(tag.get('href'))

# print(soup.getText)