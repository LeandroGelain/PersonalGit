
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup 

driver = webdriver.Firefox(executable_path=r'C:\Users\leand\Documents\selenium\chromedriver.exe') 
driver.get("http://leideacesso.etransparencia.com.br/itaquaquecetuba.prefeitura.sp/Portal/desktop.html?410")
time.sleep(15)
 
# Aqui estou buscando o elemento que possui na classe o valor valo01, que e respectivo ao valor da receita onde quero clicar para ir na proxima pagina
receita = driver.find_element_by_class_name("val01")
# aqui e feito um clique no elemento que foi encontrado acima
receita.click()
# aguardando o carregamento da pagina
time.sleep(10)
# agora quero as receitas desde 2013 ate 2017
anos = ["2013","2014","2015","2016","2017"]
 
for a in anos:
    # aqui e utilizado o modulo Select do selenium para interagir com o ComboBox
    select = Select(driver.find_element_by_name("exe"))
    # aqui e alterado o valor do ComboBox
    select.select_by_value(a)
    # agora e buscado o elemento cujo o ID e igual a imgFiltrar
    filtrar = driver.find_element_by_id('imgFiltrar')
    # retornado o elemento da busca e clicado no botao
    filtrar.click()
    # aguardando o carregamento da tabela
    time.sleep(3)
    # armazenando a div que possui a tabela dentro da variavel dados
    dados = driver.find_element_by_id("bd10")