#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import json
'''
json只能序列化python的标准类型。

'''

class Card:
    def __init__(self,cardnum,password,money,islock=False):
        self.cardnum = cardnum
        self.password = password
        self.money = money
        self.islock = islock

card = Card("101110","110",110,True)


def card2dict(card):
    return {"cardnum":card.cardnum,"password":card.password,"money":card.money,"islock":card.islock}


def dict2card(d):
    return Card(d["cardnum"],d["password"],d["money"],d["islock"])

# dict1={"name":"lili","age":18,"hobby":None,"sex":True}
# print(str(dict1))


with open("card.txt","w",encoding="utf-8") as f:
    f.write(json.dumps(card,default=card2dict))


with open("card.txt","r",encoding="utf-8") as f2:
    res = json.loads(f2.read(),object_hook=dict2card)
    print(res)
    print(type(res))
