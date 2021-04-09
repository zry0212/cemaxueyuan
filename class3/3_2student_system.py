# -*- coding: utf-8 -*-
# 姓名：zry
# @time: 2021/2/20 14:40
# @File: 3_2student_system.py

str1 = """---------------欢迎进入学生管理系统--------------------
0：显示所有学员信息\n
1：添加一个学员信息\n
2：删除一个学员信息\n
3：修改一个学员信息\n
4：查询一个学员信息\n
exit：退出学生管理系统\n
请选择系统功能：
"""
# 定义一个列表存放学生信息
mylist = ['张三', '李四', '王五', '赵六']


def getallinfo():
    print(mylist)
    studentsystem(input(str1), mylist)         #运行完一次后可以重复运行


def addinfo():
    mylist.append(input('请输入增加的学员姓名：'))
    print('增加学员后所有学员信息：', mylist)
    studentsystem(input(str1), mylist)         #运行完一次后可以重复运行


def delinfo():
    delname = input('请输入要删除学员姓名:')
    if delname in mylist:
        # if mylist.count(delname)>0:             #另一种方法判断要删除的姓名是否在系统中
        mylist.remove(delname)
        print('删除学员后所有学员信息：', mylist)
        studentsystem(input(str1), mylist)         #运行完一次后可以重复运行
    else:
        print('输入的学员不在系统中')


def updateinfo():
    oldname = input('请输入要修改学员姓名:')
    newname = input('请输入修改后的学员姓名：')
    if mylist.count(oldname) > 0:
        mylist[mylist.index(oldname)] = newname
        print('修改学员后所有学员信息：', mylist)
    else:
        print('要修改的学员不在系统中')
        studentsystem(input(str1), mylist)         #运行完一次后可以重复运行


def selectinfo():
    selectname = input('请输入要查询学员姓名：')
    if mylist.count(selectname) > 0:
        print(str(selectname) + '在座位号' + str(mylist.index(selectname)) + '的位置')
        studentsystem(input(str1), mylist)         #运行完一次后可以重复运行
    else:
        print('系统中没有这个学员')


def studentsystem(num, mylist):
    if num == '0':
        getallinfo()
    elif num == '1':
        addinfo()
    elif num == '2':
        delinfo()
    elif num == '3':
        updateinfo()
    elif num == '4':
        selectinfo()
    elif num == 'exit':
        print('退出学生系统，欢迎下次使用')
    else:
        print('输入的内容超出功能范围')
        studentsystem(input(str1), mylist)


studentsystem(input(str1), mylist)
