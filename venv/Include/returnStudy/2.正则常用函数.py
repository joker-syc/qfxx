#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
re.compile(pattern,flags)
功能：将正则表达式编译成一个对象，返回一个对象模式，
需要正则的时候调用这个编译好的对象即可

re.match(pattern,string,flags)
功能：从字符串的开始来进行匹配，若匹配成功则返回匹配成功的对象
若匹配不成功则返回None。
注意：它是一个不完全匹配，若匹配成功之后，string还有剩余，仍然视为匹配
成功，若想完全匹配，我们需要在正则表达式后面添加$

re.search(pattern,string,flags)
功能：使用正则在string中进行查找，若找到第一个匹配则立即返回，若没有匹配上
则返回None

re.findall(pattern,string,flags)
 功能：查找所有的符合正则表达式的字符串并且以列表的方式返回，若没有找到
 则返回空列表。

 re.finditer(pattern,string,flags)
 功能：查找所有的符合正则表达式的字符串并且以迭代器的方式返回，若没有找到
 则返回空的迭代器。［迭代器中存储的是匹配成功的对象］

 re.split(pattern,string,maxsplit,flags)
功能：以指定的正则表达式对指定的字符串来进行切片处理，返回一个切片后的列表。

re.sub(pattern,repl,string,count,flags)
功能使用repl替换指定的pattern匹配到的字符串，count指定替换次数，默认全部替换。


'''
import re

# obj = re.compile(r"^\w{5,8}\.com$")
# res = obj.findall("112334.com")
# res2 = obj.findall("334.com")
# print(res)
# print(res2)

print(re.match("1\d{10}","123456789456"))
print(re.match("1\d{10}$","123456789456"))
print(re.match("1\d{10}$","213456789456"))

print(re.search("1\d{10}","123456789456123456789089").group())
print(re.findall("1\d{10}","123456789456123456789089"))
reobj = re.finditer("1\d{10}","2345678945623456789089")
print(reobj)

print(re.split(r"[a-z]+","2346sdfESDFGHghj34SDFG56dfg3456fgh45f",maxsplit=2,flags=re.I))
print(re.sub(r"[a-z]+","","2346sdfESDFGHghj34SDFG56dfg3456fgh45f",flags=re.I))