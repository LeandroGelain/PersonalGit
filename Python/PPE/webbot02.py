import requests
from lxml import html

page = requests.get("https://br.advfn.com/indicadores/taxa-selic/valores-historicos")
tree = html.fromstring(page.content)


for i in range (1,4):
    print ()
    # cont = (str(tree.xpath('//*[@id="section_1"]/table/tbody/tr[1]/td[%i]/text()'%i)))
    for j in range(1,229):
        cont = (str(tree.xpath('//*[@id="section_1"]/table/tbody/tr[%i]/td[%i]/text()'%(j,i))))
        print(cont)

print(cont)

#//*[@id="section_1"]/table/tbody/tr[3]/td[1]
#//*[@id="section_1"]/table/tbody/tr[4]/td[1]
#//*[@id="section_1"]/table/tbody/tr[228]/td[3]