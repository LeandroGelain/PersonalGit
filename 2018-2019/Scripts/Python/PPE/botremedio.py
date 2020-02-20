import requests
from lxml import html
import csv

page = requests.get("http://www.medicamentos.med.br/index.asp")
tree = html.fromstring(page.content)

contador = 2
linha = 0

remedio = []
preço = []

while linha < 31:

    remedio = (str(tree.xpath('//*[@id="listSearchResult"]/table/tbody/tr[%d]/td[1]/a/text()' % contador)))
    preço = (str(tree.xpath('//*[@id="listSearchResult"]/table/tbody/tr[%d]/td[3]/text()'% contador)))

    insert = remedio + " ; " + preço
    insert = insert.replace('\\xa0', '').replace("['","")
    insert = insert.replace('%', '').replace("']","")
    print(insert)

    linha += 1
    contador = contador + 1


