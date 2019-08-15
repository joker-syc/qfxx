#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
列表生成式：将for循环强制性写在一行，然后将结果写在最前面，最后使用
[]将其括起来，我们称这个式子叫做列表生成式。
'''
'''
list1 = [1,2,3,...100]
'''
print(list(range(1,101)))

'''
list2 = [1,4,9,...,10000]
'''
l2 = []
for x in range(1,101):
    l2.append(x*x)
print(l2)

print([x*x for x in range(1,101)])
# print([x*x for x in range(1,101,2)])
'''
list3 = [1,9,25,....,9801]
'''


'''
list4 = [1,2,4,5,7,....,100]
'''
print([x for x in range(1,101) if x%3])

print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))

# print([['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]for x in range(1,10)])

