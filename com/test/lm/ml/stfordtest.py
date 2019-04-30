#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 下午1:41
# @Author  : liangman
# @contact: manlinux@sina.cn

# @version: 1.0
# @Site    : 
# @File    : stfordtest.py
# @Software: PyCharm
from stanfordcorenlp import StanfordCoreNLP
import tensorflow as tf
print(tf.__version__)
nlp = StanfordCoreNLP(r'/Users/lm/PycharmProjects/stanford',lang='zh')
with open("/Users/lm/PycharmProjects/text/news.txt",mode="r",encoding="utf8") as fd:
    for lin in fd:
        line = lin.strip()
        if len(lin)<1:
            continue
        print(" ".join([ a[0] +"/"+ a[1] for a in nlp.ner(line) if len(line) >2 ]))


