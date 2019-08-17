#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 14:47
# @Author  : joker-syc
# @Site    : 
# @File    : testConnectRedis.py
# @Software: PyCharm

import redis
print('string类型的使用')
r=redis.Redis(password='123456',decode_responses=True)
r.set('s','ss')
print(r.get('s'))
print(r.ttl('s'))
r.expire('s',10)
print(r.ttl('s'))
r.persist('s')
print(r.ttl('s'))
r.delete('s')
print('列表的使用')
r.lpush('dd','?','??','???')
print(r.lrange('dd',0,-1))
print(r.lindex('dd',1))
r.lpop('dd')
r.lpush('dd','????')
print(r.lrange('dd',-2,-1))
print(r.lindex('dd','2'))
print(r.llen('dd'))
r.delete('dd')
print('哈希类型的使用')
r.hset('zz',1,'2')
print(r.hget('zz',1))
r.hmset('zz',{3:'4',5:'6'})
# r.hmset('zz',['a','b','c','d'])        #必须是成对出现的
# r.hmset('zz',[['a','b'],['c','d']])        #必须是成对出现的  看来列表是不行的
print(r.hgetall('zz'))
print(r.hexists('zz',6))
print(r.hexists('zz',1))
print(r.hkeys('zz'))
print(r.hvals('zz'))
r.hdel('zz','3')
r.delete('zz')
print('有序集合的使用')
r.zadd('dd',{'/':1,'//':2})
print(r.zcard('dd'))
r.zadd('dd',{'///':4,'////':3})
print(r.zrange('dd',0,-1))          #根据分数进行升序排序
print(r.zrevrange('dd',0,-1))       #根据分数进行降序排序
print(r.zscore('dd','/'))           #返回指定元素的分数
r.delete('dd')


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
