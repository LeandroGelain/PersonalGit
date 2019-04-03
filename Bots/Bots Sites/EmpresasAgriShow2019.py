import requests
import json
from bs4 import BeautifulSoup
from lxml import html
import csv

VetorEmails=[]
VetorSites=[]
nomeEmpresa=[]

url = (requests.get('http://www.camaras.org.br/site.aspx/Associadas-da-CSMIA'))
soup = BeautifulSoup(url.text, 'lxml')

def remove_repetidos(VetorSites):
    l = []
    for i in VetorSites:
        if i not in l:
            l.append(i)
    l.sort()
    return l

for conteudo in soup.find_all('div','conteudo-html'):
	for nomeEmpresas in conteudo.find_all('div'):
		for x in nomeEmpresas.find_all('a'):
			if 'http' in x.text:
				contsite = VetorSites.append(x.text)

lista = remove_repetidos(VetorSites)			
print(lista)


		# print(len(VetorSites))
		# 	elif '@' in conteudo:
		# 		conteudo = email
			
		# 	else:
		# 		nomeEmpresa = conteudo
		# # print(VetorSites)
		# print(str(site) + ' ; '+ str(email)+' ; ')