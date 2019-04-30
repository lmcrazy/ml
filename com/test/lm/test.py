#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 上午11:48
# @Author  : liangman
# @contact: manlinux@sina.cn

# @version: 1.0
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import logging

logging.basicConfig(level=logging.INFO,filename='new.log',filemode='w',format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def run():
    pass

def foo(s):
    n=int(s)
    return 10/n


if __name__ == '__main__':
    a='0'
    logging.info(foo(a))


