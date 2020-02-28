from functions import InstagramBot
from mongoConnect import connect
import json
import os
import time
import random
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException

def SearchByHashTag_main():
	with open("hashtags.json") as dataJson:
		data = json.load(dataJson)
		for getHashTags in data["data"][0]["empreendedorismo"]:
			searchHashtag = (getHashTags["hashtag"]).replace("#","")
			bot.findPostByhashtag(searchHashtag)

def PeopleLikePost_main():
	for linksPost in mydb.postsLinks.find():
		print(linksPost["_id"])
		try:
			if linksPost["LinkPerfisPego"] != True:
				bot.SearchPeopleByPostLink(linksPost["_id"],linksPost["hashTag"])
				mydb.postsLinks.find_one_and_update({"_id":linksPost["_id"]}, {"$set" :{"LinkPerfisPego":True}})
		except KeyError:
			bot.SearchPeopleByPostLink(linksPost["_id"], linksPost["hashTag"])
			mydb.postsLinks.find_one_and_update({"_id":linksPost["_id"]}, {"$set" :{"LinkPerfisPego":True}})

def classifyLanguageProfile_main(doc,instancia):
	idProfile = doc["_id"]
	response = bot.classifyLanguageProfile(idProfile)
	try:
		if response["NotFound"] == False:
			respLang = response["lang"]
			mydb.usersInstagram.find_one_and_update({"_id":idProfile}, {'$set':{
				"language":respLang,
				"bio":response["bio"],
				"langChecked":True
			}})
			print(f"lang: {respLang} - updated - Instancia {instancia}")
		else:
			# mydb.usersInstagram.delete_one({"_id":idProfile})
			print("deleted - NotFound page") 
	except TypeError:
		print(f"updated - Instancia {instancia}")
if __name__ == "__main__":
	load_dotenv()
	userInsta = os.getenv("USER_INSTAGRAM")
	pwdInsta = os.getenv("PASSWORD_INSTAGRAM")
	instancia = 2
	bot = InstagramBot(userInsta, pwdInsta, instancia)
	
	# bot.login()
	conn, mydb = connect()

	"""	Buscar post por hashtag"""
	# SearchByHashTag_main()
	"""	Buscar pessoas que curtiram o post"""
	# PeopleLikePost_main()
	"""	Classificar linguagem dos perfis"""
	docsList = mydb.usersInstagram.find({"IDP":instancia})
	for doc in docsList:
		if doc["langChecked"] == False:
			time.sleep(random.randint(5,40))
			classifyLanguageProfile_main(doc,instancia)
	time.sleep(10)
	bot.driver.close()
