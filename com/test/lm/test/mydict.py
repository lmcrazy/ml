#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 下午2:09
# @Author  : liangman
# @contact: manlinux@sina.cn

# @version: 1.0
# @Site    : 
# @File    : mydict.py
# @Software: PyCharm

class MyDict(dict):
    def __init__(self,**kw):
        super(MyDict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


