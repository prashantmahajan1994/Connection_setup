import pymongo

client = pymongo.MongoClient("mongodb+srv://pmahajan:j839ngkUlvi1B57p@cluster0.0gfbg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['non']
coll = db1['test']
coll.insert_one(d )