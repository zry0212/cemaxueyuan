# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/18 21:58
# @File: 3_5time_module.py

#时间相关模块
import time
#时间戳
#时间元组
t=(2020,10,13,20,16,22,0,0,0)
print('当前时间的时戳：',time.time())
print('当前时间的时间元组：',time.localtime())
print('通过英文的方式表示当前时间：',time.asctime())
print('获取时间元组的部分信息：',time.localtime().tm_year
      ,time.localtime().tm_mon
      ,time.localtime().tm_mday)

#表示方式的相互转换
#元组转化为时间戳
print('元组转换为时间戳：',time.mktime(t))
#当前系统时间转换成时间戳
print(time.mktime(time.localtime()))
#时间戳转换为时间元组
print(time.localtime(1502591382))
print('当前时间戳转换为时间元组:',time.localtime(time.time()))

#元组转换为时间格式字符串,注意区分大小写
print('当前时间转换成时间格式的字符串:',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

#时间格式字符串转换成时间元组,后面的格式描述不能少
print('时间格式字符串转换成时间元组:',time.strptime('2021-02-21 21:00:09','%Y-%m-%d %H:%M:%S'))

#datatime模块，表示日期时间
import datetime
print(datetime.datetime(2021,2,21,21,37,50))  #以时间元组创建日期时间，年月日时必写，时分秒不填默认00:00:00
print(datetime.datetime.now())   #获取当前时间，精确到微秒
print(datetime.datetime.today())   #获取当前时间

#时间表示形式相互转换
print('当前日期时间转换成时间戳',datetime.datetime.now().timestamp())   #
print('把时间戳转换成日期时间',datetime.datetime.fromtimestamp(1613914941.140178))
print('日期时间转换成时间格式字符串',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('时间字符串转换成日期时间',datetime.datetime.strptime('2021-02-21 21:47:44','%Y-%m-%d %H:%M:%S'))

#日历模块
import calendar
print('打印年历',calendar.calendar(2020))
print('打印月历',calendar.month(2021,2))
print('判断是否为闰年',calendar.isleap(2020))
print('判断所给日期是星期几',calendar.weekday(2020,10,13))
print('当前日期是星期几',time.localtime().tm_wday)
print('当前日期是星期几',datetime.datetime.now().weekday())

import arrow
from datetime import datetime

now = arrow.utcnow().to('local')
print(now)
date = now.datetime
print(date)
# 当前时间以day区间所在的区间
print(now.span('day'))
# 以当前时间的hour区间的开始
print(now.floor('hour').datetime)
# 以当前时间的hour区间的结尾
print(now.ceil('hour').datetime)
# 以昨天时间的day区间的开始
last_now = now.shift(days = -1)
print(last_now.floor('day').datetime)

# 获取当前日期的日
print(datetime.now().day)
# isocalendar()返回指定日期的年，第几周，周几这三个值放在元组里
print(datetime.now().isocalendar()[1])
# 当前时间是星期几
print(datetime.now().weekday())
# 当前时间是几月
print(datetime.now().month)
# 当前时间是几年
print(datetime.now().year)




#异常处理函数，可以让自动化测试不因为发生异常而停止测试
#python的异常处理的语法结构
# try.......except........
# try........except.as
# try.......except...as......else
# try.......except........finally
# raise
# try:
#     num1=int(input('请输入数字'))
#     print(num1+10)
# except ValueError:              #发生异常是就执行except下的语句
#     print('输入的不是数字')
#except 后可以定义具体的异常类型
# 常见的错误类型：
# FileNotFoundError 找不到文件
# NameError     没有初始化对象
# BaseException  所有异常的基类，可以捕获所有错误，不知道错误类型时可以写这个
# ValueError     数据的值错误
# try:
#     file1=input('请输入要打开的文件名：')
#     open('%s.txt'%file1)
# except FileNotFoundError:
#     print('文件没有找到')

#捕获系统给的提示信息
# try:
#     file1=input('请输入要打开的文件名：')
#     open('%s.txt'%file1)
# except BaseException as msg:     #发生异常时执行except后的语句
#     print(msg)

# try:
#     file1=input('请输入要打开的文件名：')
#     open('%s.txt'%file1)
# except BaseException as msg:
#     print(msg)
# else:            #没有异常时执行else后的语句
#     print('没问题')

# try:
#     file1=input('请输入要打开的文件名：')
#     open('%s.txt'%file1)
# except BaseException as msg:
#     print(msg)
# finally:             #不管是否有异常都会执行finally后的语句
#     print('输入完毕')

#raise：先定义异常条件，符合条件时抛出异常,只能用于python中的标准异常类，一旦执行了raise语句，raise后面的语句将不能执行
def division(x,y):
    if y==0:
        raise ZeroDivisionError('不能为0')
    return x/y
try:
    print(division(12,0))
except BaseException as e:
    print(e)