#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
单例模式
饿汉式
懒汉式
'''

class Person:


    def __init__(self,name):
        self.name = name
        print("init方法被调用了")

    def __new__(cls, *args, **kwargs):
        print("new方法被调用了")


class Singleton(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) #创建实例
        return cls.__instance

    def __init__(self, number):
        self.number = number


# 项目重构
if __name__ == '__main__':
    # per = Person("lili")
    # per2 = Person("lili")
    # print(id(per))
    # print(id(per2))

    singl = Singleton("123")
    singl2 = Singleton("122")
    print(singl)
    print(singl2)
    print(singl.status_number)
    print(singl2.status_number)
    print(singl is singl2)

