import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.test
collection = db['person']
result = collection.delete_many({'age': 24})
print(result)
