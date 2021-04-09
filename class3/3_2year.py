# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/20 16:18
# @File: 3_2year.py
# 计算1900年1月1日到今天（2019年12月20日）相距多少天
sum = 0
for year in range(1900, 2019):  # 先算1900到2018的天数
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # 判断为闰年的条件
        sum = sum + 366
    else:
        sum = sum + 365
for month in range(1, 13):  # 再算2019/1/1到2019/12/20
    if month in [1, 3, 5, 7, 8, 10, 12]:  # 先算大小月
        sum = sum + 31
    elif month in [4, 6, 9, 11]:
        sum = sum + 30
    else:
        if (2019 % 4 == 0 and 2019 & 100 != 0) or (2019 % 400 == 0):  # 再算是否是润年的2月
            sum = sum + 29
        else:
            sum = sum + 28
print(sum - 11)  # 12/20到12/31多算了11天
