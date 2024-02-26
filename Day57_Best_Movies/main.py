from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
hkkr_webpage = response.text

soup = BeautifulSoup(hkkr_webpage, "html.parser")
# anch_title = soup.select(name="span", class_= "titleline")
# print(soup.prettify())
# print(soup.title.string)
# print(soup.select_one(selector= "span a"))


all_article = soup.select(selector='.titleline a')
# print(all_article)
all_votes = soup.find_all(name="span", class_='score')
texts = []
links = []
votes_ = []

for tag in all_article:
    tag_text = (tag.getText())
    texts.append(tag_text)
    tag_link = (tag.get("href"))
    links.append(tag_link)


for votes in all_votes:
    votes = int((votes.getText()).split()[0])
    votes_.append(votes)

largest_vote = max(votes_)
print(largest_vote)
# for title in anch_title:
    # print(title)  


# print(f'Max Votes: {max_vote}\n Web Texts: {texts}\n Web links: {links} Votes:{votes_}')


































# print(votes_)

# largest_vote = max(votes_)
# print(largest_vote)
# for title in anch_title:
#     print(title)

# for tag in soup.find_all("a"):
#     print(tag.get('href'))

# print(soup.getText)