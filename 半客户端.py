from socket import *

HOST = 'localhost'
PORT = 2051
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        continue
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    print data

tcpCliSock.close()
