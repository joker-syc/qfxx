#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
鸭子模型：若有一只鸟，走路像鸭子，叫声像鸭子，我们可以称这只鸟就是鸭子。
在python中我们不关心数据的类型，我们只关心数据的属性以及其方法的使用。

真正的多态：
指一个事物的多种表现形态，必须依赖于继承而存在。
isinstance(obj,types)
功能：判断obj是否属于指定的types，或者types的子类
types：也可以是一个元组。若是元组，则判断的是obj是否属于types元组中
的某种类型。
若有一个成立，得到的结果就为True，否则为False。

dir(obj)
功能：可以查看obj所有的属性以及方法以列表的形式返回。
'''


class Animal:

    def __init__(self,name):
        self.name = name

    @staticmethod
    def run(obj):
        # print(isinstance(obj,Animal))
        print("%s跑..."%obj.name)

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Person:
    def __init__(self,name):
        self.name = name


if __name__ == '__main__':
    cat = Cat("Tom")
    print(cat)
    # Animal.run(cat)
    # dog = Dog("jerry")
    # Animal.run(dog)
    # print(isinstance(cat,Animal))
    # # print(isinstance(dog,Animal))
    # per = Person("狗蛋")
    # Animal.run(per)
    # print(isinstance(per,Animal))
    # print(type(cat)==Animal)
    # print(isinstance(cat,(Animal,Cat)))
    # print(dir(cat))




