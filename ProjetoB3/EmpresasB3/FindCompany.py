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

def TirarRepetidosMongo():
    cursor = mongoConection()
    array= []
    arrayTratado = []
    for content in cursor.find():
        array.append(content['link_b3_empresa']) 
    for i in range(0,len(array)):
        if array[i] == (array[i-1]):
            pass
        else:
            arrayTratado.append(array[i])
    return list(arrayTratado)

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
    
    ConcLinks = TirarRepetidosMongo()
    for i in range(0, 3):
        linkSplit = (ConcLinks[i])
        link = linkSplit.split('=')
        codigo = (link[1])
        ArrayTDs = []
        url = requests.get('http://bvmf.bmfbovespa.com.br/pt-br/mercados/acoes/empresas/ExecutaAcaoConsultaInfoEmp.asp?CodCVM='+str(codigo)+'&ViewDoc=1&AnoDoc=2019&VersaoDoc=1&NumSeqDoc=80335')
        pageContent = BeautifulSoup(url.content, 'lxml')                                  
        # print(pageContent)
        for tbody in pageContent.findAll('div',{'class':'content active'}):
            # print(tbody)
            arrayCodBolsa = []
            for codigoBolsa in tbody.findAll('a'):
                conteudoCodigo = (codigoBolsa.text)
                conteudoCodigo = conteudoCodigo.split('\\n')
                arrayCodBolsa.append(conteudoCodigo)
                
            print('Códigos de Negociação: %s'%(arrayCodBolsa[1]))
            
            for td in tbody.findAll('td'):
                td = (td.text)
                ArrayTDs.append(td)
                # print('-=============================-') 

        # quit()
        pInfos = [1, 5,11]
        for i in range(0,len(pInfos)):
            if i == 0:
                print('Nome de Pregão: %s'%(ArrayTDs[pInfos[i]]))
               
            elif i == 1:
                print('CNPJ: %s'% (ArrayTDs[pInfos[i]]))
            elif i == 2:
                print('Site: %s'%(ArrayTDs[pInfos[i]]))
        
        print('+===========')  
                
find_details_in_all_companies()
# TirarRepetidosMongo()