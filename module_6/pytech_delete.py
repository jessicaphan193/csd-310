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

#insert Ed Parker
Ed = {
    "student_id": "1010",
    "first_name": "Ed",
    "last_name": "Parker"
}
Ed_student_id = students.insert_one(Ed).inserted_id

print(f"\nInserted student record", Ed, Ed_student_id)

doc = db.students.find_one({"student_id":"1010"})
print(doc)

#delete
results = db.students.delete_one({"student_id": "1010"},)
print(results)


docs = db.students.find({})
for doc in docs:
    print(doc)
