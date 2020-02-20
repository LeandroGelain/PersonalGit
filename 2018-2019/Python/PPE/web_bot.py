import requests
from lxml import html

page = requests.get("http://portaldota2.com.br/listar_herois.php")
tree = html.fromstring(page.content)


# for i in range(1, 5):
#     conteudo = (str(tree.xpath('//*[@id="conteudo18"]/table/tbody/tr[%i]/td[1]/text()'%i)))
#     print(conteudo)
#     for j in range(1,5):
#         conteudo = (str(tree.xpath('//*[@id="conteudo18"]/table/tbody/tr[%i]/td[%i]/text()'%(i,j))))
#         print(conteudo)

conteudo = (str(page.xpath('//*[@id="conteudo18"]/table/tbody/tr[1]/td[2]/text()')))
print(conteudo)

# //*[@id="conteudo18"]/table/tbody/tr[1]/td[2]
# //*[@id="conteudo18"]/table/tbody/tr[4]/td[4]