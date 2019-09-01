#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 0031 8:59
# @Author  : joker-syc
# @Site    : 
# @File    : test1.py
# @Software: PyCharm
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

neigh = KNeighborsClassifier(n_neighbors=3)

#身高、体重、鞋的尺寸

X = np.array([[181,80,44],[177,70,43],[160,60,38],[154,54,37],

     [166,65,40],[190,90,47],[175,64,39],[177,70,40],

     [159,55,37],[171,75,42],[181,85,43]])
# img=plt.imshow(X)
# plt.show()
print(X)

y = ['male','male','female','female','male','male','female','female','female','male','male']

# 第1步：训练数据

neigh.fit(X,y)

# 第2步：预测数据

Z = neigh.predict(np.array([[190,70,43],[168,55,37]]))

# print(type(Z))
print(Z)
#输出结果为 ['male' 'female']  说明前面一个是女性  后面一个是男性