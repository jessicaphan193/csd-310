from pymongo import MongoClient

import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.izawcpw.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test
col = db['test1']

dic = {"first_name": "Thorin"}

x = col.insert_one(dic)

print(x)


