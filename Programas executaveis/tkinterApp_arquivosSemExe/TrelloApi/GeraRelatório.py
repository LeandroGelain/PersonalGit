from TrelloApi.TrelloConfig import Trello as tconfig
import requests
import datetime
import json
import re
import os
import threading
import xlsxwriter
class OpenFolderError(Exception):
    def __str__(self):
        return 'Diretório já exite'


class GeraRelatorio(object):
    
    def __init__(self):
        self.Trello = tconfig()
        self.lista_idBoards = self.Trello.idBoards()
        self.status_code = False
        
    def function_nameBoards(self, key, token,idBoard):
        url = "https://api.trello.com/1/boards/"+str(idBoard)
        
        idBoard = '5c879757f9ec7677ec8dc306'
        querystring =   {"actions":"all",
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

        self.setResponse(requests.request("GET", url, params=querystring))
        return self.setName(json.loads(self.getResponse().content.decode('utf-8')))
	
    def function_IDs(self, key, token, idBoard):
        url = "https://api.trello.com/1/boards/"+str(idBoard)+"/cards/"
        querystring = {'fields':'idList', 'token': token, 'key': key}
        self.setResponse(requests.request("GET", url, params=querystring))
        return self.setIds(json.loads(self.getResponse().content.decode('utf-8')))

    def function_nameCards(self, key, token, idCard):
        url = "https://api.trello.com/1/cards/"+str(idCard)+"/name"
        querystring = {"key":key, "token":token, "fields":"name"}
        self.setResponse(requests.request('GET',url, params=querystring))
        self.nameCard = (self.setNameCard(json.loads(self.getResponse().content.decode('utf-8'))))
        return self.nameCard

    def function_nameList(self, key, token, idList):
        url = "https://api.trello.com/1/lists/"+str(idList)
        querystring = { 'key' : key , 'token' : token}
        self.setResponse(requests.request('PUT', url, params=querystring))
        self.nameList = (self.setNameList(json.loads(self.getResponse().content.decode('utf-8'))))
        return self.nameList

    def function_CommentCard(self, key, token, idCard):
        url = "https://api.trello.com/1/cards/"+str(idCard)+"/actions"
        querystring = {"key":key,"token":token}
        self.setResponse(requests.request("GET", url, params=querystring))
        self.commentCard = self.setCommentCard(json.loads(self.getResponse().content.decode('utf-8')))
        
        self.comment_card = self.getCommentCard()
        self.arrayComment = []
        for self.Comment in (self.comment_card):
            self.typeComment = self.Comment['type']
            if str(self.typeComment) == 'commentCard':
                self.comment_singular_card = (self.Comment['data']['text'])
                self.comment_singular_card = re.sub('\\n|\\t|  ',', ',self.comment_singular_card)
                self.arrayComment.append(self.comment_singular_card)
        
        return self.arrayComment
      
    def function_Description_card(self, key, token, idCard):
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
        
        self.setResponse(requests.request("GET", url, params=querystring))
        try:
            self.description_card = self.setDescritionCard(json.loads(self.getResponse().content.decode('utf-8')))
            return self.description_card
        except:
            self.description_card = 'Sem comentário'
            return self.description_card

    def function_main(self):
        self.pathLocal = os.getcwd()
        print('=====================================')
        data = datetime.date.today()
        self.data = str(data).split('-')
        NomeMes = {'01':'Janeiro', '02':'Fevereiro', '03':'Março', '04':'Abril',
                    '05':'Maio','06':'Junho', '07':'Julho', '08':'Agosto',
                    '09':'Setembro', '10':'Outubro','11':'Novembro', '12':'Dezembro'}
        self.mes = self.data[1]
        self.nomeMes = NomeMes['%s'%self.mes]
        self.day = (self.data[2])
        self.year = self.data[0]
        self.nameDir = ('Relatórios-%s-%s'%(self.nomeMes, self.year))

        try:
            self.status_access = (os.access(r'%s\%s'%(self.pathLocal,self.nameDir), os.R_OK))
            if self.status_access == False:
                self.newDirPerMonth = os.mkdir('%s\%s'%(self.pathLocal,self.nameDir))
                print(os.access('%s\%s'%(self.pathLocal,self.nameDir), os.R_OK))
            else:
                print(os.access('%s\%s'%(self.pathLocal,self.nameDir), os.R_OK))

        except OpenFolderError:
            print('Diretorio já exite')
        
        except FileNotFoundError:
            print('except1')
            self.newDirPerMonth = os.mkdir('%s\%s'%(self.pathLocal,self.nameDir))
            print(os.access(r'%s\%s'%(self.pathLocal,self.nameDir), os.R_OK))
        except FileExistsError:
            print('except2')
            self.newDirPerMonth = os.mkdir('%s\%s'%(self.pathLocal,self.nameDir))
            print(os.access(r'%s\%s'%(self.pathLocal,self.nameDir), os.R_OK))
        self.token = self.Trello.token
        self.key = self.Trello.key
        try:
            print('%s/%s/%s'%(self.day,self.nomeMes,self.year))
            # self.arquivo = xlsxwriter.Workbook('Relatório-%s-%s-%s.xlsx'%(self.day, self.mes, self.year))
            # self.arquivo = self.arquivo.add_worksheet()
           
            self.arquivo = open('%s\%s\Relatório-%s-%s-%s.xlsx'%(self.pathLocal,self.nameDir,self.day, self.mes, self.year),'a+')
            self.arquivo.write('Nome do Board;Nome da Lista;Nome do card;Descrição;Comentários')
            for num_board in self.lista_idBoards:
                self.singular_ids = self.lista_idBoards[num_board]
                self.name_board = self.function_nameBoards(self.key, self.token, self.singular_ids)
                self.name_board = self.getName()

                self.ids_card_list = self.function_IDs(self.key,self.token,self.singular_ids)
                self.ids_card_list = self.getIds()
                
                for i in range(len(self.ids_card_list)):
                    self.id_card = self.ids_card_list[i]['id']
                    self.id_list = self.ids_card_list[i]['idList']
                    
                    self.name_card = self.function_nameCards(self.key, self.token, self.id_card)
                    self.name_card = self.getNameCard()
                    
                    self.name_list = self.function_nameList(self.key, self.token, self.id_list)
                    self.name_list = self.getNameList()

                    self.description_in_card = self.function_Description_card(self.key, self.token, self.id_card)
                    self.description_in_card = self.getDescritionCard()
                    
                    self.comment_card = self.function_CommentCard(self.key, self.token, self.id_card)
                    self.comment_card = re.sub("[|]|'|",'',str(self.comment_card))
                    self.replaced_comment_card = ("'"+str(self.comment_card)+"'")
                    self.replaced_comment_card = self.replaced_comment_card.replace("'[",'').replace("]'", '')
                    
                    self.conc = ('%s ; %s ; %s ; %s ; %s \n'%(self.name_board,self.name_list, self.name_card, self.description_in_card, str(self.replaced_comment_card)))
                    self.conc = re.sub('[|]','',self.conc)
                    try:
                        print(self.conc)
                        self.arquivo.write(self.conc)
                    except UnicodeEncodeError:
                        pass
                        
        except KeyboardInterrupt:
            self.arquivo.close()
            return 'Fim da execussão'
        
        self.arquivo.close()
        return 'Fim da execussão'

    def getStatus_code(self):
        return self.status_code

    def setStatus_code(self, status_code):
        self.status_code = status_code

    def getDescritionCard(self):
        self.desc_card = self.desc_card['desc']
        self.desc_card = self.desc_card.replace('\n', '')
        return self.desc_card

    def setDescritionCard(self, desc_card):
        self.desc_card = desc_card
    
    def getCommentCard(self):
        return self.com_Card

    def setCommentCard(self, commentCard):
        self.com_Card = commentCard

    def getNameList(self):
        return self.NameList['name']

    def setNameList(self, NameList):
        self.NameList = NameList

    def getIds(self):
        return self.__idlist

    def setIds(self, idlist):
        self.__idlist = idlist

    def getNameCard(self):
        return str(self.nameCards['_value'])

    def setNameCard(self, nameCard):
        self.nameCards = nameCard

    def getResponse(self):
        return self.__response

    def setResponse(self, response):
        self.__response = response

    def getName(self):
        return self.__nome['name']

    def setName(self, nome):
        self.__nome = nome
