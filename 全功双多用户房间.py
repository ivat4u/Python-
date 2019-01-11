# -*- coding: UTF-8 -*-
import socket, select
import re

server = socket.socket()
Addr = ("", 2050)
server.bind(Addr)
server.listen(5)
inputs = [server]
clientdict = {}
user = "No name user"
roomnumber = 0
print "Start the chat server..."

while True:
    rs, ws, es = select.select(inputs, [], [])
    # 1、select函数阻塞进程，直到inputs中的套接字被触发（在此例中，套接字接收到客户端发来的握手信号，从而变得可读，满足select函数的“可读”条件），rs返回被触发的套接字（服务器套接字）；
    for i in rs:
        if i == server:
            client, addr = i.accept()
            # print "Connected from",addr,"this is user%s"%user
            inputs.append(client)
            clientdict[client] = [client, addr, user, roomnumber]

        else: #5、当客户端发送数据时，客户端套接字被触发，rs返回客户端套接字，然后进行下一步处理。
            try:
                data = i.recv(1024)
                matchname = re.match(r'(.+)\sjoin the server', data)
                matchroom = re.match(r'Join the room(\d)', data)
                if matchname:
                    print data
                    for x in inputs:
                        if x == server or x == i:
                            pass
                        else:
                            if clientdict[x][2] == "No name user" or clientdict[x][3] == 0:
                                pass
                            else:
                                x.send(data)
                    username = matchname.group(1)
                    clientdict[i][2] = username
                    i.send('Welcome,%s' % username)
                elif matchroom:
                    print '%s' % clientdict[i][2], data
                    roomnumber = matchroom.group(1)
                    clientdict[i][3] = roomnumber
                    i.send('You join room%s' % roomnumber)
                    for x in inputs:
                        if x == server or x == i:
                            pass
                        else:
                            if clientdict[x][3] == clientdict[i][3]:
                                x.send('%s join this room' % clientdict[i][2])
                else:
                    senddata = "%s said:%s" % (clientdict[i][2], data)
                    for x in inputs:
                        if x == server or x == i:
                            pass
                        else:
                            if clientdict[x][3] == clientdict[i][3]:
                                x.send(senddata)
                disconnected = False

            except socket.error:
                disconnected = True

            if disconnected:
                leftdata = "%s has left" % clientdict[i][2]
                print leftdata
                for x in inputs:
                    if x == server or x == i:
                        pass
                    else:
                        x.send(leftdata)
                inputs.remove(i)
