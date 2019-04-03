from bs4 import BeautifulSoup

import requests

r  = requests.get("Inserir url aqui")

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
