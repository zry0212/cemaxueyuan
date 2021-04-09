# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/19 22:06
# @File: 3_1function.py

# 函数，自定义函数
# 参数的传递  形参  实参
# 值传递适用于不可变类型：字符串 数字 元组，不可变对象作为函数参数，通过函数体后不能修改函数外变量的值
# 引用传递使用可变类型 列表 字典，可变对象作为函数参数，通过函数体可以改变函数外变量的值
list1 = [1, 2, 3, 4]


def changelist(listn):
    list1.append(listn)


changelist([5, 6, 7, 8])
print(list1)  # 引用传递，函数外的变量list1被改变


# 参数类型：必须参数，关键字参数，默认参数，不定长参数
# 1.必须参数：定义了几个形参，传入必须就有几个实参
def hanshu(canshu1, canshu2):
    print(canshu1, canshu2)


# hanshu('chuanru1')    不能这样写，因为函数中有两个参数要传入
# 2.关键字参数：是一个特殊的必须参数
hanshu(canshu2 = 'heihei', canshu1 = 'haha')  # 关键字识别参数，可以不按顺序写


# 3.默认参数：在定义过程中定义了默认值
def hanshu2(canshu1, canshu2 = 'morenzhi'):  # 一般默认值放在后面,否则会出错
    print(canshu1, canshu2)


hanshu2('chuanru3')  # 定义了默认值得形参可以不用传入实参，只传一个也可以
hanshu2('chuanru3', 'chuanru4')  # 定义了默认值得形参也可以传入新的值，会覆盖默认值，也可以用关键字传


# 4.不定长参数：在定义过程中，不确定会有多少个参数，就设置成不定长参数
# 参数前带一个*,把不定长参数存储在元组里，可以通过元组调用其中某一个参数
def a(name, *canshuming):
    print(name)
    print(canshuming)


a('张三', '17', '武汉')


# 参数前带**，把不定长参数存储在字典里
def b(name, **canshuming):
    print(name)
    print(canshuming)


b('李四', nianlin = '20', dizhi = '长沙')  # 形参是存在字典里，调用参数时需要声明键值对，不然会报错


# *可以单独出现，在调用的时候必须通过关键字传值
def c(num1, num2, *, num4):
    return num1 + num2 + num4


print(c(1, 2, num4 = 4))  # 星号前的实参可以直接传，星号后的实参必须用关键字传


# 不定长形参可以单独存在，*和**的不定长参数可以同时定义
def a2(*yu):
    print(yu)


a2('dadakdhakdha')


def a3(*shican1, **shican2):
    print(shican1)
    print(shican2)


a3(1, 2, 3, nianlin = 18, name = 'lisa')

# 函数的嵌套
# 调用嵌套，函数和函数之间可以互相调用
# 定义嵌套，在函数里定义函数
# 函数自己调用自己会出现死循环，避免出现函数的递归
# 匿名函数：lambda表达式   只有一行表达式的函数
# 通过匿名函数求和
sum1 = lambda a, b: a + b  # 只能接表达式，不是代码块
print(sum1(7, 8))
# 匿名函数与函数的区别：匿名函数不可以使用其他变量，只能对内部参数做运算，函数可以使用函数外的参数

# 模块，一个.py文件就是一个模块
