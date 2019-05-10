from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import requests
import time
import random
import json
import mongoConnect

def findAllCompanies():
    # driver.get('http://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm')
    conexão, mydb = mongoConnect.connect()
    cursor = mydb['WorkClusterFree']
    arrayLinks = []
    arrayEmpresas = []
    subXpath= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Z','5']
    for i in range(0,5):
    # for i in range(0,len(subXpath)):
        url = requests.get('http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?Letra='+str(subXpath[i])+'&idioma=pt-br')
        # time.sleep(4)
        
        pageContent = BeautifulSoup(url.content, 'lxml')
        for tagA in pageContent.find_all('a', href=True):
            nomeEmpresa = (tagA.text)
            LinkEmpresa = (tagA['href'])
            if not 'http://www.b3.com.br/' in LinkEmpresa:
                arrayLinks.append(LinkEmpresa)
                arrayEmpresas.append(nomeEmpresa)
                print(tagA['href'] + ' ; '+tagA.text)
        
    # for insert in range(0,len(arrayLinks)):
    #     print('Inseridos banco: '+str(insert+1))
    #     mydb.empresas_link_b3.insert_one({
    #         "nome_empresa": arrayEmpresas[insert] , "link_b3_empresa": arrayLinks[insert]
    #     })

    # driver.close()
    
findAllCompanies()

# linkBase na segunda pesquisa = http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/