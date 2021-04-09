# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/20 22:31
# @File: 3_3osmodule.py

# 文件及os模块
# 打开文件
# file=open(file_name路径，访问模式)

# read()  每次读取整个文件
# readline() 每次读取一行内容
# readlines() 一次性读取整个文件；自动将文件内容分析成一个行的列表
import os

file1 = open('1.txt', 'w')
file1.write('''zhangsan1
zhangsan2
zhangsan3
zhangsan4
zhangsan5
zhangsan6
''')
file1.close()
file2 = open('1.txt', 'r')
print(file2.readline())
# for x in file2.readlines():
#     print(x)

# 读取指定某一行的数据，返回到一个列表中
print(file2.readlines()[1:3])  # 读取指针位置1到3的数据

# a+  对文件内容做追加，指针放在文件末尾去追加,如果源文件不存在，则新建
# w+   先找到文件，然后把指针放在开头，把源文件内容清空，然后再去写入内容，如果源文件不存在，则新建

# 获取文件权限 os.access（path，mode）
# mode：os.F_OK(是否存在） os.R_OK（可读） os.W_OK(可写）os.X_OK(可执行）
file7 = r'C:\Users\hasee\Desktop\python位置.txt'  #
print(os.access(file7, os.F_OK))
print("判断是否可写", os.access(file7, os.W_OK))

# 如何更改文件权限os.chmod（path，mode）
