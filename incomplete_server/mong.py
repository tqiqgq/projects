import json, pymongo
from bson import json_util, ObjectId
conn = pymongo.MongoClient('localhost', 27017)
db = conn.admin
#a = db.users.find({"result": "CZECH REPUBLIC"})   {'$exists': 1}
a = db.users.find({"result": "Latvia"})
for i in a:
    print(i)