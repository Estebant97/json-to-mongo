import pymongo
import json
from pymongo import MongoClient, InsertOne
client = pymongo.MongoClient('localhost', 27017)
db = client['colormedb']
collection = db['zara-prod']
categories = []
# creates an array with our data
with open(r"./db.json") as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        category = myDict.keys()
for cat in category:
    if myDict[cat]:
        result = collection.insert_many(myDict[cat])
client.close()