# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2019/7/23 0023 9:43
# # @Author  : joker-syc
# # @Site    :
# # @File    : test.py
# # @Software: PyCharm
# import copy
# a=[1,2]
# b=[a]*3
# c=copy.deepcopy(b)
# c[0].append(99)
# print(c)
# print(id(c[0]))
# print(id(c[1]))
# print(id(b[0]))
# #这里的主要原因是c中的3个a的确经过深拷贝后与b中的a不同,但是c中的3个a却用的是同一个地址
# #如果要杜绝这种情况,就不能用上面的赋值方式
#
# #这个a[:]指的是a的浅拷贝
# c=[a[:],a[:],a[:]]
# c[0].append(99)
# print(c)
# print(b)
# print(id(c[0]))
# print(id(c[1]))
# print(id(b[0]))

'''
成员方法:专门给对象使用的方法
(在没有创建对象时用类名直接调用成员方法则会报错,如果在此之前创建了则不会)

静态方法:在类中的,但是与类和对象都没啥关系的方法,在外部,类和对象都可以调用该方法
使用@staticmethod进行标记

类方法:是绑定在类身上的一类方法,专门给类使用的,
当使用此方法时,会将类自身传入到方法中,作为第一个参数.
创建此方法时,使用@classmethod 进行标记
'''
# class Pizza:
#     def __init__(self,size):
#         self.size=size
#         if size==7:
#             self.price=49
#         elif size==10:
#             self.price=79
#         elif size==12:
#             self.price=99
#     def change(self):
#

# class Boss:
#
#     def __init__(self,name,money,car):
#         self.name=name
#         self.__money=money
#         self.__car=car
#
#     @property          #代表getter方法
#     def car(self):
#         return self.__car
#
#     @car.setter        #代表setter方法
#     def car(self, car):
#         self.__car = car
#
#     def outMoney(self,nun):
#         if nun<=1000:
#             print("借你钱")
#         else:
#             print("不借")
#
# if __name__ == '__main__':
#     boss=Boss("dd",100000000000,"QQ")
#     # boss.outMoney(1000)
#     # boss.outMoney(10000)
#     print(boss.car)
#     boss.car="大奔"
#     print(boss.car)

class women:

    def __init__(self,name,age1):
        self.name=name
        self.age=age1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if 0<=age<=120:
            print("ok")
        else:
            print("骗子")

if __name__ == '__main__':
    women1=women("沙雕",120)
    women2=women("美女",900)

