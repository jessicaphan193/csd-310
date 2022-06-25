from pymongo import MongoClient

import pymongo

try:
    conn = MongoClient()
    print("Connected")
except:
    print("Not connected")

url = "mongodb+srv://admin:admin@cluster0.izawcpw.mongodb.net/?retryWrites=true&w=majority";


#from pymongo import MongoClient
client = MongoClient(url)

db = client.pytech

students = db.students

docs = db.students.find({})
for doc in docs:
    print(doc)


results = db.students.update_one({"student_id": "1007"}, 
                        {"$set": {"last_name": "Smith"}})
print(results)

doc = db.students.find_one({"student_id":"1007"})
print(doc)