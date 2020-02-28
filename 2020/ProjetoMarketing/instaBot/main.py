from functions import InstagramBot
from mongoConnect import connect
import json
import os
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException

if __name__ == "__main__":
	load_dotenv()
	userInsta = os.getenv("USER_INSTAGRAM")
	pwdInsta = os.getenv("PASSWORD_INSTAGRAM")
	bot = InstagramBot(userInsta, pwdInsta, 1)
	bot.login()
	conn, mydb = connect()

	# =============================================================================
	"""
	Buscar post por hashtag
	"""
	# with open("hashtags.json") as dataJson:
	# 	data = json.load(dataJson)
	# 	for getHashTags in data["data"][0]["empreendedorismo"]:
	# 		searchHashtag = (getHashTags["hashtag"]).replace("#","")
	# 		bot.findPostByhashtag(searchHashtag)
	# =============================================================================
	
	# =============================================================================
	"""
	Buscar pessoas que curtiram o post
	"""
	for linksPost in mydb.postsLinks.find():
		print(linksPost["_id"])
		try:
			if linksPost["LinkPerfisPego"] != True:
				bot.SearchPeopleByPostLink(linksPost["_id"],linksPost["hashTag"])
				mydb.postsLinks.find_one_and_update({"_id":linksPost["_id"]}, {"$set" :{"LinkPerfisPego":True}})
		except KeyError:
			bot.SearchPeopleByPostLink(linksPost["_id"], linksPost["hashTag"])
			mydb.postsLinks.find_one_and_update({"_id":linksPost["_id"]}, {"$set" :{"LinkPerfisPego":True}})
	# =============================================================================
		
	bot.driver.close()