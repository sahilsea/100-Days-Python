import requests 
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

Movies_webpage = response.text

soup = BeautifulSoup(Movies_webpage,"html.parser" )

all_title = soup.find_all(name= "h3", class_= 'title')
title_ls = []
for title in all_title:
    i_title = title.getText()
    title_ls.append(i_title)
    title_ls.append("\n")

print(title_ls )
# print("\n")

with open('titles.txt' , 'w') as file:
    file.writelines(title_ls)
    file.write('\n')
