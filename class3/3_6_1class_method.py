# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/22 1:26
# @File: 3_6_1class_method.py

# 类方法：实例方法/静态方法/类方法，修饰器不同
# @classmethod修饰的方法为类方法
# @staticmethod修饰的方法为静态方法
# 不用任何修饰的方法称为实例方法
class Student:
    @classmethod
    def listen(cls):
        print("这是类方法", cls)

    @staticmethod
    def read(bookname, num):
        print(bookname, num)

    def __init__(self):
        self.name = 'yourname'
        self.color = 'yellow'
    # 也可以在初始化函数中定义变量，实例化对象时传入变量值,例如实例化stu1=Student('张三'，'yellow')
    # def __init__(self, name, color):
    #     self.name = name
    #     self.color = color

    def say(self):
        print('这是实例方法')

    def write(self):
        # 实例方法之间可以嵌套调用
        self.say()
        # 还可以调用__init__中的属性
        print(self.name, '天气好')




# 实例方法通常会有用类对象直接调用
zhangsan = Student()
zhangsan.say()
zhangsan.write()
# 也可以类名调用实例方法，需要手动给self进行参数传递
# Student.say()      #不能直接这样调用
Student.say(zhangsan)  # 可以这样写，需要实例化传值

# 类方法可以使用类名直接调用
Student.listen()
# 类方法也可以使用类对象调用
lisi = Student()
lisi.listen()

# 静态方法（类似函数），和函数的区别只是定义下类里面，不需要绑定像self、cls这样的对象

# 静态方法可以使用类名直接调用,不用先实例化对象
Student.read('安徒生', 18)
# 静态方法也可以使用类对象调用
dahan = Student()
dahan.read('灰姑娘', 10)


class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1   # 想要让conut累加，就不能写成self.count

    @classmethod
    def show_count(cls):
        print(cls.count)   # 这里写cls.cpunt和Tool.count都可以


tool1 = Tool('斧头')
tool2 = Tool('镰刀')
Tool.show_count()