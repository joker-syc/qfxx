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
conn.select_db('school')
#3.设置连接输出结果的字符集
conn.set_charset('utf8')
#4.创建游标对象(方便遍历执行sql操作后返回的结果集)
cursor=conn.cursor()
#5.初始化sql操作(sql语句)





