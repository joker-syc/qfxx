#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(("10.20.159.161",9099))

while True:
    msg = input("请输入您要发送的内容：")
    sock.send(msg.encode("utf-8"))
    if msg == "bye":
        break
    res = sock.recv(1024)
    print(res.decode("utf-8"))

sock.close()