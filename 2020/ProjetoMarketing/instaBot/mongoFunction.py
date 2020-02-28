from mongoConnect import connect
from outherFunctions import remove_repetidos

conn, mydb = connect()

def QuebraLista(lista, NumeroDeDocsPorLista):
	for i in range(0, len(lista), NumeroDeDocsPorLista):
		yield lista[i:i + NumeroDeDocsPorLista]

def update_many_teste():
    x = mydb.usersInstagram.update_many(
            {'langCheck': True}, {"$set":{'langCheck': None}}
        )
    print(x)

def divideUsersPorIDP():
    lista = []
    for elementos in mydb.usersInstagram.find():
        lista.append(elementos)

    instancias = int(len(lista)/6)
    print(instancias)
    splited = list(QuebraLista(lista, instancias))
    print(len(splited))
    count=1
    try:
        for i in range(1,instancias+1):
            for doc in splited[i-1]:
                print( i ,"-",doc["_id"])
                mydb.usersInstagram.find_one_and_update({"_id":doc["_id"]}, {"$set":{"IDP":i}})	
                count+=1
    except IndexError:
        pass

# divideUsersPorIDP()