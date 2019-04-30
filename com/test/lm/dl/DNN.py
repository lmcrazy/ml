#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-27 18:05
# @Author  : liangman
# @contact: manlinux@sina.cn

# @version: 1.0
# @Site    : 
# @File    : DNN.py
# @Software: PyCharm
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


samples = stats.chi2.rvs(size=10000, df=1)
sns.distplot(samples)
plt.title('$\chi^2$,df=1')
plt.show()
