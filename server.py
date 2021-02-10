import socket
import time

HEADERSIZE = 10

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((socket.gethostname(), 1236)) #(IP address, port number)
mySocket.listen(5)

while True:
    clientsocket, address = mySocket.accept() #Accepts everyone into server
    print (f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"Time: {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
