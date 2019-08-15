#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import socket
import threading

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

iplocation=input('请输入客户机要绑定的地址:\n')
port=int(input('请输入要绑定的端口号:\n'))

sock.connect((iplocation,port))

def recvmessage():
    res = sock.recv(1024)
    print('收到的信息:',res.decode("utf-8"))

while True:
    msg = input()
    sock.send(msg.encode("utf-8"))
    if msg == "bye":
        break
    t=threading.Thread(target=recvmessage,daemon=False,name='connection')
    t.start()


sock.close()