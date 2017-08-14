from elasticsearch import Elasticsearch
from bson import json_util, ObjectId
import json, pymongo, time
print("START ES")
conn = pymongo.MongoClient('localhost', 27017)
db = conn.admin
search_string = ""
while search_string == "":
    for i in db.users.find({"Searchstring": {'$exists': 1}}): #["Searchstring"]:
        search_string = str(i["Searchstring"])
    time.sleep(0.3)

es = Elasticsearch()

print(search_string)
def index_doc(index_name, type_doc, count_doc):
    try:
        for id in range(count_doc):
            body = db.users.find_one({"id": id})
            body.pop('_id')
            es.index(index=index_name, doc_type=type_doc, id=id, body=json.loads(json_util.dumps(body)))
    except:
        return False
    finally:
        return True


def search_doc(index_name, type_doc, search_string, count_doc):
    result_of_search = {}
    result = es.search(index=index_name, doc_type=type_doc, body={"size": count_doc, 'query': {"match": {"text": search_string}},
                                                                   "highlight": {"fields": {"text": {}}}})

    for i in range(result["hits"]["total"]):
        #if result["hits"]["hits"][i]['_source']["name"] in result_of_search.keys():
            #result_of_search[result["hits"]["hits"][i]['_source']["name"]].append(
                #result["hits"]["hits"][i]["highlight"]["text"])
        #print(result["hits"]["hits"][i]['_source']["name"])
        #print(type(result["hits"]["hits"][i]["highlight"]["text"]))
        result_of_search.update({"id": str(i), "name": result["hits"]["hits"][i]['_source']["name"], "entries":
            result["hits"]["hits"][i]["highlight"]["text"], "result": search_string})
        db.users.save({"id": str(i), "name": result["hits"]["hits"][i]['_source']["name"], "entries":
            result["hits"]["hits"][i]["highlight"]["text"], "result": search_string})

        #else:
            #result_of_search.update({result["hits"]["hits"][i]['_source']["name"]:
                                         #result["hits"]["hits"][i]["highlight"]["text"]})
    return result_of_search
search_string = "Latvia"
print("Indexing ...")
#index_doc("myindex", "doc", 283)
print("Searching ...")
res = search_doc("myindex", "doc", search_string, 283)
#print(res)
#print(res)


print("Finish indexing and searching!!!")