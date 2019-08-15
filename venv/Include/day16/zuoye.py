#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 0029 17:23
# @Author  : joker-syc
# @Site    :
# @File    : zuoye.py
# @Software: PyCharm
#
# import re
# from bs4 import BeautifulSoup
#
# def getData(url):
#     with open(file=url,mode='r',encoding='utf-8') as f:
#         # print(f.read())
#         data=re.findall('<span>\n{3}(.*?)</span>',f.read(),re.S)
#         dataList=[]
#         for a in data:
#             b=a.replace('<br>',' ')
#             b=b.replace('\n','')
#             # print(b)
#             # print(type(b))
#             data[data.index(a)]= b
#         print(data)
#         with open(file='data.txt',mode='w',encoding='utf-8') as d:
#             for e in data:
#                 d.write(e)
#                 d.write('\n')
#         # soup=BeautifulSoup(f.read(),"html.parser")
#         # data=soup.find_all('span')
#         # # print(data)
#         # dd=[]
#         # for a in data:
#         #     if 'span class=' in str(a) or 'img' in str(a) or 'href' in str(a):
#         #         continue
#         #     else:
#         #         dd.append(a)
#         # # print(dd)
#         # realData=[]
#         # for b in dd:
#         #     print(a)
#         #     zz=re.findall('<span>(.*?)</span>',b)
#         #     # zzd=re.findall('\S',str(zz))
#         #     realData.append(zz)
#         # print(realData)
# if __name__ == '__main__':
#     getData(r'C:\Users\Administrator\PycharmProjects\workhard\venv\Include\day16\qiushibaike.htm')

