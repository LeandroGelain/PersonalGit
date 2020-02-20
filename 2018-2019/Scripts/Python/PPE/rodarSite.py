#-*- coding: utf-8 -*-
from lxml import html
import requests

#URL do site a coletar os dados
page = requests.get('https://www.agrolink.com.br/agrolinkfito/produto/lista/')
tree = html.fromstring(page.content)

'''a =0 '''
#Linha = 1
produtos = []
precos = []
maringa = []
'''precos_londrina = []
precos_foz = []
precos_cascavel = []
'''	
produtos = tree.xpath('//*[@id="tr_rows"]/td[1]/a/text()')
precos = tree.xpath('//*[@id="tr_rows"]/td[3]/a/text()')
maringa = tree.xpath('//*[@id="tr_rows"]/td[4]/a/text()')


print produtos
print precos
print maringa

