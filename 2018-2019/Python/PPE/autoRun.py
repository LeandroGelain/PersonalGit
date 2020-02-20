
from lxml import html
import requests
import schedule
import time

def job():
    Novo = open('dados.csv', 'w')
    #URL do site a coletar os dados
    page = requests.get('http://celepar7.pr.gov.br/ceasa/hoje.asp')
    tree = html.fromstring(page.content)
    a =0
    Linha = 3
    produtos = []
    precos_curitiba = []
    precos_maringa = []
    precos_londrina = []
    precos_foz = []
    precos_cascavel = []
    while Linha < 193:
        produtos.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[1]/font/text()' % Linha )))
        precos_curitiba.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[2]/p/font/text()' % Linha )))
        precos_maringa.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[3]/p/font/text()' % Linha)))
        precos_londrina.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[4]/p/font/text()' % Linha)))
        precos_foz.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[5]/p/font/text()' % Linha)))
        precos_cascavel.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[6]/p/font/text()' % Linha)))
        aux = str(Linha) + str(produtos[a]) + str(precos_curitiba[a])  + str(precos_maringa[a]) + str(precos_londrina[a]) + str(precos_foz[a]) + str(precos_cascavel[a]) + "\n"
        Novo.write(aux)
        Linha += 1
        a += 1

schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    pass