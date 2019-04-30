#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 下午5:53
# @Author  : liangman
# @contact: manlinux@sina.cn

# @version: 1.0
# @Site    : 
# @File    : cut_data.py
# @Software: PyCharm

import jieba
import re

jieba.load_userdict("dict.txt")
# fp=open("dict.txt",'r',encoding='utf8')

# for line in fp:
#     line=line.strip()
#     jieba.suggest_freq(line,tune=True) #修改频率值
[ jieba.suggest_freq(line,tune=True) for line in open("dict.txt",'r',encoding='utf8') ]

if __name__=="__main__":
    str="台中正确应该不会被切开"
    words=jieba.cut(str,HMM=False)
    result=" ".join(words)
    print(result)