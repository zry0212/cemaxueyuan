# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/20 23:57
# @File: 3_4document_process.py

# 文件处理具体的应用
# .txt
# .csv(类似于表格）
# .xml文件的读写
# .txt文件的读取
# with open('123.txt','r',encoding='utf-8') as file1:
#     lines=file1.readlines()
#     print(lines)
# #只想获得学生姓名
# for line in lines:
#     print(line.split(',')[0])   #以逗号切片，姓名在[0]的位置

# csv文件的读取，
# 表格的后缀名是.xsl，csv文件的后缀是.csv,逗号分隔值，以纯文本的形式存储表格数据（数字和文本）
import csv
# file3=csv.reader(open('234.csv','r',encoding='utf-8'))
# for stu in file3:
#     print(stu)
# with open('234.csv','r',encoding='utf-8') as file4:
#     lines=file4.readlines()
#     print(lines)
# for line in lines:
#     print(line.split(',')[0])

# csv文件的写入
import csv

stu1 = ['dahan', 'xinjiang']
stu2 = ['yuyan', 'changde']
out = open('234.csv', 'a+', newline = '')  # CSV文件追加内容时会先空一行再加入内容，表示去除空行
writer1 = csv.writer(out, dialect = 'excel')  # CSV文件数字和文本存储数据，dialect='excel'表示声明以表格写入
writer1.writerow(stu1)
writer1.writerow(stu2)

# .xml（可扩展标记语言）类似于html（超文本标记语言）
# xml是用来传输和存储数据，htm是用来显示数据
# xml特点：
# <note> 根元素/根节点(节点值为none）
# 	<dahan id='kw'>zhangsan<dahan> 子元素/子节点
# 	<to>lisi</to>
# 	<from>23</from>
# </note>
# 由标签对组成，并且区分大小写
# 标签里面可以有属性<dahan id='kw'>zhangsan<dahan>里面的id='kw'就是属性
# 标签对里面可以存储数据<to>lisi</to>
# 标签里面可以存放标签<from>23</from>
# xml文档必须包含根元素，这个根节点是所有元素的父元素

# dom文档对象模型：html和xml之间的api接口，每一个对象都是一个节点
# 创建一个xml存储学生数据（姓名/年龄/城市）,账号，密码
# xml的节点有三种：
# 元素节点
# 文本节点
# 属性节点
# 每个节点里包含的信息：节点名称 nodeName 节点值 nodeValue  节点类型 nodeType

# 读取元素节点（节点名称/节点值/节点类型)
# from xml.dom import minidom
# dom=minidom.parse('567.xml')   #加载xml文件
# root=dom.documentElement   #读取对象元素，一般读取根节点元素documentElement
# print(root.nodeName)
# print(root.nodeValue)
# print(root.nodeType)     #节点类型，如果是元素节点返回1，如何是属性节点返回2

# 读取文本节点的值
# from xml.dom import minidom
# dom=minidom.parse('567.xml')
# root=dom.documentElement
# name1=root.getElementsByTagName('name')      #getElementsByTagName根据标签名称获取标签对象
# age1=root.getElementsByTagName('age')
# city1=root.getElementsByTagName('city')
# # print(name1[0].firstChild.data)    .firstChild表示找到标签对应的值
# # print(age1[0].firstChild.data)
# # print(city1[0].firstChild.data)
# for i in range(4):
#     print(name1[i].firstChild.data)
#     print(age1[i].firstChild.data)
#     print(city1[i].firstChild.data)

# 读取属性节点的值：读取老师和学生的账号密码
# from xml.dom import minidom
# dom=minidom.parse('567.xml')
# root=dom.documentElement
# login1=root.getElementsByTagName('login')
# for i in range(2):
#     username1 = login1[i].getAttribute('uername')      #.getAttribute表示获取属性
#     print(username1)
#     password1 = login1[i].getAttribute('password')
#     print(password1)

# 读取子节点信息（节点名称/节点值/节点类型)
from xml.dom import minidom

dom = minidom.parse('567.xml')
root = dom.documentElement
root1 = root.getElementsByTagName('student')
print(root1[0].nodeName)
print(root1[0].nodeValue)
print(root1[0].nodeType)  # 节点类型，如果是元素节点返回1，如何是属性节点返回2
