import pymongo

def connect():
    conexaoDB = pymongo.MongoClient("mongodb+srv://LeandroGelain03:M.a.159730@datainstagram-s6xj1.mongodb.net/test?retryWrites=true&w=majority")
    myDB = conexaoDB['InstagramMarketing']
    return conexaoDB, myDB