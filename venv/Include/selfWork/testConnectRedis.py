#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 14:47
# @Author  : joker-syc
# @Site    : 
# @File    : testConnectRedis.py
# @Software: PyCharm

import redis

r=redis.Redis(password='123456',decode_responses=True)
r.set('s','ss')
print(r.get('s'))
print(r.ttl('s'))
r.expire('s',10)
print(r.ttl('s'))
r.persist('s')
print(r.ttl('s'))
r.delete('s')

r.lpush('dd','?','??','???')
print(r.lrange('dd',0,-1))
print(r.lindex('dd',1))
r.lpop('dd')
r.lpush('dd','????')
print(r.lrange('dd',0,-1))
r.delete('dd')

r.hset('zz',1,'2')
print(r.hget('zz',1))
r.hmset('zz',{3:'4',5:'6'})
# r.hmset('zz',['a','b','c','d'])        #必须是成对出现的
# r.hmset('zz',[['a','b'],['c','d']])        #必须是成对出现的  看来列表是不行的
print(r.hgetall('zz'))
print(r.hexists('zz',6))
print(r.hexists('zz',1))

r.delete('zz')


# #创建连接池
# pool=redis.ConnectionPool(password='123456',decode_responses=True)
#
# #使用连接池对象去连接redis数据库
# r=redis.Redis(connection_pool=pool)
#
# # r.delete('s')
# r.set('s','sss')
# r.delete('s')
# print(r.get('s'))
