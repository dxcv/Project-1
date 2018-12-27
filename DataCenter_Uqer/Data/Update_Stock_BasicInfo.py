#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新优矿股票数据
"""
import uqer
from uqer import DataAPI
import pandas as pd
import sys
sys.path.append(r'D:\CXM\Project_New\DataCenter_Uqer')
import Constant
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
# import MSSQL
import SASQL

date = Constant.today

query_del = "delete from Stock_BasicInfo where RefreshDate = '{}'".format(date)
dbqu = SASQL.DB_DataCenter_Uqer()
dbqu.ExecNonQuery(query_del)


uqer.Client(token=Constant.token)

df_StockInfo = DataAPI.EquGet(equTypeCD=['A','B'], listStatusCD=['L', 'S'])

# 添加更新日期列
df_StockInfo.insert(0, 'RefreshDate', [date for x in range(0, df_StockInfo.shape[0])])
#匹配数据库列名
df_StockInfo.columns = ['RefreshDate','SecID','Code','ExchangeCD','ListSectorCD','ListSector','TransCurrCD','Name','FullName','ListStatusCD','ListDate','DelistDate','EquTypeCD','ExCountryCD','EquType','PartyID','TotalShares','NonrestFloatShares','NonrestFloatA','OfficeAddress','PrimeOperating','EndDate','TShEquity']

df_StockInfo.to_sql('Stock_BasicInfo',dbqu.conn,if_exists='append',index=False,chunksize=1000)




# df_STOCKINFO = a.where(a.notnull(),None)
# df_STOCKINFO.replace(pd.to_numeric('nan', errors='ingore'), None, inplace=True)
#
# for i in range(0, df_STOCKINFO.shape[0]):
#     query = "insert into Stock_BasicInfo(RefreshDate,SecID,Code,ExchangeCD,ListSectorCD,ListSector,TransCurrCD,Name,FullName,ListStatusCD,ListDate,DelistDate,EquTypeCD,ExCountryCD,EquType,PartyID,TotalShares,NonrestFloatShares,NonrestFloatA,OfficeAddress,PrimeOperating,EndDate,TShEquity) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}',{},{},{},'{}','{}','{}',{})".format(date,df_STOCKINFO.iloc[i][0],df_STOCKINFO.iloc[i][1],df_STOCKINFO.iloc[i][2],df_STOCKINFO.iloc[i][3],df_STOCKINFO.iloc[i][4],df_STOCKINFO.iloc[i][5],df_STOCKINFO.iloc[i][6],df_STOCKINFO.iloc[i][7],df_STOCKINFO.iloc[i][8],df_STOCKINFO.iloc[i][9],df_STOCKINFO.iloc[i][10],df_STOCKINFO.iloc[i][11],df_STOCKINFO.iloc[i][12],df_STOCKINFO.iloc[i][13],df_STOCKINFO.iloc[i][14],df_STOCKINFO.iloc[i][15],df_STOCKINFO.iloc[i][16],df_STOCKINFO.iloc[i][17],df_STOCKINFO.iloc[i][18],df_STOCKINFO.iloc[i][19],df_STOCKINFO.iloc[i][20],df_STOCKINFO.iloc[i][21])
#     dbqu.ExecNonQuery(query)


