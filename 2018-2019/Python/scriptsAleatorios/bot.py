#coding ~utf-8~
import requests
from bs4 import BeautifulSoup
from lxml import html

page = requests.get("http://blog.dota2.com/")
tree = html.fromstring(page.content)

bsObj = BeautifulSoup(page.text, "lxml")

conteudo = bsObj.findAll("a", {"rel":"bookmark"})

for i in conteudo:
    print(i["title"])