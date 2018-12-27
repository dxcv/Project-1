#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新指数日行情
"""

from uqer import DataAPI,Client
import sys
sys.path.append(r'D:\CXM\Project_New\DataCenter_Uqer')
import Constant
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
# import MSSQL
import SASQL

date = '20180808'#Constant.today

dbqu = SASQL.DB_DataCenter_Uqer()

query_del = "delete from Index_HistoryData_Daily where TradeDate = '{}'".format(date)
dbqu.ExecNonQuery(query_del)

# query_getcode = "select Code from Stock_BasicInfo where RefreshDate = '{}'".format(date)
# df = dbqu.ExecQuery(query_getcode)

login = Client(token=Constant.token)

df_index = DataAPI.MktIdxdGet(tradeDate=date)

df_index.columns = ['IndexID','IndexCode','PorgFullName','SecName','ExchangeCD','TradeDate','PreCloseIndex','OpenIndex','LowestIndex','HighestIndex','CloseIndex','TurnoverVol','TurnoverValue','PriceChange','PriceChangePercent']

df_index.to_sql('Index_HistoryData_Daily',dbqu.conn,if_exists='append',index=False,chunksize=1000)



# df_index.replace(pd.to_numeric('nan', errors='ingore'), 0, inplace=True)
#     # 将强制转化为float64的nan值用0替换，避免在写入数据时出现错误
# for i in range(0, df_index.shape[0]):
#     query = "insert into Index_HistoryData_Daily(IndexID,IndexCode,	PorgFullName,SecName,ExchangeCD,TradeDate,PreCloseIndex,OpenIndex,LowestIndex,HighestIndex,CloseIndex,TurnoverVol,TurnoverValue,	PriceChange,PriceChangePercent) values('{}','{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},{})".format(df_index.iloc[i][0],df_index.iloc[i][1],df_index.iloc[i][2],df_index.iloc[i][3],df_index.iloc[i][4],df_index.iloc[i][5],df_index.iloc[i][6],df_index.iloc[i][7],df_index.iloc[i][8],df_index.iloc[i][9],df_index.iloc[i][10],df_index.iloc[i][11],df_index.iloc[i][12],df_index.iloc[i][13],df_index.iloc[i][14])
#     dbqu.ExecNonQuery(query)