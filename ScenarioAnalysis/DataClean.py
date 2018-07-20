# -*- coding: utf-8 -*-
"""
@author: 陈祥明

用于数据的处理
"""

import numpy as np
import pandas as pd

# 将dataframe转成list
def DataframeTolist(Data):
    a = np.array(Data)
    b = a.tolist()
    return b


# 区分dataframe中股票和期货
def StockOrFuture(df, n):
    stock = []
    future = []
    for i in range(0, n):
        a = str(df.index[i])
        if str.isdigit(a) is True:
            stock.append(a)
        else:
            future.append(a)
    return stock, future


# 获取dataframe中指定排序的数据
def getOrder_df(df, col, order=10):
    df0 = df.sort_values(by=col)
    result = float(df0[col][(order - 1):order])
    return result