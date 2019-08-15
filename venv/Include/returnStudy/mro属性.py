#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-

class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

class D(A,B):
    pass

class E(B, C):
    pass

class F(D, E):
    pass

print(F.__bases__)
print(F.__mro__)