#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 上午10:58
# @Author  : liangman
# @contact: manlinux@sina.cn

# @version: 1.0
# @Site    : 
# @File    : Student.py
# @Software: PyCharm
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getName(self):
        print(self.name)


def run():
    stu = Student("testABm",12)
    stu.getName()
    print("stu is instance",isinstance(stu,Student))
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')








if __name__ == '__main__':
    run()
