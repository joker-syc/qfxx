#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import socket
import threading

# 创建一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定地址，ip地址＋端口号
iplocation=input('请输入服务器要绑定的地址:\n')
port=int(input('请输入要绑定的端口号:\n'))

s.bind((iplocation,port))
#设置最大监听数
s.listen(5)
def cnthread(sock,adress):
    t=threading.Thread(target=server,args=('在线聊天开启',sock,adress))
    t.start()
    t.join()

def recvmessage():
    data = sock.recv(1024).decode("utf-8")
    print('收到的信息:',data)

def server(a,sock,adress):
    print(a+threading.current_thread().name)
    while True:
        t=threading.Thread(target=recvmessage,daemon=False,name='connection')
        t.start()
        msg = input()
        if msg=='bye':
            break
        sock.send(msg.encode("utf-8"))

if __name__ == '__main__':
    while True:
        sock, adress = s.accept()
        print(sock, adress)
        cnthread(sock,adress)




