from functions import InstagramBot
from mongoConnect import connect
import json
import os

if __name__ == "__main__":
    userInsta = os.getenv("USER_INSTAGRAM")
	pwdInsta = os.getenv("PASSWORD_INSTAGRAM")
	bot = InstagramBot(userInsta, pwdInsta)
	conn, mydb = connect()
	"""
	Buscar post por hashtag
	"""
	# with open("hashtags.json") as dataJson:
	# 	data = json.load(dataJson)
	# 	for getHashTags in data["data"][0]["empreendedorismo"]:
	# 		searchHashtag = (getHashTags["hashtag"]).replace("#","")
	# 		bot.findPostByhashtag(searchHashtag)

	"""
	Buscar pessoas que curtiram o post
	"""
	for linksPost in mydb.postsLinks.find():
		print(linksPost["_id"])
		bot.SearchPeopleByPostLink("https://www.instagram.com/p/B82q9iYB4zA/")
	bot.driver.close()
			