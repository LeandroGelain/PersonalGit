import pymongo

def connect():
    conexaoDB = pymongo.MongoClient("mongodb+srv://user:pwd@datainstagram-s6xj1.mongodb.net/test?retryWrites=true&w=majority")
    myDB = conexaoDB['InstagramMarketing']
    return conexaoDB, myDB