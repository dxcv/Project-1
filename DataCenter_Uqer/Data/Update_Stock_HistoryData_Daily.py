#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新优矿股票数据
"""
import uqer
from uqer import DataAPI
import numpy as np
import pandas as pd
import sys
sys.path.append(r'D:\CXM\Project_New\DataCenter_Uqer')
import Constant
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import MSSQL

date = '20180806'#Constant.today

dbqu = MSSQL.DB_DataCenter_Uqer()

query_del = "delete from Stock_HistoryData_Daily where TradeDate = '{}'".format(date)
dbqu.ExecNonQuery(query_del)

query_getcode = "select Code from Stock_BasicInfo where RefreshDate = '{}'".format(date)
df = dbqu.ExecQuery(query_getcode)

uqer.Client(token=Constant.token)

df_stock = DataAPI.MktEqudGet(tradeDate=date, ticker=[x[0] for x in df])
df_stock.fillna(0)
for i in range(0, df_stock.shape[0]):
    query = "insert into Stock_HistoryData_Daily(SecID,Code,Name,ExchangeCD,TradeDate,PreClosePrice,	ActPreClosePrice,OpenPrice,HighestPrice,LowestPrice,ClosePrice,TurnoverVol,TurnoverValue,DealAmount,TurnoverRate,AccumAdjFactor,NegMarketValue,MarketValue,PriceChangePercent, PE_TTM ,PE_Motive,PB,IsOpen,Vwap) values('{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(df_stock.iloc[i][0],df_stock.iloc[i][1],df_stock.iloc[i][2],df_stock.iloc[i][3],df_stock.iloc[i][4],df_stock.iloc[i][5],df_stock.iloc[i][6],df_stock.iloc[i][7],df_stock.iloc[i][8],df_stock.iloc[i][9],df_stock.iloc[i][10],df_stock.iloc[i][11],df_stock.iloc[i][12],df_stock.iloc[i][13],df_stock.iloc[i][14],df_stock.iloc[i][15],df_stock.iloc[i][16],df_stock.iloc[i][17],df_stock.iloc[i][18],df_stock.iloc[i][19],df_stock.iloc[i][20],df_stock.iloc[i][21],df_stock.iloc[i][22],df_stock.iloc[i][23])
    dbqu.ExecNonQuery(query)