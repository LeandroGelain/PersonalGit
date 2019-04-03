#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from lxml import html
import requests

url = requests.get('https://br.advfn.com/indicadores/taxa-selic/valores-historicos')
cont = html.fromstring(url.content)
page = BeautifulSoup(cont.text, "lxml")

for conteudo in page:
    bsObjs = conteudo.find_all['div', {'class':'even'}]
    print(bsObjs['tr'])

for conteudo2 in page:
    bsobjs2 = conteudo2.find_all['div', {'class': 'odd'}]
    print(bsobjs2['tr'])