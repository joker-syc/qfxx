#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
将内存中的变量变成可存储或者可传输的过程我们称之为序列化。
将序列化的对象重新读回到内存的过程我们称之为反序列化。

pickle模块
pickle.dumps(obj)
功能：将指定的对象序列化
pickle.dump(obj,f)
功能：将指定的对象序列化并写入到打开的文件中
pickle.loads(f2.read())
功能：将二进制的字符串反序列化为对象
pickle.load(f2)
功能：读取打开的文件对象，并且将读取到的内容反序列化为对象
'''
import pickle

dict1 = {"name":"lili","age":18}

class Card:
    def __init__(self,cardnum,password,money,islock=False):
        self.cardnum = cardnum
        self.password = password
        self.money = money
        self.islock = islock

card = Card("101110","110",110,True)

# with open("demo.txt","wb") as f:
#     # f.write(pickle.dumps(card))
#     pickle.dump(card,f)


with open("demo.txt","rb") as f2:
    res = pickle.load(f2)
    print(res)
    print(type(res))
    # res = pickle.loads(f2.read())
    # print(res)
    # print(type(res))
    # print(res.cardnum)
    # print(res.money)