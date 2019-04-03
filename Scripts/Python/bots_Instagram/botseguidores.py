import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup 
import matplotlib as mlp
import numpy as np
from datetime import datetime

class Instagram():
    
    def __init__():
        return "/Inicialize Bot."
    
    def seguidores():
        while True:
            pagina = webdriver.Chrome(executable_path=r'C:\Users\leand\Documents\selenium\chromedriver.exe') 
            web = pagina.get("https://www.instagram.com/seguros_martins/")
            time.sleep(2)
            if web == True:
                seguidores = pagina.find_elements_by_css_selector(".g47SY ")
                dados = (seguidores[1])
                numero = (dados.text)

                time.sleep(5)
                pagina.refresh()
        
                return numero
            # now = datetime.now()
            
            # ano = str(now.year)
            # mes= str(now.month)
            # dia= str(now.day)
            # hora = str(now.hour)
            # minutos = str(now.minute)
            # segundos = str(now.second)
            # horario =str(hora+":"+minutos+":"+segundos)
            # data = str(dia+"/"+mes+"/"+ano)
            
            # print(dados.text + " ; "+ data + " ; " + horario)

dados = Instagram.seguidores()
print(dados)