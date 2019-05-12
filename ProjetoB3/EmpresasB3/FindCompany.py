from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import requests
import time
import random
import json
import re
import mongoConnect

def mongoConection():
    conexão, mydb = mongoConnect.connect()
    cursor = mydb['empresas_link_b3']
    return cursor

def findAllCompanies():
    # driver.get('http://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm')
    cursor = mongoConection()
    arrayLinks = []
    arrayEmpresas = []
    subXpath= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Z','5']
    for i in range(0,len(subXpath)):
        url = requests.get('http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?Letra='+str(subXpath[i])+'&idioma=pt-br')        
        pageContent = BeautifulSoup(url.content, 'lxml')
        for tagA in pageContent.find_all('a', href=True):
            nomeEmpresa = (tagA.text)
            LinkEmpresa = (tagA['href'])
            if not 'http://www.b3.com.br/' in LinkEmpresa:
                arrayLinks.append(LinkEmpresa)
                arrayEmpresas.append(nomeEmpresa)
                print(tagA['href'] + ' ; '+tagA.text)
        
    for insert in range(0,len(arrayLinks)):
        print('Inseridos banco: '+str(insert+1))
        mydb.empresas_link_b3.insert_one({
            "nome_empresa": arrayEmpresas[insert] , "link_b3_empresa": arrayLinks[insert]
        })

# linkBase na segunda pesquisa = http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/
def find_details_in_all_companies():
    url = ('http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/')
    cursor = mongoConection()
    ConcLinks = []
    for links in cursor.find():
        link = (links['link_b3_empresa'])
        ConcLinks.append(link)
        # print(link)
    for i in range(0, 1):
        linkSplit = (ConcLinks[1])
        link = linkSplit.split('=')
        codigo = (link[1])
        listTD = []
        url = requests.get('http://bvmf.bmfbovespa.com.br/pt-br/mercados/acoes/empresas/ExecutaAcaoConsultaInfoEmp.asp?CodCVM='+str(codigo)+'&ViewDoc=1&AnoDoc=2019&VersaoDoc=1&NumSeqDoc=80335')
        pageContent = BeautifulSoup(url.content, 'lxml')                                  
        # print(pageContent)
        for tbody in pageContent.findAll('div',{'class':'content active'}):
            # print(tbody)
            for tr in tbody.findAll('tr'):
                tr = (tr.text)
                print(tr)
                listTD.append(tr)
                print('-=============================-')
        # p = (listTD[0].text)
        # p = p.split(':')
        # p = str(p)
        # p = p.replace('\n','')
        # p = re.sub('A','',p)
        # print(p)
find_details_in_all_companies()