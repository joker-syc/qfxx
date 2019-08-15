#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import doctest
'''
文档测试：
提取注释中的代码来进行执行，要求注释中的代码必须严格的按照python解释器
模式来进行书写。
'''


def myadd(a,b):
    '''
    :param a:
    :param b:
    :return: a+b
    >>> myadd(1,2)
    4
    '''
    return a+b