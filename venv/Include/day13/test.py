#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 0024 9:54
# @Author  : joker-syc
# @Site    : 
# @File    : test.py
# @Software: PyCharm

#最好不要给默认参数设置可变类型

# class Animal:
#
#     def __init__(self,name):
#         self.name=name
#
#     def __move(self):
#         print('%s可以动'%self.name)
#
#     def m(self):
#         self.__move()
#
#     def eat(self):
#         print('%s会吃东西'%self.name)
#
# class Cat(Animal):
#
#     def nao(self):
#         print('%s会挠人'%self.name)
#
# class Dog(Animal):
#
#     def destory(self):
#         print('%s会拆家'%self.name)
#
#
# if __name__ == '__main__':
#     animal=Animal("dd")
#     # animal.__move()
#     animal.m()
#
#     cat=Cat('傻猫')
#     # cat.__move()
#     # cat.m()
#     cat.nao()
#
#     dog=Dog('傻狗')
#     # dog._move()
#     dog.destory()

#python的多态:鸭子模型(只要一个,叫声像鸭子,走路的样子像鸭子,我们就认为他是鸭子)
#python的多态是假多态,我们不关心数据的类型,但关心数据的属性以及方法的使用

#yield 关键字 可以将函数变为生成器,可以多次返回 多次执行
#用next()获取