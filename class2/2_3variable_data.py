# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/18 16:33
# @File: 2_3variable_data.py

# 可变数据类型：列表、字典、集合
# 列表，一种有序集合，可以随时添加和删除列表的元素
lst1 = [1, 2, 3, 4, 5]
print(lst1)
# 访问列表中的元素，列表的切片
print(lst1[0])
print(lst1[1:3])  # 左开右闭
lst2 = lst1[1:3]
print(lst2)
# 访问超出索引的范围，则会报错，索引越界
# 修改list当中元素的值
lst1[0] = 0  # 可以直接访问元素修改
print(lst1)
# 增加元素
# 在末尾增加一个元素.append
# 在指定位置前添加元素.insert(索引位置，元素值）
lst1.insert(1, 'zhangsan')
print(lst1)
# 在末尾增加多个元素.extend()方法
lst3 = [11, 22, 33]
lst1.extend(lst3)
print(lst1)
# 通过append增加多个元素,apppend增加后最后一个元素是一个列表
lst1.append(lst3)
print(lst1)
# 删除元素
lst4 = [20, 21, 22, 23, 24, 25]
lst4.pop()  # 默认删除最后一个元素
print(lst4)
lst4.remove(24)  # remove根据元素的值去删除
print(lst4)
del lst4[-1]
print(lst4)  # del根据元素的索引位置去删除
# 如果列表中有重复的值，只删除一个:
lst5 = [6, 7, 6, 8, 9]
print(lst5.count(6))  # 找到重复的值在列表出现的次数
print(lst5.index(6, 0, len(lst5)))  # 用索引查找index（要查找的元素值，索引开始位置，索引结束位置）6在lst5中返回6的索引位置
del lst5[0]  # 再根据索引进行删除
print(lst5)

# list可以支持的运算：+ * in/not in
lst6 = [2, 3, 1, 5, 4]
lst7 = [6, 8, 7, 9]
lst8 = lst6 + lst7
print(lst8)
# list的其他操作
# .sort列表默认升序排序
lst7.sort()
print(lst7)
# 降序排序.sort（reverse=True)
lst7.sort(reverse = True)
print(lst7)
# list翻转
lst7.reverse()
print(lst7)
# 将列表头尾两个元素对调
lst9 = [1, 2, 3]
lst9 = lst9[::-1]  # [::-1] #顺序相反操作，[3::-1]就是从第3个位置坐标开始 截取顺序相反
print(lst9)

# 字典
# dict={key1:value1,key2:value2,key3:value3}    键值对，key必须是唯一的且不可变
dict1 = {'姓名': '张三', '密码': '123456'}
# 另一种创建字典的方法
student = dict(姓名 = '张三', 密码 = '123456')
student1 = dict([('姓名', '张三'), ('密码', '123456')])
print(dict1)
print(student)
print(student1)
# 访问字典里的元素，一般通过键取访问
print(dict1['姓名'], dict1['密码'])
# 修改字典
dict1['密码'] = 'abcdefg'
print(dict1)
# 增加一个键值对
dict1['地址'] = '武汉'
print(dict1)
# 删除键值对
del dict1['地址']
print(dict1)
# 通过函数删除键值对
dict1.pop('姓名')
print(dict1)
# 删除最后一个键值对
dict1.popitem()
print(dict1)
# 删除整个字典
del dict1
# print(dict1)
# 将列表合并成字典，
key_list = ['a', 'b', 'c']
value_list = [11, 22, 33]
"""zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
Python 3.x 中为了减少内存,zip() 返回的是一个对象"""
D = dict(zip(key_list, value_list))
print(D)

# 字典常见的内置函数
dict1 = {'姓名': '张三', '密码': '123456'}
print(len(dict1))  # len()返回这个数据类型的长度
str1 = str(dict1)  # 将字典转换成字符串
print(str1, type(str1))
# 依次获取字典中key和Vaule的值  items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回
print(dict1.items())
for x, y in dict1.items():
    print(x, y)
# 把下面内容作为字典里的键
lst9 = ['姓名', '密码', '地址', '性别']
dict2 = {}
dict2 = dict2.fromkeys(lst9, 'none')  # dict.fromkeys(seq, val)创建一个新字典以以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
print(dict2)
# 根据列表中的元素作为字典的key，初始值为0，不用fromkey
lst10 = [1, 2, 3, 4, 5]
dict3 = {}
for a in lst10:
    dict3[a] = 0
print(dict3)

# 字典里的成员判断，通过键取判断
if '姓名' in dict2:
    print('存在')
else:
    print('不存在')
# 多个元素进行更新字典
dict3 = {'xingming': 'zahngsan', 'mima': '123456'}
dict4 = {'xingming': 'zahngsan', 'dizhi': 'wuhan', 'xingbie': 'nan'}
dict3.update(dict4)  # 把dict4更新到dict3中，会按照不同的key去更新，自动去重
print(dict3)
# 如果是同一个key，但是值不同，如何更新？
dict5 = {'xingming': 'zahngsan', 'mima': '123456'}
dict6 = {'xingming': 'zahngsan1', 'dizhi': 'wuhan', 'xingbie': 'nan'}
dict5.update(dict6)  # 把dict6更新到dict5中，相同的key取要更新来源的字典dict6
print(dict5)

# 集合，集合中的数据是无顺的，用{},元素可以是任意各种类型，每个元素之间用逗号隔开
set1 = {1, 2, 3, 4, 'hehe', 11}
print(set1, type(set1))
# 创建一个空集合
set2 = {}  # 创建空集合不能这样写，这样写成了字典
print(set2, type(set2))
set21 = set()  # 创建空集合用set(),不是set{}
print(set21, type(set21))
# 创建集合的另外一种方式
set3 = set([1, 6, 3, 4, 3, 5])  # 创建集合，自动去重
print(set3, type(set3))
# 访问集合：集合是无需的，所以不能访问
# 集合支持哪些运算：
# a&b交集：公共的部分
# a|b并集：全部的元素合起来去重
# a-b差集：返回a中元素中去除b中有的元素
# a^b非交集：返回a，b中没有重复的元素
set4 = {1, 2, 3, 4, 5, 6, 7}
set5 = {5, 6, 7, 8, 9, 'haha'}
print(set4 & set5)
print(set4 | set5)
print(set4 - set5)
print(set4 ^ set5)
print('-------------------------')
# 集合常见的内置函数
print(set4.intersection(set5))  # .intersection相当于交集
print(set4.union(set5))  # .union相当于并集
print(set4.difference(set5))  # .difference相当于差集
print(set4.symmetric_difference(set5))  # .symmetric_difference相当于非交集
print('------------------------')
# 集合元素操作的相关函数
set4.add(20)  # 增加元素
print(set4)
set4.pop()  # 随机删除元素，无法指定删除某个位置元素
print(set4)
set4.remove(20)  # remove/discard也是删除元素，区别是discard删除没有的元素时不会报错
print(set4)
set4.discard(100)
print(set4)
# 集合常用的判断函数
set4 = {1, 2, 3, 4, 5, 6, 7}
set5 = {5, 6, 7, 8, 9, 'haha'}
print(set4.isdisjoint(set5))  # 判断两个集合有没有重复的元素，没有返回Ttue，有则返回False
set6 = {1, 2, 3, 4, 5, 6}
set7 = {1, 2, 3}
print(set7.issubset(set6))  # 判断set7是不是set6的子集，是返回True，不是则返回False
print(set6.issuperset(set7))  # 判断set6是不是set7的父集，是返回True，不是则返回False
# 更新集合
set4.update(set5)  # 把set5里的元素更新到set4里去
print(set4)
