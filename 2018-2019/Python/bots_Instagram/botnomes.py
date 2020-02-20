import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup 
import matplotlib as mlp
import numpy as np
from datetime import datetime

class taxaAcerto():
    
    def __init__():
        return "/Inicialize Bot."
    
    def nomesInstagram():
        pagina = webdriver.Chrome(executable_path=r'C:\Users\leand\Documents\Leandro\PythonOuData\Pythonchromedriver.exe') 
        while True:
            now = datetime.now()
            pagina.get("https://www.instagram.com/seguros_martins/")
            time.sleep(2)
            seguidores = pagina.find_elements_by_css_selector(".g47SY ")
            dados = (seguidores[1])
            ano = now.year
            mes= now.month
            dia= now.day
            hora = now.hour
            minutos = now.minute
            segundos = now.second
            horario =(hora+":"+minutos+":"+segundos)
            
            print(dados.text + "-"+ dia )
            
            time.sleep(60)
            pagina.refresh()

    def gerarGrafico():
        dadosSeguidores = taxaAcerto.nomesInstagram()


dados = taxaAcerto.nomesInstagram()
print(dados)