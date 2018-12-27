#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成Twap时间
"""

from datetime import timedelta, datetime
from openpyxl import load_workbook
import os
import pandas as pd
import numpy as np
import pymssql
import math

from WindPy import w

today = datetime.today().strftime('%Y%m%d')
tradebegintime = today[0:4]+'-'+today[4:6]+'-'+today[6:]+' 09:30:00'
tradeendtime = today[0:4]+'-'+today[4:6]+'-'+today[6:]+' 11:30:00'

def endtime(st, period): # 获取截至时间，返回str  'xx:xx'
    t = int(st.split(':')[0])*60+int(st.split(':')[1])+period
    hour = math.floor(t/60)
    min = t % 60
    if len(str(min)) == 1:
        return str(hour)+':0'+str(min)
    else:
        return str(hour) + ':' + str(min)
def timeperiod(st, period): # 获取时间段，返回str  'xx:xx-xx:xx'
    t = int(st.split(':')[0])*60+int(st.split(':')[1])+period
    hour = math.floor(t/60)
    min = t % 60
    if len(str(min)) == 1:
        return st + '-' + str(hour) + ':0' + str(min)
    else:
        return st+'-'+str(hour)+':'+str(min)

def getamountperminute(codei, bt=tradebegintime, et=tradeendtime):
    windcode = w.htocode(codei, "stocka").Data[0][0]
    winobj = w.wsi(windcode, 'amt', beginTime=bt, endTime=et)
    dfperminute = pd.DataFrame(columns=['Data'], data=winobj.Data[0])
    amountperminute = dfperminute.mean()['Data']
    return amountperminute

def getmultipleof5(x):
    remainder = x % 5
    if remainder == 0:
        res = x
    else:
        res = x-remainder+5
    return res


# # 建立数据库连接
conn = pymssql.connect(host='127.0.0.1', user='sa', password='ZAQ!2wsxCDE#', database='ScenarioAnalysis')
cur = conn.cursor()

getprivioustradedatequery = "SELECT  top 1 TradeDate FROM Calendar where TradeDate<'{}' order by TradeDate desc".format(today)
cur.execute(getprivioustradedatequery)
privioustradedate = cur.fetchall()[0][0]

# if_merge = input("是否合并（？y/n）:")
filepath = r'C:\Users\Admin\Desktop\互换执行20180911合并.xlsx' # 测试用
# path = r'Z:\personal\倪振豪\OptionTest\执行'
# files = os.listdir(path)
# for i in files:
#     if today in i:
#         if if_merge == 'y':
#             filepath = path+"\\互换执行"+today + '合并' # 获得当日执行文件路径
#         elif if_merge == 'n':
#             filepath = path + "\\互换执行" + today  # 获得当日执行文件路径
#     else:
#         pass
#
source = pd.read_excel(filepath, converters={'证券代码': str})
source = source[source['证券代码'] != 0] # 剔除掉不可见的空行0
source.set_index('证券代码',inplace=True)

Customer = np.array(source[['客户名称']].drop_duplicates().unstack()).tolist()
# source['time'] = 0

dfli = []

starttimeforsell = input("请输入起始时间：")

w.start()

for client in Customer:
    df = source[source['客户名称'] == client]
    tp = []
    dataset = df.groupby(level=0).max()
    dataset['MV'] = np.nan

    for i in dataset.index:
        query = "SELECT closeprice FROM HistData_Stock where Date='{}' and InstrumentID='{}'".format(privioustradedate,i)
        cur.execute(query)
        closeprice = cur.fetchall()[0][0]
        dataset.at[i, 'MV'] = dataset.at[i, '数量'] * closeprice
