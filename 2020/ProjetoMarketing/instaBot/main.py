from functions import InstagramBot
import json
if __name__ == "__main__":
	bot = InstagramBot("user", "pwd")
	with open("hashtags.json") as dataJson:
		data = json.load(dataJson)
		for getHashTags in data["data"][0]["empreendedorismo"]:
			searchHashtag = (getHashTags["hashtag"]).replace("#","")
			bot.findPostByhashtag(searchHashtag)

	bot.driver.close()
			