from pymongo import MongoClient

url = "mongodb+srv://<username>:<password>@cluster0.izawcpw.mongodb.net/?retryWrites=true&w=majority";

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names)


