# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2019/7/30 0030 8:58
# # @Author  : joker-syc
# # @Site    :
# # @File    : test.py
# # @Software: PyCharm
#
# # import re
# #
# # print(re.split(r'[a-z]|\W',r'23u4h33hu3hu*(JH*8e3heJK&u3heJHuuhduHHBBdh3h8',flags=re.I))
#
# import socket
# '''
# 参数一：ip协议  ipv4
# 参数二：tcp协议
# '''
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# # 创建连接
# '''
# address: ip地址［域名］ 端口号
# 网页端口默认80，
# STMP邮件端口默认25
# '''
# # sock.connect(("www.zxxk.com",80))
# # # 发送数据给服务器
# # sock.send(b"GET / HTTP/1.1\r\nHost:yw.zxxk.com\r\nConnection:close\r\n\r\n")
# #
# # buffer = b""
# # while True:
# #     res = sock.recv(1024*1000)
# #     if res == b"":
# #         break
# #     buffer += res
# #     # print(res,end="")
# # # print(buffer.decode("utf-8",errors="ignore"))
# # # print(buffer)
# # file1=buffer.decode(encoding='utf-8',errors='ignore')
# # # print(file1)
# # dd=file1.split('\r\n\r\n',maxsplit=1)
# # print(dd[0])
# # print(dd[-1])
# # sock.close()

# 全错排列问题的递归解法
# def nolist(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return (n-1)*(nolist(n-1)+nolist(n-2))
#
# print(nolist(int(input("请输入元素个数"))))

#全错排列问题的非递归解法
# n=int(input('请输入元素个数'))
# ans=3
# a=0
# b=1
# while 1:
#     if n==1:
#         print(a)
#         break
#     elif n==2:
#         print(b)
#         break
#     elif ans<=n:
#         z=(ans-1)*(a+b)
#         a=b
#         b=z
#         ans+=1
#         print(z,a,b,ans,"\n")
#     else:
#         print(z)
#         break

eval("print([a for a in range(10)])")

