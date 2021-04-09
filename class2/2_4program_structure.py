# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/18 23:43
# @File: 2_4program_structure.py

# 顺序结构
# 选择结构
# if else
# if elif  else
# 循环结构
# while  满足条件则一直循环，不满组则跳出循环体  whie   else
# for in  用来遍历字符串/列表/元组/字典/集合
# 没有do whie语句，C语言中有
# 一般能用for的时候可以用whie，反过来则不一定
# 当知道循环次数的时候用for，不知道循环次数的时候用while

# 循环嵌套，外循环次数*内循环次数=总共循环次数
# 打印下面的图形
# *
# **
# ***
# ****
# *****
for x in range(1, 6):  # 确定有5行,
    for y in range(0, x):  # 内层循环每行的输出根据与行的关系循环到数
        print('*', end = '')
    print()  # print自带换行

#     *
#    ***
#   *****
#  *******
# *********
for x in range(0, 5):
    for y in range(0, 5 - x):
        print(' ', end = '')
    for z in range(0, x * 2 + 1):
        print('*', end = '')
    print()

#  *******
#   *****
#    ***
#     *
for x in range(0, 4):
    for y in range(0, x + 2):
        print(' ', end = '')
    for z in range(0, 7 - x * 2):
        print('*', end = '')
    print()

for x in range(0, 5):
    for y in range(0, 5 - x):
        print('#', end = '')
    for z in range(0, x * 2 + 1):
        print('*', end = '')
    print()

# break 跳出整个循环
# continue 跳出本次循环
# pass  空语句，占位语句，保证代码的完整性
# 想到去除h不打印
str1 = 'nihaoma'
for i in str1:
    if i == 'h':
        continue
    else:
        print(i)
