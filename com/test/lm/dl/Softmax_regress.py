#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-29 23:42
# @Author  : liangman
# @contact: manlinux@sina.cn

# @version: 1.0
# @Site    : 
# @File    : Softmax_regress.py
# @Software: PyCharm

# 参考博客 https://blog.csdn.net/tsyccnh/article/details/79163834
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

## 1.加载数据
# def read_data_sets(train_dir,
#                    fake_data=False,
#                    one_hot=False,
#                    dtype=dtypes.float32,
#                    reshape=True,
#                    validation_size=5000,
#                    seed=None,
#                    source_url=DEFAULT_SOURCE_URL):
data=input_data.read_data_sets("../MINDATA/",one_hot=True)

## 2.定义函数
W = tf.Variable(tf.zeros([784,10]))
b= tf.Variable(tf.zeros([10]))

x=tf.placeholder(dtype=tf.float32,shape=(None,784))

y=tf.nn.softmax(tf.matmul(x,W)+b)


y_=tf.placeholder(tf.float32,shape=(None,10))

cross_entropy=tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y),reduction_indices=[1]))

tran_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

##3.定义评估
# tf.argmax(vector, 1)：返回的是vector中的最大值的索引号，如果vector是一个向量，那就返回一个值，如果是一个矩阵
# ，那就返回一个向量，这个向量的每一个维度都是相对应矩阵行的最大值元素的索引号。
correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
init = tf.global_variables_initializer()

with tf.Session() as sess:
    init.run()
    for i in range(1000):
      batch_x,batch_y =  data.train.next_batch(100)
      sess.run(tran_step,feed_dict={x:batch_x,y_:batch_y})
      print("acc:%s"%accuracy.eval({x:batch_x,y_:batch_y}))

    print("TestSet acc : %s" % accuracy.eval({x: data.test.images, y_: data.test.labels}))


