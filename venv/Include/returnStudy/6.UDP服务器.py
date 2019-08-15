#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import socket

'''
参数一：指定ipv4协议，ip协议
参数二：指定udp协议
'''
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定地址，ip地址＋端口号
s.bind(("10.20.159.161",9000))

while True:
    data,adress = s.recvfrom(1024)
    print(data.decode("utf-8"))
    print(adress)
    s.sendto("收到".encode("utf-8"),adress)