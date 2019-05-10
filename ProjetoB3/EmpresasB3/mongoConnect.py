import pymongo

def connect():
    conexaoBD = pymongo.MongoClient('mongodb://leandrogelain08:M.a.159730@cluster0-shard-00-00-o7elb.mongodb.net:27017,cluster0-shard-00-01-o7elb.mongodb.net:27017,cluster0-shard-00-02-o7elb.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')
    myDB = conexaoBD['pessoas-linkedin-data']

    return conexaoBD, myDB