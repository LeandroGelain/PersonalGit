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
		mobile_emulation = { "deviceName": "Nexus 5" }
		self.conn , self.mydb = mongoConnect.connect()
		self.options = webdriver.ChromeOptions()
		self.options.add_argument('--profile-directory=Default')
		self.options.add_argument('--user-data-dir=./User_Data')
		self.options.add_experimental_option("mobileEmulation", mobile_emulation)
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

	def SearchPeopleByPostLink(self, link):
		self.driver.get(link)
		self.driver.find_element_by_class_name('zV_Nj').click()
		time.sleep(.4)
		currentScrollCheck = 0
		i=1
		while True:
			self.driver.execute_script(f"window.scrollTo(0,{i*1000})")
			i+=1
			currentScroll = (self.driver.execute_script("return window.pageYOffset"))
			time.sleep(.5)
			if currentScroll != currentScrollCheck:
				currentScrollCheck = currentScroll
			else:
				break

		profileElements = self.driver.find_elements_by_tag_name("a")
		exceptionsLinks = ["https://www.instagram.com/","https://www.instagram.com/explore/","https://www.instagram.com/accounts/activity/","https://www.instagram.com/evolui_mtk/"]
		links = []
		for i in profileElements:
			link = (i.get_attribute("href"))
			if not link in exceptionsLinks:
				links.append(link)
		current_day = date.today().strftime("%d/%m/%Y")	
		for link in links:	
			try:
				self.mydb.usersInstagram.insert_one({
					"_id":str(link),
					"enviadoFollow":True,
					"followBack":False,
					"canceledFollow":False,
					"currentDate":str(current_day)
				})
			except pymongo.errors.DuplicateKeyError:
				print("duplicate key error")
		print(len(profileElements))

