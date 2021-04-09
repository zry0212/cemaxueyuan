# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/22 14:38
# @File: 3_6_2built-in_method.py

#常用内置方法
class Student():
    name='yourname'    #类属性或类变量，所有类的实例化对象都同时共享类变量
    color='yellow'
    __weight=48         #私有属性
    def __init__(self,name,city,weight):
        self.name=name           #self.name称为实例属性/实例变量
        self.city=city
        self.__weight=weight
        print('调用构造方法','我是%s，来自%s'%(name,city))
    def __del__(self):
        print('释放对象会调用__del__方法')
    def __str__(self):
        return ('这是一个自定义实例输出的方法')
    def __getattribute__(self, item):    #所有通过对象访问的属性（包括类属性）都会被拦截，而直接通过类访问类属性则不会
        if(item=='name'):
            print(item)
    def listen(self,music):     #实例方法
        self.musicname='演员'   #实例变量
        print('学生听音乐')
        return self.__weight     #在类里调用私有属性
    def __mini(self):            #定义一个私有方法
        print('这是一个私有方法')

# zhangsan=Student('张三','长沙')
# print(zhangsan)       #先调用__init__，然后调用__str__，最后调用_del_，__getattribute__没有被调用
# print(zhangsan.color)
# print(zhangsan.name)     #__getattribute__被调用

#私有方法和私有属性
#以__开头去定义私有方法，私有方法不能在类外部使用，只能在内部使用
#私有属性，以__开头定义，不能在类的外部访问，且不能直接访问，使用时候是用self.类的私有属性表示
zhangsan=Student('张三','长沙',100)
#zhangsan.__weight          #不能这样在类外调用私有属性
# print(zhangsan._Student__weight)   #可以用对象._类名+私有属性名  这样来在类外调用私有属性，一般不建议这样使用
# print(zhangsan.listen('好运来'))
# zhangsan._Student__mini()      #私有方法不可以通过对象调用,不能直接写zhangsan.__mini()

#私有方法的实际应用
class Test:
    def __send_msg(self):
        print('正在发送信息')
    def send_msg(self,new_money):
        if new_money>100:
            self.__send_msg()
        else:
            print('余额不足')
wangwu=Test()
wangwu.send_msg(20)