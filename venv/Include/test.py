# # Python包含6中内建的序列：列表、元组、字符串、Unicode字符串、buffer对象和 xrange 对象。序列通用的操作包括：索引、长度、组合（序列相加）、重复（乘法）、分片、检查成员、遍历、最小值和最大值
#
# # List[].sort()的key用法
# # 获取列表的第二个元素
# def takeSecond(elem):
#     #这里取到了列表中的列表
#     # 然后取出这个列表的第二个元素
#     return elem[1]
#
# # 列表
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
#
# # 指定第二个元素排序
# # 大于该元素的排前面，小于的排后面
# # key指的是相比较的元素（基准）
# random.sort(key=takeSecond)
#
# # 输出类别
# print("1.排序列表：",random)
#
# # 字符串操作实例
# a="a"
# if a in "abc":
#        print("2.dd")
# #        字符串可以向List一样检索
# else:print("2.gg")
#
# a="abc"
# for b in a:
#        print("3."+b)
# #        可以循环遍历
#
# print("4."+a[1])
# # 可以提取数据
#
# # a[1]="gg"
# # print(a)
# # 这个会报错，字符串是不可变对象,不能用下标赋值的方式去改变字符串。
#
# # List[].sort()的普遍用法
# aList=["1","a",'A','c','b',"2"];
# aList.sort();
# print("5.")
# print (aList)