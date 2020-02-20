#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import html
import requests
from bs4 import BeautifulSoup
import csv

arquivo = open('roupasMasculinas.csv', 'a+')
cont= 1
while cont < 981:
    url = (requests.get('https://www.dafiti.com.br/roupas-masculinas/?cat-pwa=0&campwa=0&page=%d'%cont))
    print(str(cont) +'/981')
    soup = BeautifulSoup(url.text, 'lxml')
    for box in soup.find_all('div', 'product-box-detail'):
        print('=======================================')
       
        for x in box.find_all('p', 'product-box-title hide-mobile'):
            item = (str(x.text))
            px =("Produto"+item)
            csvpx= (item+';')
            print(px)
            arquivo.write(csvpx)
        
        for y in box.find_all('span', 'product-box-price-to'):
            precoP = (str(y.text))
            if (precoP != 0) and (precoP != '') and (precoP != False): 
                py = ("Preço com desconto = "+precoP)
                csvpy = (precoP+';')
                print(py)
                arquivo.write(csvpy)
            else:
                resp = ("0;")
                print(resp)
                arquivo.write(resp)
        
        for z in box.find_all('span', 'product-box-price-from'):
            precoR = (str(z.text))
            if (precoR != 0) and (precoR != '') and (precoR != False):
                pz = (precoR)
                csvpz = (precoR+';\n')
                print(pz)
                arquivo.write(csvpz)
            else:
                resposta = ("0;\n")
                print(resposta)
                arquivo.write(resposta)
    cont+=1
arquivo.close()