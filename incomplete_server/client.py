
from socketIO_client import SocketIO, LoggingNamespace
import socket, json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Start client!")
s.connect(("localhost", 4080))
#data1 = s.recv(1024).decode("utf-8")
data = {"dsdsdsds": "3434343434344", "ghghghghgh": "787878787878"}
#s.send(json.dumps({"res":data}).encode())
s.send((str(data) + "\n").encode())
#s.send(b"{res: \"rererer\"")
s.close()

#with SocketIO('localhost', 4080, LoggingNamespace) as socketIO:
    #socketIO.emit("res", data)