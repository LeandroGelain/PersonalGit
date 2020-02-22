from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from datetime import date
import mongoConnect
import pymongo
import time

class InstagramBot(object):

	def __init__(self, username, password):
		print("========= inicializing bot ==========")
		self.username = username
		self.password = password
		self.conn , self.mydb = mongoConnect.connect()
		self.options = webdriver.ChromeOptions()
		self.options.add_argument('--profile-directory=Default')
		self.options.add_argument('--user-data-dir=./User_Data')
		self.options.add_argument("--window-size=1920x1080")
		# self.options.add_argument("--headless")
		self.driver = webdriver.Chrome(chrome_options=self.options)
		# self.driver.maximize_window()
		self.driver.get('https://www.instagram.com')

	def login(self):
		self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
		time.sleep(2)
		loginFields = self.driver.find_elements_by_tag_name("input")
		for i in range(len(loginFields)):
			if (i == 0):
				loginFields[i].send_keys(self.username)
			elif(i == 1):
				loginFields[i].send_keys(self.password)	
		self.driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button").click()
		time.sleep(2)							  
					

	def findPostByhashtag(self, hashtag):
		"""
		Apenas os posts que está no 'Principais publicações' por enquanto
		"""
		self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
		time.sleep(3)
		self.elementList = []
		try:
			for i in range(1,4):
				for j in range(1,4):
					self.post = (self.driver.find_element_by_css_selector(f"#react-root > section > main > article > div.EZdmt > div > div > div:nth-child({i}) > div:nth-child({j})"))
					if self.post != "":									
						self.elementList.append(self.post.find_element_by_tag_name("a").get_attribute("href"))
		except NoSuchElementException:
			pass
		current_day = date.today().strftime("%d/%m/%Y")			
		
		print( f"=============  {hashtag}  ==============" )
		for element in self.elementList:
			try:
				self.mydb.postsLinks.insert_one({
													"_id":str(element),
													"hashTag":str(hashtag),
													"currentDate":str(current_day)
												})
				print(element)
			except pymongo.errors.DuplicateKeyError:
				print("duplicate key error")
		
		print( "=========================================" )