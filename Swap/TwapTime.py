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
import math
# import tushare as ts
#
from WindPy import w

tradebegintime = str(datetime.today().year)+'-'+str(datetime.today().month)+'-'+str(datetime.today().day)+' 09:30:00'
tradeendtime = str(datetime.today().year)+'-'+str(datetime.today().month)+'-'+str(datetime.today().day)+' 11:30:00'


def endtime(st, period): # 获取截至时间，返回str  'xx:xx'
    t = int(st.split(':')[0])*60+int(st.split(':')[1])+period
    hour = math.floor(t/60)
    min = t%60
    if min == 0:
        return str(hour)+':'+str(min)
    else:
        return str(hour) + ':' + '00'
def timeperiod(st, period): # 获取时间段，返回str  'xx:xx-xx:xx'
    t = int(st.split(':')[0])*60+int(st.split(':')[1])+period
    hour = math.floor(t/60)
    min = t%60
    if min == 0:
        return st + '-' + str(hour) + ':' + '00'
    else:
        return st+'-'+str(hour)+':'+str(min)

def getamountperminute(i, bt=tradebegintime, et=tradeendtime):
    windcode = w.htocode(i, "stocka").Data[0][0]
    winobj = w.wsi(windcode, 'amt', beginTime=bt, endTime=et)
    df = pd.DataFrame(columns=['Data'] ,data=winobj.Data[0])
    amountperminute = df.mean()['Data']
    return amountperminute

def getmultipleof5(x):
    remainder = x%5
    if remainder == 0:
        res = x
    else:
        res = x-remainder+5
    return res

conn = pymssql.connect(host='127.0.0.1', user='sa', password='ZAQ!2wsxCDE#', database='ScenarioAnalysis')
cur = conn.cursor()

#获取前一个交易日的日期
today = datetime.today().strftime('%Y%m%d')
getprivioustradedatequery = "SELECT  distinct top 1 [Date] FROM [ScenarioAnalysis].[dbo].[HistData_Stock] where Date<'{}' order by Date desc".format(today)
cur.execute(getprivioustradedatequery)
privioustradedate = cur.fetchall()[0][0]

#读取今日互换的文件
path = r'C:\Users\ZHAIYUE\Desktop'  #查找执行文件夹
files = os.listdir(path)
for i in files:
    if today in i:
        filepath = path+"\\"+i #获得当日执行文件路径
    else:
        pass

# 数据清洗
df = pd.read_excel(filepath, converters={'证券代码': str}).fillna(0)
df = df[df['证券代码'] != 0] #剔除掉不可见的空行0
df['time'] = 0
dataset = df.groupby('证券代码').sum()
dataset['MV'] = 0


for i in dataset.index:
    query = "SELECT closeprice FROM HistData_Stock where Date='{}' and InstrumentID='{}'".format(privioustradedate, i)
    cur.execute(query)
    closeprice = cur.fetchall()[0][0]
    dataset.loc[dataset.index == i, 'MV'] = dataset.loc[i]['数量']*closeprice

condition = df.loc[df['证券代码'] == i, '方向'] == 'sell'
tp = []

starttimeforsell = input("请输入起始时间")
w.start()
for i in dataset.index:
    condition = df.loc[df['证券代码'] == i, '方向'] == 'sell'
    if condition.iloc[0] == True:
        averageamount = getamountperminute(i)
        timeneeded = getmultipleof5(math.ceil(dataset.loc[dataset.index == i, 'MV']/averageamount)*5)
        df.loc[df['证券代码'] == i, 'time'] = timeperiod(starttimeforsell, timeneeded)
        tp.append(timeneeded)
    else:
        pass

if len(tp) == 0:
    starttimeforbuy = starttimeforsell
elif len(tp) == 1:
    starttimeforbuy = endtime(starttimeforsell, tp[0])
else:
    a = tp.sort()
    starttimeforbuy = endtime(starttimeforsell, tp.sort()[-1])



for i in dataset.index:
    condition = df.loc[df['证券代码'] == i, '方向'] == 'buy'
    if condition.iloc[0] == True:
        averageamount = getamountperminute(i)
        timeneeded = getmultipleof5(math.ceil(dataset.loc[dataset.index == i, 'MV'] / averageamount)*5)
        df.loc[df['证券代码'] == i, 'time'] = timeperiod(starttimeforbuy, timeneeded)
    else:
        pass

df['TwapPrice'] = np.nan
df['期末价格'] = np.nan

conn.close()
df.to_excel(filepath,index=None)