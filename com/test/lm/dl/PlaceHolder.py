#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-29 23:27
# @Author  : liangman
# @contact: manlinux@sina.cn

# @version: 1.0
# @Site    : 
# @File    : PlaceHolder.py
# @Software: PyCharm

import tensorflow as tf


A = tf.placeholder(tf.float32,shape=(None,3),name="A")

B = A+5

with tf.Session() as sess:
    B_1 = B.eval(feed_dict={A:[[1,23,4]]})
    B_2 = B.eval(feed_dict={A: [[2, 23, 4]]})
print(B_1)
print(B_2)