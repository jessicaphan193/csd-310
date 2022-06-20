from pymongo import MongoClient

import pymongo

url = "mongodb+srv://admin:admin@cluster0.izawcpw.mongodb.net/?retryWrites=true&w=majority";


from pymongo import MongoClient
client = MongoClient(url)

db = client.pytech

print(db.list_collection_names())