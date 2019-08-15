#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
socket 是一个抽象的概念，通常我们使用socket表示打开一个网络连接。
需要目标计算机的ip地址以及端口号
'''
import socket
'''
参数一：ip协议  ipv4
参数二：tcp协议
'''
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 创建连接
'''
address: ip地址［域名］ 端口号
网页端口默认80，
STMP邮件端口默认25
'''
sock.connect(("www.zxxk.com",80))
# 发送数据给服务器
sock.send(b"GET / HTTP/1.1\r\nHost:yw.zxxk.com\r\nConnection:close\r\n\r\n")

buffer = b""
while True:
    res = sock.recv(1024*1000)
    if res == b"":
        break
    buffer += res
    # print(res,end="")
# print(buffer)
buffer = buffer.decode("utf-8",errors="ignore")
sock.close()
resList = buffer.split("\r\n\r\n",maxsplit=1)
print(len(resList))
with open("head.txt","w",encoding="utf-8") as f:
    f.write(resList[0])

with open("zxxk.html","w",encoding="utf-8") as f2:
    f2.write(resList[-1])
'''
head.txt
zxxk.html
'''