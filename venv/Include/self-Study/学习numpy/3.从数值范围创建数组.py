#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 14:28
# @Author  : joker-syc
# @Site    : 
# @File    : 3.从数值范围创建数组.py
# @Software: PyCharm

import numpy as np
#从数值范围创建数组
# a=np.arange(5)
# a=np.arange(1,10,2,dtype=float)      #(start,stop,step)
# print(a)

# a=np.linspace(2,50,5,endpoint=False,retstep=True)          #(start,end,nun,endpoint,retstep,dtype)
#                                    # (起始点,终止点,生成的等差数列的数量,True(默认)包括/False不包括,True显示间距/False(默认)不显示间距,ndarray数据类型)
# print(a)
# print(type(a))                     #当要显示间距时,a的数据类型就变成tuple,相应的参数在里面(不显示间距时,a是ndarray类型)
# print(a[0][1])
# print(a[1])

# a=np.logspace(0,9,9,base=2,endpoint=False)       #使用方法与上面的类似,(start,end,nun,endpoint,base,dtype)
#                                                         #(起始点=nun**base,终止点=nun**base,生成的等比数列的数量(默认为50),True(默认)包括/False不包括,底数base,ndarray数据类型)
# print(a)