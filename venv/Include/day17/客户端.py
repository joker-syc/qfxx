# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2019/7/30 0030 15:12
# # @Author  : joker-syc
# # @Site    :
# # @File    : 客户端.py
# # @Software: PyCharm
#
# import socket
#
# cus=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
# while True:
#     data = input("请输入您要发送的内容：").encode("utf-8")
#     if data == b"bye":
#         break
#     cus.sendto(data,('10.20.159.230',8090))
#     print(cus.recv(2048).decode("utf-8"))
#
# sock.close()