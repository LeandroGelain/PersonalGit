from bs4 import BeautifulSoup
import requests
import csv

arquivo = open('listadetagsA.txt','a+')
url = (requests.get('https://www.facebook.com/leandro.gelain.3/friends'))
soup = BeautifulSoup(url.text, 'lxml')
 
for div in soup.find_all("div"):
    for name in div.findAll('a'):
        print(name)
        arquivo.write(str(name))

arquivo.close()
# for friends in soup.findAll("li",{"class":"_698"}):
#     print (friends.text())
# print (soup)
