# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/16 23:16
# @File: 2_2Immutable_data.py


# 不可变数据类型：数字型、字符型、元组
import math
import random

a = 3.888
print(math.floor(a))
print(math.ceil(3.1212))
print(random.randint(0, 20))
print(random.random())

# 对字符串进行切片：字符串变量名[开始位置：结束位置：step] ，step默认是1，表示每隔0个取值，取值位置的索引是左闭右开，左边的包含，右边的不包含
str1 = 'abcdef'
str2 = 'adc'
print(str1[0:4])
print(str1[-1])  # 获取最后一个字符
print(str1[:-1])  # 获取除了最后一个的所有字符
print(str1[:])  # 获取全部的字符
print(str1[::2])  # 从左往右隔一个字符取一个
print(str1[::-2])  # 从右往左隔一个字符取一个
print(str1[::-1])  # 实现了字符串的翻转
# 通过的拼接的方式修改字符串,不能直接赋值改变
str1 = str1[:-1] + '1'
print(str1)
print(str1 * 2)  # 把字符串str1复制两遍
if '1' not in str1:  # in/not in
    print('不存在')
else:
    print('存在')

str3 = 'abdcng\n12344'  # \n表示换行
str4 = r'abdcng\n12344'  # r表示转义，换行不生效
print(str3)
print(str4)
str5 = r'C:\Users\hasee'  # 如果不用r转义，则特殊字符识别不了
print(str5)

# 字符串的格式化引入变量,有三种方式
# 1.%需要顺序传值，
# 2.format不需要顺序传值，可以自定义传值位置
print('%s工作年限：%d年' % ('zhangsan', 3))  # %前后分开传入的值
print('{1}工作年限：{0}年'.format('lisi', 4))
# 3.通过f-string，只支持Python3.7以上版本
name = 'wangwu'
age = 18
print(f'{name}帅哥：{age}岁')

# 字符串常见其他内置函数：见网页https://www.runoob.com/python/python-strings.html
# 通过分隔符把字符串链接起来 .join
list1 = ['nihao', 'shijie']
str6 = '-'.join(list1)  # 以-把列表里的元素连接起来返回字符串
print(str6)
list2 = str6.split('-')  # 以-为分隔符，分割成两个，返回分割后的字符串列表,
print(list2)
list3 = str6.rsplit('-')  # rsplit从右边开始分割,但是列表里元素的顺利不变
print(list3)
list3 = str6.rsplit('-', 1)  # 1表示分割成2个,参数可以变

# replace替换某个字符串，除了拼接以外修改字符串的函数
str7 = 'aaabbbccc'
str8 = str7.replace('bbb', '222')
print(str8)

# 元组
# 如果元组只有一个元素，需要在后面加一个逗号，取消除数学歧义
tup3 = (1,)
print(tup3, type(tup3))
# 可以创建任何元素的元组
tup4 = (1, 2, 3, 'haha', [1, 2, 3])
print(tup4[3])
# 去头去尾的访问
print(tup4[1:-1])
print(tup4[1:4])  # 左闭右开
# 元组的更新不能通过直接赋值，要通过切片、连接的方式进行更新
# 把tup4中的haha改成hehe
tup5 = ('hehe',)
tup6 = (tup4[0:3] + tup5 + tup4[4:])  # 拼接时不能直接写成tup4[4]，也可以写成tup[-1:]
print(tup6)
# 复制元组
print(tup6 * 2)
# 删除元组里的元素，不能直接删除元素，只能通过拼接，但是可以删除整个元组
# 把元组转换成列表
print(list(tup6))
