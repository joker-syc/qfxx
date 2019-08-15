#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import socket
import urllib


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = input("请输入您要发送的内容：").encode("utf-8")
    if data == b"bye":
        break
    sock.sendto(data,("10.20.159.161",9000))
    print(sock.recv(1024).decode("utf-8"))

sock.close()
