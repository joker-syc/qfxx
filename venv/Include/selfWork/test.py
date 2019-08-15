#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc
# import re
#
# txt='<html>  <body>  <h1>my first title</h1>  <p>This is the index page of our website. I like sporting very much, do you like it? He does not like eating chocolate.    you and I</p>  <a href="/dir01/layer011.html">link to layer011.html</a> <hr />  <a href="/dir01/layer012.html">link to layer012.html</a> <hr />  <a href="/dir02/layer021.html">link to layer021.html</a> <hr />  <a href="/dir02/layer022.html">link to layer022.html</a> <hr />  </body>  </html>'
#
#
# re1 = re.findall('href=".*?"',txt)
# print(re1)

# re1='.*?'	# Non-greedy match on filler
# re2='(\\/dir01\\/layer011\\.html)'	# Unix Path 1
# re3='.*?'	# Non-greedy match on filler
# re4='(\\/dir01\\/layer012\\.html)'	# Unix Path 2
# re5='.*?'	# Non-greedy match on filler
# re6='(\\/dir02\\/layer021\\.html)'	# Unix Path 3
# re7='.*?'	# Non-greedy match on filler
# re8='(\\/dir02\\/layer022\\.html)'	# Unix Path 4
#
# rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8,re.IGNORECASE|re.DOTALL)
# m = rg.search(txt)
# if m:
#     unixpath1=m.group(1)
#     unixpath2=m.group(2)
#     unixpath3=m.group(3)
#     unixpath4=m.group(4)
#     print ("("+unixpath1+")"+"("+unixpath2+")"+"("+unixpath3+")"+"("+unixpath4+")"+"\n")

# 爬虫备份
# file=open(seedURL,mode="r")
#     if maxDepth>=0:
#         # print(seedURL)
#         for a in seedURL:
#             if a in haveGetFile:
#                 continue
#             else:
#                 haveGetFile.append(a)
#                 # print(haveGetFile)
#             # 如果一级目录中有 .html文件，则执行get()
#             if a.endswith(".html"):
#                 pass
#                 # print(a)
#                 # get(a)
#             elif a.endswith(".txt"):
#                 File = open(a, mode='r+', encoding='utf-8')
#                 h = File.read()
#                 # print(h)
#             else:
#                 seedURL.pop(seedURL.index(a))
#         for b in targetDir:
#             maxDepth -= 1
#             if maxDepth<=0:
#                 break
#             else:
#                 all(b)
#                 targetDir.pop(targetDir.index(b))
#                 crawler(seedURL,targetDir,2)
#     else:
#         print("已到达抓取深度限制")
#         pass

# 如果一开始的seedURL是个文件目录,则循环遍历该目录下的一级文件,返回该文件的地址
# def all(seedURL):
#     if maxDepth>0:
#         if not os.path.exists(seedURL):
#             print("设置的基础目录不存在")
#         else:
#             aim=os.listdir(seedURL)
#             # print (aim)
#             for file in aim:
#                 fileR=os.path.join(seedURL,file)
#                 if os.path.isfile(fileR):
#                     if fileR in saveFile:
#                         pass
#                     else:
#                         saveFile.append(fileR)
#                         # print (fileR)
#                         # return fileR
#                 elif os.path.isdir(fileR):
#                     if fileR in saveDir:
#                         pass
#                     else:
#                         saveDir.append(fileR)
#                     # print (fileR)
#         # print (saveFile)
#         # print (saveDir)
#         # crawler(saveFile,saveDir,maxDepth)
#     else:
#         pass
                    # return all(fileR)

# def get(sds):
#     # print(dd)
#     htmlFile=open(sds,mode='r+',encoding='utf-8')
#     # print(htmlFile.name)
#     h=htmlFile.read()
#     # h里面竟然是空的......(实际上目标地址的网页本身就是空的...)
#     print(h)
#     dd=BeautifulSoup(h,"html.parser")
#     linkg=dd.find_all("a")
#     print(linkg)
#     for link in linkg:
#         re1 = re.findall('href=".*?"', str(link))
#         print(re1)
#         str1=CharacterProcessing(re1[0])
#
#     htmlFile.close()
#
# def CharacterProcessing(str1):
#     str1=str1.lstrip('href="').rstrip('"')
#     print(str1)
#     str1=str1.replace("/","\\")
#     print(str1)
#     return str1


# a=[]
# if a:
#     print("a")
# else:
#     print("b")

# t=[]
# try:
#     t.pop()
# except:
#     print("dd")

# t=["3",2]
# p=t
# print(p)

# t={1:2,3:4}
# print(str(t))

import requests
from bs4 import BeautifulSoup
import re
import openpyxl
from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
import json
from urllib.request import urlopen, quote

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Host': 'sh.lianjia.com'
}

'''第一步：爬取小区信息'''
def export_communityInfo(xiaoquInfo_list):
    '''导出小区信息'''
    with open('浦东地区小区信息.txt', 'a', encoding='utf-8') as file:
        file.write(','.join(xiaoquInfo_list))
        file.write('\n')

def get_communityInfo(community_url, community_name):
    '''获取某个小区的信息'''
    r = requests.get(url=community_url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    try:
        unitPrice = soup.find(name='span', attrs={'class': 'xiaoquUnitPrice'}).string #小区均价
    except:
        unitPrice = '空'
    try:
        address = soup.find(name='div', attrs={'class': 'detailDesc'}).string #小区地址
        address = '"' + address + '"'
    except:
        address = '空'
    xiaoquInfo = soup.find_all(name='span', attrs={'class': 'xiaoquInfoContent'}) #小区信息
    xiaoquInfo_list = []
    community_name = '"' + community_name + '"'
    xiaoquInfo_list.append(community_name)
    xiaoquInfo_list.append(address)
    xiaoquInfo_list.append(unitPrice)
    for info in xiaoquInfo:
        xiaoquInfo_list.append(info.string)
    xiaoquInfo_list.pop()
    export_communityInfo(xiaoquInfo_list)
    print('已爬取{}的信息'.format(community_name))

def xiaoqu_pachong():
    '''获取所有小区名字和链接'''
    for i in range(1, 100):
        if i == 1:
            i = ""
        else:
            i = 'pg' + str(i)
        url = r"https://sh.lianjia.com/xiaoqu/" + i + "rs浦东/"
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        for j in soup.find_all(name='div', attrs={'class': 'title'}):
            community = str(j)
            if '''target="_blank"''' in community:
                community_list = re.search('''<a href="(.*?)" target="_blank">(.*?)</a>.*?''', community)
                community_url = community_list.group(1)
                community_name = community_list.group(2)
                try:
                    get_communityInfo(community_url, community_name)
                except:
                    print('{}的{}出错了, url是{}'.format(i, community_name, community_url))

'''第二步：数据清洗'''
def clean_data():
    '''数据清洗'''
    pd.set_option('display.max_columns', None)  # 显示所有列
    column_name = ['小区名称', '小区地址', '均价', '建成年份', '建筑类型', '物业费', '物业名称', '开发商', '楼栋数', '住户数']
    xiaoqu_data = pd.read_csv(r'浦东地区小区信息.txt', names=column_name, encoding='utf-8', engine='python')
    xiaoqu_data['建成年份'].replace('年建成', '', regex=True, inplace=True)
    xiaoqu_data['楼栋数'].replace('栋', '', regex=True, inplace=True)
    xiaoqu_data['住户数'].replace('户', '', regex=True, inplace=True)
    xiaoqu_data = xiaoqu_data[xiaoqu_data['住户数'] != '暂无信息']
    xiaoqu_data = xiaoqu_data[xiaoqu_data['建成年份'] != '暂无信息']
    xiaoqu_data = xiaoqu_data[xiaoqu_data['建成年份'] != '暂无信息 ']
    xiaoqu_data = xiaoqu_data[xiaoqu_data['均价'] != '空']
    xiaoqu_data = xiaoqu_data[xiaoqu_data['小区地址'] != '空']
    xiaoqu_data = xiaoqu_data.dropna(subset=['均价'])
    xiaoqu_data = xiaoqu_data[xiaoqu_data['建成年份'].astype(int) >= 1975]
    # print(xiaoqu_data['建成年份'].unique)
    xiaoqu_data = xiaoqu_data[xiaoqu_data['住户数'].astype(int) >= 10][['小区名称', '小区地址', '建成年份', '均价', '楼栋数', '住户数']]
    xiaoqu_data['楼均住户数'] = xiaoqu_data['住户数'].astype(int) / xiaoqu_data['楼栋数'].astype(int)
    xiaoqu_data['小区年龄'] = 2020 - xiaoqu_data['建成年份'].astype(int)
    xiaoqu_address = xiaoqu_data['小区地址'].str.split(')', expand=True, n=1)
    xiaoqu_address.columns = ['区域', '地址']
    xiaoqu_address['区域'] = xiaoqu_address['区域'].str[1:]
    xiaoqu_address['地址'] = '浦东新区'+ xiaoqu_address['地址']
    xiaoqu_data = pd.merge(xiaoqu_data, xiaoqu_address, how='left', left_index=True, right_index=True)
    xiaoqu_data = xiaoqu_data[xiaoqu_data['楼均住户数'] <= 200][['小区名称', '区域', '地址', '小区年龄', '均价', '楼均住户数', '楼栋数', '住户数']]
    xiaoqu_data[['均价', '楼栋数', '住户数']] = xiaoqu_data[['均价', '楼栋数', '住户数']].astype(int)
    xiaoqu_data.drop_duplicates('小区名称', 'first', inplace=True)
    # print(xiaoqu_data)
    xiaoqu_data.to_excel(r"小区数据.xlsx", encoding='gbk', index=False)

'''第三步：数据补充'''
def getjwd_bd(address):
    '''根据地址获得经纬度（百度）'''
    url = 'http://api.map.baidu.com/geocoding/v3/?address='
    output = 'json'
    ak = '********'#需填入自己申请应用后生成的ak
    add = quote(address) #本文城市变量为中文，为防止乱码，先用quote进行编码
    url2 = url+add+'&output='+output+"&ak="+ak
    req = urlopen(url2)
    res = req.read().decode()
    temp = json.loads(res)
    lng = float(temp['result']['location']['lng'])  # 经度 Longitude  简写Lng
    lat = float(temp['result']['location']['lat'])  # 纬度 Latitude   简写Lat
    return lng, lat

def getjwd_gd(address):
    '''根据地址获得经纬度（高德）'''
    parameters = {'address': address, 'key': '********'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    # print(answer)
    jwd = answer['geocodes'][0]['location'].split(',')
    lng = jwd[0]
    lat = jwd[1]
    return lng, lat

def get_distance(lng1,lat1,lng2,lat2):
    '''计算到人民广场的距离'''
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371  # 地球平均半径，6371km
    distance = round(distance, 0)
    return distance

def get_bd_distance():
    '''获得地址的经纬度和到人民广场的距离（百度）'''
    wb = openpyxl.load_workbook('小区数据.xlsx')
    ws = wb['Sheet1']
    maxrow = ws.max_row
    for i in range(2, maxrow + 1):
        address = ws["C" + str(i)].value.split(',')[0]
        address2 = '上海市浦东新区' + ws["A" + str(i)].value
        try:
            temp_list = getjwd_bd(address)
        except:
            try:
                temp_list = getjwd_bd(address2)
            except:
                temp_list = getjwd_bd(address)
        lng = temp_list[0]
        lat = temp_list[1]
        bd_rmgc_lat = 31.23453
        bd_rmgc_lng = 121.48187
        distance = get_distance(lng, lat, bd_rmgc_lng, bd_rmgc_lat)
        ws['J1'].value = '到人民广场的距离（百度）'
        ws["J" + str(i)].value = distance
        print("{}的经度是{}，纬度是{}，到人民广场的距离是{}".format(address, lng, lat, distance))
    wb.save('小区数据.xlsx')
    wb.close()

def get_gd_distance():
    '''获得地址的经纬度和到人民广场的距离（高德）'''
    wb = openpyxl.load_workbook('小区数据.xlsx')
    ws = wb['Sheet1']
    maxrow = ws.max_row
    for i in range(2, maxrow + 1):
        address = ws["C" + str(i)].value.split(',')[0]
        address2 = '上海市浦东新区' + ws["A" + str(i)].value
        try:
            temp_list = getjwd_gd(address)
        except:
            try:
                temp_list = getjwd_gd(address2)
            except:
                temp_list = getjwd_bd(address)
        lng = temp_list[0]
        lat = temp_list[1]
        gd_rmgc_lat = 31.22872
        gd_rmgc_lng = 121.47518
        distance = get_distance(lng, lat, gd_rmgc_lng, bd_rmgc_lat)
        ws['I1'].value = '到人民广场的距离（高德）'
        ws["I" + str(i)].value = distance
        print("{}的经度是{}，纬度是{}，到人民广场的距离是{}".format(address, lng, lat, distance))
    wb.save('小区数据.xlsx')
    wb.close()

def get_right_distance(arrlike):
    '获取正确的距离'
    distance1 = arrlike['高德距离']
    distance2 = arrlike['百度距离']
    mean_distance = arrlike['平均距离']
    std_distance = arrlike['标准差距离']
    lower_distance = mean_distance - std_distance*1.96
    upper_distance = mean_distance + std_distance*1.96
    if (lower_distance <= distance1 <= upper_distance) and (lower_distance <= distance2 <= upper_distance):
        right_distance = (distance1 + distance2) / 2
    elif (lower_distance <= distance1 <= upper_distance) and (distance2 < lower_distance or distance2 > upper_distance):
        right_distance = distance1
    elif (lower_distance <= distance2 <= upper_distance) and (distance1 < lower_distance or distance1 > upper_distance):
        right_distance = distance2
    else:
        right_distance = mean_distance
    return right_distance

def get_last_data():
    '''根据高德和百度获得的距离，根据以下规则判定最终距离：
    1、获取每个区域的I和J列的数据（也就是用高德和百度获得的到人民广场的距离）；
    2、根据上述数据，获取每个区域的平均数和标准差；
    3、如果I和J都在平均数上下1.96个标准差之内的，按两者平均数取值；
    4、如果I和J只有一个在平均数上下1.96个标准差之内的，按在里面的取值；
    5、如果I和J都不在里面的，按区域平均数取值；
    '''
    xiaoqu_data2 = pd.read_excel(r'小区数据.xlsx')[['区域', '到人民广场的距离（高德）', '到人民广场的距离（百度）']]
    xiaoqu_data2.rename(columns={'到人民广场的距离（高德）': '高德距离', '到人民广场的距离（百度）': '百度距离'}, inplace=True)
    xiaoqu_data3 = xiaoqu_data2[['区域', '高德距离']].rename(columns={'高德距离': '距离'})
    xiaoqu_data4 = xiaoqu_data2[['区域', '百度距离']].rename(columns={'百度距离': '距离'})
    xiaoqu_data5 = pd.concat([xiaoqu_data3, xiaoqu_data4])
    quyu_mean = xiaoqu_data5.pivot_table(index='区域', values='距离', aggfunc=np.mean).reset_index().rename(
        columns={'距离': '平均距离'})  # 区域均值
    quyu_std = xiaoqu_data5.pivot_table(index='区域', values='距离', aggfunc=np.std).reset_index().rename(
        columns={'距离': '标准差距离'})  # 区域标准差
    xiaoqu_data5 = pd.merge(xiaoqu_data2, quyu_mean, how='left', left_on='区域', right_on='区域')
    xiaoqu_data6 = pd.merge(xiaoqu_data5, quyu_std, how='left', left_on='区域', right_on='区域')
    xiaoqu_data6['正确距离'] = xiaoqu_data6.apply(get_right_distance, axis=1)
    xiaoqu_data7 = pd.read_excel(r'小区数据.xlsx')
    final_xiaoqu_data = pd.merge(xiaoqu_data7[['小区名称', '区域', '地址', '小区年龄', '均价', '楼均住户数', '楼栋数', '住户数']],
                                 xiaoqu_data6['正确距离'], how='left', left_index=True, right_index=True)
    # print(final_xiaoqu_data)
    final_xiaoqu_data.to_excel(r"小区数据（清洗完毕）.xlsx", encoding='gbk', index=False)

if __name__ == '__main__':
    #第一步：数据爬取
    xiaoqu_pachong()
    #第二步：数据清洗
    clean_data()
    #第三步：获取经纬度和到人民广场的距离
    get_bd_distance()
    get_gd_distance()
    # 第四步：根据高德和百度获得的距离，根据规则判定最终距离
    get_last_data()
