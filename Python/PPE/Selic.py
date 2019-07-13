#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import csv
from lxml import html

novo = open("selic_historica.csv", 'a+')
page = requests.get("https://br.advfn.com/indicadores/taxa-selic/valores-historicos")
tree = html.fromstring(page.content)
Linha = 0
contador = 2

while Linha < 219:
    data = (str(tree.xpath('//*[@id="section_1"]/table/tbody/tr[%d]/td[1]/text()' % contador)))
    Vigencia = (str(tree.xpath('//*[@id="section_1"]/table/tbody/tr[%d]/td[2]/text()' % contador)))
    taxa=(str(tree.xpath('//*[@id="section_1"]/table/tbody/tr[%d]/td[3]/text()' % contador)))
    inserir = data + " ; " + Vigencia + " ; " + taxa +  ";\n"
    inserir = inserir.replace('\\xa0', '')
    inserir = inserir.replace("%","")
    
    novo.write(inserir)
    print (inserir)
    Linha = Linha+1
    contador = contador + 1
novo.close()