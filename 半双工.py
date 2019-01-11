#-*- coding:utf-8 -*-
from socket import *

HOST = ""
PORT = 2051
ADDR = (HOST, PORT)
BUFSIZ = 1024
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print "Waiting for connect..."
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr
    while True:
        data = tcpCliSock.recv(BUFSIZ)#因为该条语句是阻塞的，导致接受和发送无法同时进行
        if data == 'Quit':
            tcpCliSock.close()
        else:
            print "%s said:%s" % (addr, data)
        senddata = ""
        while senddata == "":
            senddata = raw_input('> ')
        tcpCliSock.send(senddata)
        data = None
tcpCliSock.close()
