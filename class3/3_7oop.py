# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/22 16:56
# @File: 3_7oop.py

#封装/继承/多态
# 创建封装的类
# 先分析以下：
# 公共的特性  人类
# # 具体的对象    小明/小美
# # 对象的属性    姓名/体重
# # 要实现的功能   跑步/吃东西
class Person:
    def __init__(self,weight,name):
        self.weight=weight
        self.name=name
    def running(self):
        self.weight-=0.5
        print(f'因为跑步，所以体重减少，现在的体重是{self.weight}')          #format的简写方式

    def eating(self):
        self.weight+=1
        print(f'因为嘴馋，所以体重增加，现在的体重是{self.weight}')
xiaoming=Person(75,'小明')
xiaoming.running()
xiaoming.eating()

#继承 子类拥有和父类及父类中封装的所有属性和方法，继承分为单继承和多继承
# class People:      #父类
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def speak(self):
#         print('说话')
#     def sleep(self):
#         print('睡觉')
# class Student(People) :    #子类
#     def speak(self):       #子类里可以有父类相同的方法
#         # People.speak(self)
#         print('子类里的说话')
#
# zhangsan=Student('张三',18)       #Student一定要传入参数，因为继承了父类，父类中有构造函数
# zhangsan.speak()                 #先调用子类里的方法，若方法名相同，就近原则：根据方法名先调用自己类里的方法，再找父类里的方法
# zhangsan.sleep()
#继承的作用：
#1.子类可以重写父类的方法
#2.子类扩展父类的方法
#要同时调用子类和父类的同一个方法；在子类的方法里调用父类People.speak(self)

#多继承：有多个父类名 class 类名（父类1，父类2,......)
# class People:      #父类
#     # def __init__(self,name,age):   #一个py文件中的类中一般只有一个init方法，若有两个则以就近原则运行，后面的int方法会被屏蔽，无法调用
#     #     self.name=name
#     #     self.age=age
#     def speak(self):
#         print('说话')
#     def sleep(self):
#         print('睡觉')
#
# class Pythonstudent():
#     def speak(self):
#         print('我是pythonstudent')
#
# class Javastudent():
#     def speak(self):
#         print('我是Javastudent')
#
# class Student(Pythonstudent,Javastudent) : #多继承，两个父类中的方法名相同，只执行从左到右的第一个方法？？？
#     def __init__(self,name):
#         self.name=name
#     def hear(self):
#         print('子类里的说话')
#
# lisi=Student('李四')
# lisi.speak()

#多态：不同的子类调用相同的方法它会执行不同的代码
class wx:
    def pay(self):
        print('微信支付')
class zfb:
    def pay(self):
        print('支付宝支付')
class yl:
    def pay(self):
        print('银行卡支付')
def start_pay(object):        #这句里的object不能少
    object.pay()
wx1=wx()
start_pay(wx1)
zfb1=zfb()
start_pay(zfb1)
yl1=yl()
start_pay(yl1)

class A:
    def method(self):
        print('A')
class B(A):
    pass
class C(A):
    def method(self): #父类的里method方法已经被重写覆盖，运行子类的method方法就不再运行父类的method
        print('C')
class D(B,C):
    pass
D().method()

#python2.x执行的顺序是D B A C A 输出结果是A，因为运行到B类后调用到A类了，然后再运行到C类中时有相同的方法就不再调用了（相当于父类里的方法已经被子类重写了）
#python3.x执行的顺序是D B C A 输出结果是C，因为运行到B直接pass，再运行C里的method方法（子类优先运行自己类里的方法）后再调用A类，但相同名称的方法method不运行

# class Father:
#     def __init__(self,hobby):
#         self.hobby=hobby
#     def say(self):
#         print('我是爸爸，我的爱好是',self.hobby)
# class Mother:
#     def __init__(self,food):
#         self.food=food
#     def say1(self):
#         print('我是妈妈，我喜欢的食物是',self.food)
# class Son(Father,Mother):
#     pass
# zhangsan=Son('跑步')       #有构造函数，必须传入hobby的参数
# zhangsan.say()
# zhangsan.say1()   #不能调用say1，say1要用到food的值，有两个init方法，就近原则Father中的init方法已经遮蔽了Mother中的init方法，所有就没有值传到food


class Father:
    def __init__(self,hobby):
        self.hobby=hobby
    def say(self):
        print('我是爸爸，我的爱好是',self.hobby)
class Mother:
    def __init__(self,food):
        self.food=food
    def say1(self):
        print('我是妈妈，我喜欢的食物是',self.food)
class Son(Father,Mother):
    def __init__(self,hobby,food):
        super().__init__(hobby)              #调用Father类的构造方法
        # super(Father,self).__int__(hobby)     #执行效果和上一行相同
        # Father.__init__(self,hobby)          #使用未绑定方法调用Father类的构造方法
        Mother.__init__(self,food)           #调用其他父类的构造方法，需要给self传值
zhangsan=Son('跳舞','熟食')       #有构造函数，必须传入hobby的参数
zhangsan.say()
zhangsan.say1()