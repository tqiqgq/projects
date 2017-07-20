import socket
import threading
import sys
import time

# Wait for incoming data from server
# .decode is used to turn the message in bytes to a string

# Get host and port
signal = True
host = "localhost"
port = 5000


def receive(socket_client, signal):
    while signal:
        try:
            data = socket_client.recv(32)
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            signal = False
            break

# Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

# Create new thread to wait for data
receiveThread = threading.Thread(target=receive, args=(sock, True))
receiveThread.start()

# Send data to server
# str.encode is used to turn the stri+ng message into bytes so it can be sent across the network
while signal:
    message = input()
    sock.send(message.encode())
    time.sleep(2)
    if message == "exit":
        sock.close()
        break
