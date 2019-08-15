# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2019/7/30 0030 15:12
# # @Author  : joker-syc
# # @Site    :
# # @File    : 服务端.py
# # @Software: PyCharm
#
# import socket
# '''
# 先写一个UDP的
# '''
#
# sever=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
# sever.bind(('10.20.159.230',8090))
#
# with open(file=r'C:\Users\Administrator\PycharmProjects\workhard\venv\Include\day16\data.txt',mode='r',encoding='utf-8') as f:
#     # print(len(f.readlines()))
#     print("服务器已开启")
#     joke=f.readlines()
#     # print(joke)
#     # print(type(joke))
#     while True:
#         flag=True
#         date,adress=sever.recvfrom(1024)
#         print(date.decode('utf-8'),adress)
#         # print(type(date.decode('utf-8')))
#         if date.decode('utf-8')=='bye':
#             sever.sendto('bye'.encode('utf-8'), adress)
#         for a in joke:
#             if date.decode('utf-8') in a:
#                 flag=False
#                 sever.sendto(a.encode('utf-8'),adress)
#         if flag:
#             sever.sendto('抱歉,未找到相应的笑话'.encode('utf-8'), adress)
#
#
#
#
#
