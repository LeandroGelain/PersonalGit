from bs4 import BeautifulSoup as Bs
from mongoConnect import connect
from selenium import webdriver
from lxml import html
import requests
import time

'''
fonte: INVESTING (https://br.investing.com/)
'''
class Get_data(object):

    def __init__(self):
        # self.conn, self.mydb = connect()
        # self.driver = webdriver.Firefox()
        pass
    def scraper(self, url):
        # self.driver.get(url)
        self.page = requests.get(url)
        self.soup = Bs(self.page.content, 'lxml')
        for self.content in self.soup.find_all('tbody'):
            print(self.content)
            
            
if __name__ == '__main__':
    try:
        get = Get_data()
        get.scraper('https://br.investing.com/equities/brazil')
        # get.driver.close()
    
    except KeyboardInterrupt:
        # get.driver.close()
        pass