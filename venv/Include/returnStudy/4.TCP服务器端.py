#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import socket

# 创建一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定地址，ip地址＋端口号
s.bind(("10.20.159.161",9099))
#设置最大监听数
s.listen(5)

while True:
    sock,adress = s.accept()
    print(sock,adress)
    while True:
        data = sock.recv(1024).decode("utf-8")
        print(data)
        if data == "bye":
            break
        msg = input("请输入您要回复的内容")
        sock.send(msg.encode("utf-8"))




