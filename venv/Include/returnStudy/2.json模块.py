#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
json可以直接序列化python基本数据类型。

json.dumps(obj,default)
注意：若obj为python基本数据类型，我们无需写default，直接进行序列化
若obj为自定义的数据类型，这时候default后面跟的是将对象转为基本数据类型的函数
功能：将obj使用default函数转为字典并且序列化为json字符串，并且返回

json.dump(obj,f，default)
功能：将obj使用default函数转为字典并且序列化为json字符串，
并且写入到指定的打开的f中。


json.loads(jsonstr,object_hook)
功能：将jsonstr转为字典，通过object_hook的方法将字典转为对象

json.load(f,object_hook)
功能：读取打开文件的内容，并且将读取的内容转为字典，
通过object_hook的方法将字典转为对象。
'''
import json


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


def per2dict(per):
    return {"name":per.name,"age":per.age}


def dict2per(d):
    return Person(d["name"],d["age"])


if __name__ == '__main__':
    perList = []
    for x in range(10):
        per = Person("lili"+str(x),18)
        perList.append(per)
    # perdict = per2dict(per)
    # str1 = json.dumps(per,default=per2dict)
    # print(str1)
    with open("per.txt","w",encoding="utf-8") as f:
        for per in perList:
            str1 = json.dumps(per, default=per2dict)
            f.write(str1+"\n")
            json.dump(per,f,default=per2dict)

    with open("per.txt","r",encoding="utf-8") as f2:
        for line in f2.readlines():
            obj = json.loads(line,object_hook=dict2per)
            print(obj)
    #     obj = json.load(f2,object_hook=dict2per)
    #     print(obj)

