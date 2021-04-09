# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/21 22:44
# @File: 3_6_0class.py

# 类是对象的抽象集合，对象是类的具体表现
# 类class是描述具有相同属性和方法的对象的集合，它定义了该集合中每个对象所共有的属性和方法
# 数据成员（属性）：类的不同属性数据，所有类中的变量称为属性
# 对象：对象是类的实例
# 方法：类中定义的函数，实现相关的功能
class Student():
    name = 'yourname'  # 类属性或类变量，所有类的实例化对象都同时共享类变量
    color = 'yellow'

    def __init__(self, name, city):
        self.name = name  # self.name称为实例属性/实例变量
        self.city = city

    def listen(self, music):  # 实例方法
        self.musicname = '演员'  # 实例变量
        print('学生听音乐')


class Egg():
    def cont(self, money):
        sale = 0.8 * money  # 直接在方法里定义的变量叫局部变量，只作用于这个函数
        print('优惠后的价格为', sale)


# 类方法的调用方式有两种，既可以使用类名直接调用，也可以使用类的实例化对象调用
print(Student.name)  # 使用类名直接调用
print(Student.color)  # 使用类名直接调用
Student.name = 'nidemingzi'  # 可以修改类变量的值
Student.color = 'pink'
print(Student.name)
print(Student.color)
zhangsan = Student('张三', 'pink')
print(zhangsan.name)  # 用类对象来调用所属类中的类变量
print(zhangsan.color)

# 实例变量：以'self.变量名'方式定义的变量，实例变量只能通过对象名访问，无法通过类名访问
wangwu = Student('王五', '北京')
print(wangwu.name)
print(wangwu.city)
# print(wangwu.musicname)        #不能这样直接调用
wangwu.listen(1)  # 对象wangwu先调用了listen方法，才会有.musicname的实例变量
print(wangwu.musicname)

# 局部变量 以变量名=变量值得方式定义
duckegg = Egg()
duckegg.cont(100)

# 内置属性：通过类进行调用
print(Student.__doc__)
print(Student.__name__)
print(Student.__module__)
print(Student.__base__)
print(Student.__dict__)
