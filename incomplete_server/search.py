from elasticsearch import Elasticsearch
from socketIO_client import SocketIO, LoggingNamespace
from bson import json_util, ObjectId
import json, pymongo, time, socket
print(u'data')
conn = pymongo.MongoClient('localhost', 27017)
db = conn.admin
#search_string = ""

search_string = db.users.find({"Searchstring": {'$exists': 1}})[0]["Searchstring"]
es = Elasticsearch()


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
    result = es.search(index=index_name, doc_type=type_doc, body={"size": count_doc,'query': {"match": {"text": search_string}},
                                                                   "highlight": {"fields": {"text": {}}}})

    for i in range(result["hits"]["total"]):
        #if result["hits"]["hits"][i]['_source']["name"] in result_of_search.keys():
            #result_of_search[result["hits"]["hits"][i]['_source']["name"]].append(
                #result["hits"]["hits"][i]["highlight"]["text"])
        result_of_search.update({str(i+1): {"name": result["hits"]["hits"][i]['_source']["name"], "entries":
            result["hits"]["hits"][i]["highlight"]["text"]}, "result": search_string})
        #else:
            #result_of_search.update({result["hits"]["hits"][i]['_source']["name"]:
                                         #result["hits"]["hits"][i]["highlight"]["text"]})
    return result_of_search

index_doc("myindex", "doc", 283)
#search_string = "Latvia"
res = search_doc("myindex", "doc", search_string, 283)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("search.py start socket-client!")

try:
    s.connect(("localhost", 4080))
    #s.send(b'\"data\": \"DATATAAAA\"')
except:
    print("Not connection: Error socket-server")
finally:
    #print("search.py Len res = " + str(len(res.keys())))
    for i in res.keys():
        s.send(str((res[i])).encode())
    print("search.py data transferted")
s.send(b"close")
s.close()


#with SocketIO('localhost', 4080, LoggingNamespace) as socketIO:
    #socketIO.emit('data', {'xxx': 'yyy'})
    #socketIO.emit('close')