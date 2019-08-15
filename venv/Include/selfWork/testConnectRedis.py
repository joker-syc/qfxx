#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 14:47
# @Author  : joker-syc
# @Site    : 
# @File    : testConnectRedis.py
# @Software: PyCharm

import redis

# r=redis.Redis(password='123456',decode_responses=True)
# r.set('s','ss')
# print(r.get('s'))

#创建连接池
pool=redis.ConnectionPool(password='123456',decode_responses=True)

#使用连接池对象去连接redis数据库
r=redis.Redis(connection_pool=pool)

# r.delete('s')
r.set('s','sss')
r.delete('s')
print(r.get('s'))
