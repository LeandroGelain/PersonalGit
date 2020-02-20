import requests
import json
import pymongo

key = "7a8f767767e5c03f6a5ff051c6c4942b"
token = "43c2df130bc67f353ed8f4ff0f7f04ad44b3a779d84a123621b3553f7b68da3a"
idBoard = "5c17bf769357164a9fa3a6f4"

lists = []

def getIDList(key, token, idBoard):
	url = "https://api.trello.com/1/boards/"+str(idBoard)+"/cards/"

	querystring = {'fields': 'idList, idMember' ,'key': key, 'token': token}
	response = requests.request("GET", url, params=querystring)
	lists = (json.loads(response.content.decode('utf-8')))
	return lists

def getNumeroCards(key, token, idList):
	url = "https://api.trello.com/1/lists/"+str(idList)+"/cards"
	
	querystring = {"fields":"name", 'key' : key, 'token': token}

	response = requests.request("GET", url  , params=querystring)
	lista = (json.loads(response.content.decode('utf-8')))
	return (len(lista))

def getNameTable(key, token, idList):
	url = "https://api.trello.com/1/lists/"+str(idList)

	querystring = { 'key' : key , 'token' : token}

	response = requests.request("PUT", url , params=querystring)
	table = (json.loads(response.content.decode('utf-8')))
	if 'name' in table:
		return table['name']
	else:
		return ''

def getIDTable(key, token, idList):
    
	url = "https://api.trello.com/1/lists/"+str(idList)
	querystring = { 'key' : key , 'token' : token}

	response = requests.request("PUT", url , params=querystring)
	table = (json.loads(response.content.decode('utf-8')))
	if 'id' in table:
		# print(table['id'])
		return table['id']

	else:
		return ''

def getIDMember(key , token, idCard):
	url = "https://api.trello.com/1/cards/"+(idCard)+"/members"
	querystring = {"fields":"fullName",'key':key , 'token':token }

	response = requests.request("GET", url, params=querystring)
	if response.status_code != 404:
		nomeMembro = json.loads(response.content.decode('utf-8'))
		# print(nomeMembro)
		if len(nomeMembro) != 0:
    			return nomeMembro
		else:
			return ''

def getNameCard(key, token, idList):
	url = "https://api.trello.com/1/cards/"+str(idList)+"/name"
	querystring = {"key":key, "token":token, "fields":"name"}
	
	response = requests.request("GET", url, params=querystring)
	nameCard = (json.loads(response.content.decode('utf-8')))
	return nameCard

listas = getIDList(key,token,idBoard)
for idLists in listas:
	idList =  (idLists['idList'])
	idCard = (idLists['id'])
	#idTable = getIDTable(key, token, idList)
	nameTable = getNameTable(key,token,idList)
	
	if nameTable != '':
    		
		nameCard = getNameCard(key, token, idCard)
		nameMembers = getIDMember(key, token, idCard)
		numCardTable = getNumeroCards(key, token, idList)
		
		for idMember in nameMembers:
			idMember = idMember['id']
			if idMember != '':
				print(idMember)

		if not nameMembers:
			print(nameTable + '- Ninguem associado -' + nameCard['_value'])
		
		else:
			for nameMember in nameMembers: 
				nameMember = nameMember['fullName']
				print(nameTable + ' - ' + nameMember + ' - ' + nameCard['_value'])
		
		