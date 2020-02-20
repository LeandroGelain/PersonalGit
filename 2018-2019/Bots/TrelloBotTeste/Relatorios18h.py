import requests
import json
import csv

key = '6950b8934d57f2f842b5e20e9df3081b'
token = '83833e6c9ab00b6d7a818809644d78eb63c416a05a7b0e61c029c4e57f0ed53a'
# idBoard = '5c879757f9ec7677ec8dc306'
idBoards = {
	#Time condor
	"id1":"5c879757f9ec7677ec8dc306",
	"id2":"5c87975b34ffb863e3562aa3",
	"id3":"5c879751062e1e38a539ff28",
	"id4":"5c87975f45d15517216938aa",
	"id5":"5c87999941ef10370674b424",
	"id6":"5c92221614b5d91db3379725",
	"id7":"5c92222e1467ad7f61e8c935",
	#Time cygni
	'id8':'5c5839d217bed6275c21b21e',
	'id9':'5c5839501e5d3b0fe27ded1e',
	'id10':'5c5837ce0e84fd5b2ed3389c',
	'id11':'5c583a47a767c06173ea2b94',
	'id12':'5c584165a881ef674377aae9',
	#Time Linha hunter
	'id13':'5c824191de36ac70b1d13d48',
	'id14':'5c8241a94ed68f0e7119cbb4',
	'id15':'5c7fc82bdbfaa9778459435b',
	'id16':'5c8241c980cdb87533daf1a6',
	'id17':'5c8241e8e7739a3d5268abf9',
	#Time Pulverizador de barras jacto
	'id18':'5c4adbcbc5904e63036157c4',
	'id19':'5c4adbe24636cb179bc43a1d',
	'id20':'5c4adbf61bc41f6765f8578c',
	'id21':'5c4adc08abc56b51a7bbed60',
	'id22':'5c5421f5993dd12a2a20d35a',
	#Time Uniport 2530
	'id23':'5c6c31d173ce5308d409ef59',
	'id24':'5c6c31e9e64bf81a90053a7e',
	'id25':'5c6c321e0dacc41d2bf07851',
	'id26':'5c6c319143dab36629e90641',
	'id27':'5c6c3261f041985d43d89ac0',
	#Time Uniport 3030
	'id28':'5c544907ac7603402eb900cd',
	'id29':'5c544955b6e2957005ea9653',
	'id30':'5c5447fbad5d3a8304ca4b6e',
	'id31':'5c5449752a1dc16ff3a7f831',
	'id32':'5c5449976953fa3f9611fcd0',
	#Time Iniport 5030
	'id33':'5c3a913e06d11f4d953bf41b',
	'id34':'5c3a9205dae4807b323464f9',
	'id35':'5c3a8d94f62c481e9e9fbd80',
	'id36':'5c3a92878e118e367c75e289',
	'id37':'5c485b3665ee284d25f3e8ba',
	'id38':'5c9222a1438324110555a610',
	'id39':'5c9222b2563a6c111e4cef5e',
	#Time Videos Jacto
	'id40':'5c894de00d41aa2c1422b5ce',
	'id41':'5c8971078199d664d40e955c',
	}


#Paremetros dentro de cada Board e card abaixo
#-------------------------------------------------------------------------------------------------------
def getNameBoard(key, token, idBoard):
	url = "https://api.trello.com/1/boards/5c879751062e1e38a539ff28"

	querystring = {"actions":"all",
				"boardStars":"none",
				"cards":"none",
				"card_pluginData":"false",
				"checklists":"none",
				"customFields":"false",
				"fields":"name",
				"lists":"open",
				"members":"none",
				"memberships":"none",
				"membersInvited":"none",
				"membersInvited_fields":"all",
				"pluginData":"false",
				"organization":"false",
				"organization_pluginData":"false",
				"myPrefs":"false",
				"tags":"false",
				"key":key,"token":token
			 	 }

	response = requests.request("GET", url, params=querystring)
	BoardName = (json.loads(response.content.decode('utf-8')))
	return BoardName['name']

def getIDList(key, token, idBoard):
	url = "https://api.trello.com/1/boards/"+str(idBoard)+"/cards/"

	querystring = {'fields':'idList', 'token': token, 'key': key}
	response = requests.request("GET", url, params=querystring)
	lists = (json.loads(response.content.decode('utf-8')))
	return lists

def getNameTable(key, token, idList):
	url = "https://api.trello.com/1/lists/"+str(idList)
	querystring = { 'key' : key , 'token' : token}

	response = requests.request("PUT", url , params=querystring)
	table = (json.loads(response.content.decode('utf-8')))
	if 'name' in table:
		return table['name']
	else:
		return ''

def getNameCard(key, token, idCard):
	url = "https://api.trello.com/1/cards/"+str(idCard)+"/name"
	
	querystring = {"key":key, "token":token, "fields":"name"}
	
	response = requests.request("GET", url, params=querystring)
	nameCard = (json.loads(response.content.decode('utf-8')))
	return nameCard

def getDetalhesCard(key, token, idCard):
	url = "https://api.trello.com/1/cards/"+str(idCard)
	querystring = {"fields":"desc",
					"attachments":"false",
					"attachment_fields":"all",
					"members":"false",
					"membersVoted":"false",
					"checkItemStates":"false",
					"checklists":"none",
					"checklist_fields":"all",
					"board":"false","list":"false",
					"pluginData":"false",
					"stickers":"false",
					"sticker_fields":"all",
					"customFieldItems":"false",
					"key":key,"token":token}
	
	response = requests.request("GET", url, params=querystring)
	detalhesCard = (json.loads(response.content.decode('utf-8')))
	return detalhesCard


def getCommentsCard(key, token, idCard):
	url = "https://api.trello.com/1/cards/"+str(idCard)+"/actions"
	querystring = {"key":key,"token":token}

	response = requests.request("GET", url, params=querystring)
	comments = (json.loads(response.content.decode('utf-8')))
	arrayComments= []
	arrayComments.clear()
	if comments != '':
		for comment in comments:
			typeComment = (comment['type'])
			if str(typeComment)== 'commentCard':
					arrayComments.append(comment['data']['text'])
	if len(arrayComments) == 0:
			return 'Sem Comentarios'
	else:
		arrayTratada = str(arrayComments).replace('\\n',' | ').replace(' |  | ',' | ')
		return arrayTratada

cont = 1
for idBoard in idBoards:
	NameTeam = idBoard.replace('id','')
	NameTeam = (int(NameTeam))
	if idBoard == False:
		print('Id não encontrado')
		cont+=1
	else:
		idBoard = idBoards['id'+str(cont)]
		cont+=1

		listas = getIDList(key,token,idBoard)
		for idLists in listas:
	
			csvDados = open('relatorio18h.csv','a+')
			idCard = (idLists['id'])
			idList = (idLists['idList'])
	
			nameTable =(getNameTable(key, token, idList))
	
			nameCard = (getNameCard(key, token, idCard))
			nameCard = nameCard['_value']
			# print (nameCard)

			descCard = (getDetalhesCard(key, token, idCard))
			descCard = descCard['desc']
			descCard = descCard.replace('\n',' | ')
			# print(descCard)

			commentCard = getCommentsCard(key, token, idCard)
			commentCard = commentCard.replace("['", '').replace("']",'')
			nameBoard = getNameBoard(key, token, idBoard)
		
			if NameTeam <= 7:
				csvConc = ('Time Condor'+' ; '+nameBoard +' ; '+ nameTable + ' ; '+ nameCard + ' ; '+ descCard + ' ; '+ commentCard+'\n')
				print(csvConc)
				csvDados.write(csvConc)

			elif NameTeam > 7 and NameTeam <= 12:
				csvConc = ('Time Cygni'+' ; '+nameBoard +' ; '+ nameTable + ' ; '+ nameCard + ' ; '+ descCard + ' ; '+ commentCard+'\n')
				print(csvConc)
				csvDados.write(csvConc)
			elif NameTeam > 12 and NameTeam <= 17:
				csvConc = ('Time Linha hunter'+' ; '+nameBoard +' ; '+ nameTable + ' ; '+ nameCard + ' ; '+ descCard + ' ; '+ commentCard+'\n')
				print(csvConc)
				csvDados.write(csvConc)
			elif NameTeam > 17 and NameTeam <= 22:
				csvConc = ('Time Pulverizador de barras jacto'+' ; '+nameBoard +' ; '+ nameTable + ' ; '+ nameCard + ' ; '+ descCard + ' ; '+ commentCard+'\n')
				print(csvConc)
				csvDados.write(csvConc)
			elif NameTeam > 22 and NameTeam <= 27:
				csvConc = ('Time Uniport 2530'+' ; '+nameBoard +' ; '+ nameTable + ' ; '+ nameCard + ' ; '+ descCard + ' ; '+ commentCard+'\n')
				print(csvConc)
				csvDados.write(csvConc)
			elif NameTeam > 27 and NameTeam <= 32:
				csvConc = ('Time Uniport 3030'+' ; '+nameBoard +' ; '+ nameTable + ' ; '+ nameCard + ' ; '+ descCard + ' ; '+ commentCard+'\n')
				print(csvConc)
				csvDados.write(csvConc)
			elif NameTeam > 32 and NameTeam <= 39:
				csvConc = ('Time Uniport 5030'+' ; '+nameBoard +' ; '+ nameTable + ' ; '+ nameCard + ' ; '+ descCard + ' ; '+ commentCard+'\n')
				print(csvConc)
				csvDados.write(csvConc)
			elif NameTeam > 39 and NameTeam <= 41:
				csvConc = ('Time Videos Jacto'+' ; '+nameBoard +' ; '+ nameTable + ' ; '+ nameCard + ' ; '+ descCard + ' ; '+ commentCard+'\n')
				print(csvConc)
				csvDados.write(csvConc)
	csvDados.close()