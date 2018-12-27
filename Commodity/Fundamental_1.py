#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
导入基本面因子组成结构
"""

import pandas as pd
import numpy as np
from WindPy import w
from SQLLINK import SASQL

def DataCleanWind(Windobj): # 处理万得返回的数据，将Wind对象处理成list
    df = pd.DataFrame(columns=Windobj.Fields, index=Windobj.Times)  # 将wind返回的对象处理成dataframe
    for m in range(0, len(Windobj.Fields)):
        df[Windobj.Fields[m]] = Windobj.Data[m]
    return df

dbdc = SASQL.DataCenter_Commodity()
category = pd.read_excel(r'D:\CXM\Project\Commodity\基本面因子组成结构表.xlsx')

w.start()

for i in range(0,category.shape[0]):
    print(category.iat[i,1])
    obj = w.wsd(category.iat[i,7], "close", "2010-01-01", "2018-11-26", "")
    df = DataCleanWind(obj)
    data = pd.DataFrame()
    data['TradingDate'] = df.index
    data['ProductID'] = category.iat[i,1]
    data['ProductName'] = category.iat[i, 0]
    data['IndexName'] = category.iat[i, 2]
    data['Secu_Arrb'] = category.iat[i, 3]
    #print(np.array(df[['CLOSE']].unstack()).tolist())
    # data['Closeprice'] = np.array(df[['CLOSE']].unstack()).tolist()
    data['Closeprice'] = np.array(df[['CLOSE']])
    data['Unit'] = category.iat[i, 4]
    data['Frequency'] = category.iat[i, 5]
    data['DataSource'] = category.iat[i, 6]
    # print(data[['Closeprice']])

    data.to_sql('Commodity_Spot', dbdc.conn, if_exists='append', index=False, chunksize=1000)
    del data
