import pymongo

def connect():
    conexaoBD = pymongo.MongoClient('mongodb://leandrogelain2300:M.a.159730@myworkspace-shard-00-00-udqoj.mongodb.net:27017,myworkspace-shard-00-01-udqoj.mongodb.net:27017,myworkspace-shard-00-02-udqoj.mongodb.net:27017/test?ssl=true&replicaSet=MyWorkspace-shard-0&authSource=admin&retryWrites=true')
    myDB = conexaoBD['Projetos-pessoais']

    return conexaoBD, myDB