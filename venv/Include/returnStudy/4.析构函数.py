#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import time
'''
__init__()   实例化对象／创建对象的时候调用
__del__()  对象被销毁的时候调用［当对象被销毁的时候会自动调用析构函数］
'''

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("构造函数被调用啦。。。")

    def __del__(self):
        print("析构函数被调用啦。。。")


if __name__ == '__main__':
    per = Person("lili",18)
    per2 = Person("lili",18)
    # del per
    # time.sleep(2)