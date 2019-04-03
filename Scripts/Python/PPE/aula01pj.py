#
import requests
from lxml import html
import csv
page = 0
contp = 1
linha = 0 
while contp < 15:
    page = requests.get("http://cotacoes.economia.uol.com.br/bolsas/cotacoes-historicas.html?indice=.BVSP&beginDay=1&beginMonth=1&beginYear=2006&endDay=1&endMonth=1&endYear=2018&page=[%d]&size=200" % contp)
    tree = html.fromstring(page.content)
    contador = 2
    contp += 1
    while linha < 199:
        data =      (str(tree.xpath('//*[@id="tblInterday"]/tbody/tr[%d]/td[1]/text()'% contador)))
        cotacao =   (str(tree.xpath('//*[@id="tblInterday"]/tbody/tr[%d]/td[2]/text()'% contador)))
        minima =    (str(tree.xpath('//*[@id="tblInterday"]/tbody/tr[%d]/td[3]/text()'% contador)))
        maxima =    (str(tree.xpath('//*[@id="tblInterday"]/tbody/tr[%d]/td[4]/text()'% contador)))
        variacao =  (str(tree.xpath('//*[@id="tblInterday"]/tbody/tr[%d]/td[5]/text()'% contador)))
        variacaop = (str(tree.xpath('//*[@id="tblInterday"]/tbody/tr[%d]/td[6]/text()'% contador)))
        volume =    (str(tree.xpath('//*[@id="tblInterday"]/tbody/tr[%d]/td[7]/text()'% contador)))
        
        inserir = data + " " + cotacao + " " + minima + " " + maxima + " " + variacao + " " + variacaop + " " + volume
        inserir = inserir.replace('\\xa0', '')
        inserir = inserir.replace('%','')
        
        print(inserir)
        
        linha = linha + 1
        contador = contador + 1