#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
递归函数：
函数的内部可以调用其他的函数，但是若调用的这个函数正好是他自己本身的时候，
我们称这个函数为递归函数。

不建议使用递归
1.考虑栈溢出
2.递归性能不如循环

思路：
1.写出临界条件
2.找出这次与上次的关系
3.假设此函数已经可以使用，通过上次的结果计算本次的结果
'''

'''
求1+2+3+...+n
n = 1  res = 1
f(1) = 1
f(2) = f(1)+2
f(3) = f(2)+3
...
f(n) = f(n-1)+n
'''
def f(n):
    if n == 1:
        return 1
    else:
        return f(n-1)+n
print(f(10))
print(f(100))

# f(5)
# print(f(1000))
'''
求斐波那契数列：1,1,2,3,5,8,13,21,34,55,89.....
找临界值
f(1) = 1
f(2) = 1
f(3) = f(1)+f(2)
f(n) = f(n-1)+f(n-2)
'''

def func(n):
    if n==1 or n==2:
        return 1
    else:
        return func(n-1)+func(n-2)

print(func(4))
print(func(5))
print(func(6))
print(func(7))
print(func(40))

