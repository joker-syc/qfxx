#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
函数重写 __str__系统提供的函数
当调用str／print的时候会自动调用此函数，此函数是给用户使用的，
用来描述对象的显示。

注意：__str__函数的返回值必须是一个字符串，并且当调用print的时候
打印对象的结果就是此函数的返回值

若在类中存在__repr__，但是不存在__str__,
我们可以使用 __str__ = __repr__
'''


class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "%s-%d"%(self.name,self.age)

    __str__ = __repr__


if __name__ == '__main__':
    per = Person("lili",18)
    print(per)
    print(str(per))


