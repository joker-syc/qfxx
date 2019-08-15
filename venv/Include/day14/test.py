#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 0025 9:17
# @Author  : joker-syc
# @Site    : 
# @File    : test.py
# @Software: PyCharm

#copy.deepcopy()  深拷贝可以拷贝类型!!!

class Test:

    def __new__(cls, *args, **kwargs):
        print("dd")

    def __init__(self):
        print("ss")

test=Test()

class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, status_number):
        self.status_number = status_number


singl = Singleton("123")
singl2 = Singleton("122")
print(singl)
print(singl2)
print(singl.status_number)
print(singl2.status_number)
print(singl is singl2)


'''
with open(file,mode,encoding,...) as f :
    f.read()
file:文件位置
mode:读取模式   rb 以二进制读取
encoding:读取的编码格式
'''

def readAndWrite(nun):
    with open(file='test.txt',mode='a',encoding='utf-8') as f:
        for a in range(nun):
            f.write('shadiao')

readAndWrite(3)

import os
def readAndWrite(path):
    dirlist=os.listdir(path)
    print(dirlist)
    filelist=[]
    for a in dirlist:
        filelist.append(os.path.join(path, a))
        if os.path.isdir(os.path.join(path,a)):
            for dd in os.listdir(os.path.join(path,a)):
                filelist.append(os.path.join(path,a)+"\\"+dd)
    # print(filelist)
    c=0
    for b in filelist:
        # print(b)
        if os.path.exists(os.path.join(path,"target")):
            pass
        else:
            os.mkdir(os.path.join(path,"target"))
        if os.path.isdir(b):
            if os.path.exists(os.path.join(path,"target")+'\\'+dirlist[c]):
                pass
            else:
                os.mkdir(os.path.join(path,"target")+'\\'+dirlist[c])
            c+=1
            continue
        # print(dirlist[c])
        with open(file=os.path.join(path,"target")+'\\'+dirlist[c],mode='w',encoding='utf-8') as f:
            with open(file=filelist[c],mode='r',encoding='utf-8') as  e:
                # print(filelist[c])
                f.write(e.read())
                c+=1

readAndWrite('C:\\Users\\Administrator\\PycharmProjects\\workhard\\venv\\Include\\day14')

'''
1.将字典写入文件,读出字典
'''
def writeFile(file):
    path=r'C:\Users\Administrator\PycharmProjects\workhard\venv\Include\day14\test.txt'
    with open(file=path,mode='r',encoding='utf-8') as f:
        # f.write(str(file))
        print(f.read())

    # with open(file=path,mode='w',encoding='utf-8') as d:
    #     print(d.read())

writeFile({1:2,3:4})

'''
2.将对象写入文件,读出对象
'''
class Person:

    def __init__(self,name,sex,phonenumber):
        self.name=name
        self.sex=sex
        self.phonenumber=phonenumber

    def person2dict(self):
        return {"name":self.name,"sex":self.sex,"phonenumber":self.phonenumber}

    @staticmethod
    def dict2person(dict1):
        person=Person(dict1['name'],dict1['sex'],dict1['phonenumber'])
        return person

if __name__ == '__main__':
    person=Person("沙雕",'男','123455')
    print(person.person2dict())
    print(type(person.person2dict()))
    dict1=person.person2dict()
    print(Person.dict2person(dict1))
    print(type(Person.dict2person(dict1)))
    print(Person.dict2person(dict1).name)

