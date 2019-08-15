#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 0008 20:35
# @Author  : joker-syc
# @Site    : 
# @File    : 全排列问题的解法.py
# @Software: PyCharm

'''输入一个字符串，打印出该字符串中字符的所有排列。
例如输入字符串abc，则输出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。'''

#递归解法(没必要去关注其所有过程,只需要知道把'指针'移动到下一位,并交给问题规模更小的函数就行,最后要在函数出来之后恢复arr即可)
# def dd(arr,position,end):
#     if position==end:
#         print(arr)
#     else:
#         for index in range(position,end):
#             arr[index],arr[position]=arr[position],arr[index]
#             dd(arr,position+1,end)
#             arr[index],arr[position]=arr[position],arr[index]
#
# arr=['a','b','c','d']
# dd(arr,0,len(arr))
# a='▒'
# print(ord(a))