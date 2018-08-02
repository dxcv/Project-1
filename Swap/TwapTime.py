#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成Twap时间
"""

from datetime import timedelta, datetime

import os
import pandas as pd
import numpy as np
import pymssql
import tushare as ts

df = ts.get_today_ticks('000001')
print(df)

# today = datetime.today().strftime('%Y%m%d')
# yestoday = (datetime.today() + timedelta(-1)).strftime('%Y%m%d')
#
# path = r'C:\Users\ZHAIYUE\Desktop'
#
# files = os.listdir(path)
#
# for i in files:
#     if today in i:
#         filepath = path+"\\"+i #获得当日执行文件路径
#     else:
#         pass
# for file in files:

# df = pd.read_excel(filepath, converters = {'证券代码': str}).fillna(0)
# df = df[df['证券代码'] != 0] #剔除掉不可见的空行0
# df['time'] = 0
# dataset = df.groupby('证券代码').sum()
#
#
# conn = pymssql.connect(host='127.0.0.1', user='sa', password='20180515', database='ScenarioAnalysis')
# cur = conn.cursor()
#
# for i in dataset.index:
#     query = "SELECT closeprice FROM HistData_Stock where Date='{}' and InstrumentID='{}'".format(yestoday, i)
#     cur.execute(query)
#     closeprice = cur.fetchall()[0][0]
#     mv = dataset.loc[i][0]*closeprice
#     condition = df.loc[df['证券代码'] == i, '方向'] == 'sell'
#     if condition.iloc[0] == True:
#         if mv >= 1000000.0:
#             df.loc[df['证券代码'] == i, 'time'] = '13:30-13:45'
#         elif 100000.0 <= mv < 1000000.0:
#             df.loc[df['证券代码'] == i, 'time'] = '13:30-13:40'
#         else:
#             df.loc[df['证券代码'] == i, 'time'] = '13:30-13:31'
#     else:
#         if mv >= 1000000.0:
#             df.loc[df['证券代码'] == i, 'time'] = '13:45-14:00'
#         elif 100000.0 <= mv < 1000000.0:
#             df.loc[df['证券代码'] == i, 'time'] = '13:45-13:55'
#         else:
#             df.loc[df['证券代码'] == i, 'time'] = '13:45-13:46'
#
#
# df['TwapPrice'] = np.nan
# df['期末价格'] = np.nan
#
# df.to_excel(filepath,index=None)