#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新优矿股票数据
"""
import uqer
from uqer import DataAPI
import numpy as np
import pandas as pd
import gc
from datetime import datetime
import sys
sys.path.append(r'D:\CXM\Project_New\DataCenter_Uqer')
import Constant
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import MSSQL

date = Constant.today

dbqu = MSSQL.DB_DataCenter_Uqer()


query_getcode = "select Code from Stock_BasicInfo where RefreshDate = '{}'".format(date)
df = dbqu.ExecQuery(query_getcode)

login = uqer.Client(token=Constant.token)

for x in df:
    df_stock = DataAPI.MktEqudGet(ticker=x[0],beginDate='20160101',endDate='20161231')
    df_stock.replace(pd.to_numeric('nan', errors='ingore'), 0, inplace=True)
    # 将强制转化为float64的nan值用0替换，避免在写入数据时出现错误
    print("查询代码为"+str(x[0])+"的数据成功")
    print(datetime.now())
    for i in range(0, df_stock.shape[0]):
        query = "insert into Stock_HistoryData_Daily(SecID,Code,Name,ExchangeCD,TradeDate,PreClosePrice,	ActPreClosePrice,OpenPrice,HighestPrice,LowestPrice,ClosePrice,TurnoverVol,TurnoverValue,DealAmount,TurnoverRate,AccumAdjFactor,NegMarketValue,MarketValue,PriceChangePercent, PE_TTM ,PE_Motive,PB,IsOpen,Vwap) values('{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(df_stock.iloc[i][0],df_stock.iloc[i][1],df_stock.iloc[i][2],df_stock.iloc[i][3],df_stock.iloc[i][4],df_stock.iloc[i][5],df_stock.iloc[i][6],df_stock.iloc[i][7],df_stock.iloc[i][8],df_stock.iloc[i][9],df_stock.iloc[i][10],df_stock.iloc[i][11],df_stock.iloc[i][12],df_stock.iloc[i][13],df_stock.iloc[i][14],df_stock.iloc[i][15],df_stock.iloc[i][16],df_stock.iloc[i][17],df_stock.iloc[i][18],df_stock.iloc[i][19],df_stock.iloc[i][20],df_stock.iloc[i][21],df_stock.iloc[i][22],df_stock.iloc[i][23])
        dbqu.ExecNonQuery(query)

    print(datetime.now())
    print("写入代码为" + str(x[0]) + "的数据成功")
    gc.collect()
