from pymongo import MongoClient

#import pymongo

#try:
#    conn = MongoClient()
#    print("Connected")
#except:
#    print("Not connected")

url = "mongodb+srv://admin:admin@cluster0.izawcpw.mongodb.net/?retryWrites=true&w=majority";


from pymongo import MongoClient
client = MongoClient(url)

db = client.pytech

students = db.students

Thorin = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield"
}
Thorin_student_id = students.insert_one(Thorin).inserted_id
print(Thorin_student_id)

Bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins"
}
Bilbo_student_id = students.insert_one(Bilbo).inserted_id
print(Bilbo_student_id)

Frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Boggins"
}
Frodo_student_id = students.insert_one(Frodo).inserted_id
print(Frodo_student_id)
