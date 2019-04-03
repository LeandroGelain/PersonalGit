import requests
from lxml import html
from bs4 import BeautifulSoup

page = requests.get("https://www.youtube.com/results?search_query=fatec")

tree = html.fromstring(page.content)

bsObj = BeautifulSoup(page.text, "lxml")

titulo = bsObj.findAll("a", {"class":"yt-uix-tile-link"})

for i in titulo:
    print(i['title']+"\nyoutube.com"+i['href'])