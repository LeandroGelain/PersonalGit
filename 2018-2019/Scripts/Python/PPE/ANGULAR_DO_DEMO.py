import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup 

pagina = webdriver.Chrome(executable_path=r'C:\Users\leand\Documents\selenium\chromedriver.exe') 

while True:
    pagina.get("https://www.instagram.com/seguros_martins/")
    time.sleep(2)
    seguidores = pagina.find_elements_by_css_selector(".g47SY ")
    dados = (seguidores[1])
    print(dados.text)
    time.sleep(5)
    pagina.refresh()