#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc

'''
使用,拼接字符串时,   ,会被替换为空格
使用+拼接字符串时,   +不会被替换为空格,但是只能连接相同类型
使用 格式化输出时,既不会产生空格,也可以连接多个不同类型的数据
'''
name=input("请输入你的信息:")
z=""
class  dd():
    for a in name:
        z=z+a
        if a ==" "or a==",":
            z="";
        else:
            print(z)


