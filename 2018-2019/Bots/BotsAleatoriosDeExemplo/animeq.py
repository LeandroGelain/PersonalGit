import requests
from bs4 import BeautifulSoup
from lxml import html

url = requests.get('https://animeq.xpg.com.br/anime-legendado-letra-0-9')
print(url)
soup = BeautifulSoup(url.content, 'lxml')

for tagA in soup.findAll('a', href=True):
    print(tagA.text)
    print(tagA['href'])