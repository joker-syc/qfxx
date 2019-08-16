#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 0014 11:46
# @Author  : joker-syc
# @Site    : 
# @File    : tryToConnectMysql.py
# @Software: PyCharm

import pymysql

#1.创建数据库连接对象
conn=pymysql.connect(host='localhost',user='root',password='123456')
#2.选择操控的数据库
conn.select_db('test')
#3.设置连接输出结果的字符集
conn.set_charset('utf8')
#4.创建游标对象(方便遍历执行sql操作后返回的结果集)
cursor=conn.cursor()
#5.初始化sql操作(sql语句)
sql='select * from student'
# #6.执行要执行的sql语句
# cursor.execute(sql)              #一般不用这种方式,而是要用一个变量接收
# #7.接收并处理结果集
# print(cursor.fetchone())
#
# print(cursor.fetchall())

#6.执行要执行的sql语句
dd=cursor.execute(sql)
#7.接收并处理结果集
print(dd)         #这里打印的是结果集中的元素数量
print(cursor.rowcount)
print(cursor.rownumber)

print(cursor.fetchone())
print(cursor.rownumber)
print(cursor.fetchall())

# cursor.scroll()
print(cursor.fetchone())
print(cursor.rownumber)
print(cursor.fetchall())
print(cursor.rownumber)

conn.begin()
try:
    sql='select * from student where ssex="男"'
    a=cursor.execute(sql)
except:
    conn.rollback()
else:
    print('dd')
    print(cursor.fetchall())
    conn.commit()
#8.关闭游标
cursor.close()
#9.关闭数据库连接
conn.close()





