from mongoConnect import connect

conn, mydb = connect()

# for docs in mydb.usersInstagram.find():
#     mydb.usersInstagram.find_one_and_update
#     print(docs)

x = mydb.usersInstagram.update_many(
        {'enviadoFollow': True}, {"$set":{'enviadoFollow': False}}
    )
print(x)
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "enviadoFollow": False } }

# x = mycol.update_many(myquery, newvalues)