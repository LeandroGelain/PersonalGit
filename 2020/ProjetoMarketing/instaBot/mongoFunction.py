from mongoConnect import connect
from outherFunctions import remove_repetidos
conn, mydb = connect()

def update_many_teste():
    x = mydb.usersInstagram.update_many(
            {'enviadoFollow': True}, {"$set":{'enviadoFollow': False}}
        )
    print(x)

def insert_many_test():
    # x = mydb.testeInsertMany.insert_many(
    lista = [
        {"_id":1, "nome":"Jão testando"},
        {"_id":2, "nome":"Jão testando"},
        {"_id":2, "nome":"Jão testando"},
        {"_id":2, "nome":"Jão testando"},
        {"_id":4, "nome":"Jão testando"}
    ]
    lista2 = remove_repetidos(lista)
    print(lista2)
insert_many_test()