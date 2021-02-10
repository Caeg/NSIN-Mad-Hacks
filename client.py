import socket

HEADERSIZE = 10
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((socket.gethostname(), 1236)) #Connects to server


while True:   
    full_msg = ''
    new_msg = True
    while True:
        msg = mySocket.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False         

        print (f"Full message legth:", msg[:HEADERSIZE])
        full_msg += msg.decode("utf-8")


        if len(full_msg)-HEADERSIZE == msglen:
            print ("full msg recieved")
            print (full_msg[HEADERSIZE:])
            new_msg = True




