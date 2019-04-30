#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 14:47
# @Author  : liangman
# @contact: manlinux@sina.cn

# @version: 1.0
# @Site    : 
# @File    : Chi2.py
# @Software: PyCharm
from scipy import stats
import numpy as np
from scipy.stats import chi2_contingency


def custom_chi2_contingency(observed):
    """
    自己编写的卡方检验的函数，返回
    """
    # 每一行求和
    row = observed.sum(axis=1)
    # 每一列求和
    col = observed.sum(axis=0)
    # 总数求和
    all_sum = observed.sum()

    # meshgrid 生成网格
    x1, x2 = np.meshgrid(col, row)
    # 期望频数
    expected_count = x1 * x2 / all_sum
    # 统计量，即卡方值
    chi2 = ((observed - expected_count)**2 / expected_count).sum()
    # 自由度
    df = (len(row) - 1) * (len(col) - 1)
    # 计算 p 值，这里用到了卡方分布的概率积累函数，
    # 因为这个 cdf 是计算从左边到这点的累计积分，因此用 1 减它
    p = 1 - stats.chi2.cdf(chi2, df=df)
    return chi2, p, df, expected_count


obs = np.array([[178, 272], [38, 502]])
result1 = custom_chi2_contingency(obs)
result2 = chi2_contingency(obs)
print('自定义卡方检验的函数返回：')
print(result1)
print()
print('scipy 提供的卡方检验返回：')
print(result2)
