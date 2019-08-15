#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc

#目标网页:  http://top.baidu.com/buzz?b=1&fr=topindex   百度实时热点排行榜
import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime
import os
saveDataDir='\\saveData\\'
def getDataFromWeb():
    web=requests.get(url=r"http://top.baidu.com/buzz?b=1&fr=topindex")
    web.encoding="gb2312"
    soup=BeautifulSoup(web.text,"lxml")
    # # print(soup.find_all("a"))
    hotPoints=[]
    # 查看源网页,确定要爬的内容的特殊标签,根据这个来筛选
    #爬热点名称
    for a in soup.find_all("a"):
        aa=str(a)
        if '''"./buzz?b''' in aa or '''title="''' in aa or '''class="info_title"''' in aa:
            continue
        elif '''href_top''' in aa:
            # print(aa)
            hotPoints.append(aa)
        message=[]
    #爬热点指数
    Hot_spot_index=[]
    for index in soup.find_all('span'):
        bb=str(index)
        if '''class="icon-rise"''' in bb or '''class="icon-fall"''' in bb :
            Hot_spot_index.append(bb)
    # print(Hot_spot_index)
    # print(len(Hot_spot_index))

    #     最后通过正则来提取信息
    for b in hotPoints:
        hotPoint=re.search('''>(.*?)</a>''',b)
        message.append(hotPoint.groups())
    # print(message)

    hot_spot_index=[]
    for hot in Hot_spot_index:
        hot_point=re.search('''>(.*?)</span>''',hot)
        hot_spot_index.append(hot_point.groups())
    # print(hot_spot_index)

    # 输出并存储
    timeNow=str(datetime.now())
    print("%s百度热点事件"%timeNow+"\t\t指数")
    # print(type(timeNow))
    e=1
    try:
         with open(file='C:\\Users\\Administrator\\PycharmProjects\\workhard\\venv\\Include\\selfWork\\saveData\\'+timeNow[0:10]+'.txt',mode="a",encoding="GB18030") as file1 :
             file1.write(timeNow + "\t\t指数" + '\n')
             grup = 0
             value = 0
             # 奶奶的,被反爬了!!!
             # print(len(message))
             # print(message)
             # print(len(hot_spot_index))
             for c in message:
                 for d in c:
                     print("%d." % e + d + "\t\t\t\t%s" % hot_spot_index[grup][value])
                     file1.write("%d." % e + d + "\t\t\t\t%s" % hot_spot_index[grup][value] + '\n')
                     e += 1
                     grup += 1
             #     print()
    except:
        print("路径错误")



if __name__=="__main__":
    for a in range(1000):
        getDataFromWeb()
        time.sleep(30)