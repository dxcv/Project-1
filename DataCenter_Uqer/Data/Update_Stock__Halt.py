#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新股票停牌信息
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

login = Client(token=Constant.token)

df_Stock_Halt = DataAPI.SecHaltGet(ticker='000001',beginDate='20100101',endDate='20180809')
df_Stock_Halt.insert(0, 'RefreshDate', [date for x in range(0, df_Stock_Halt.shape[0])])
df_Stock_Halt.columns = ['RefreshDate','SecID','HaltBeginTime','HaltEndTime','Code','Name','ExchangeCD','StatusCD','DelistDate','AssetClass']

df_Stock_Halt.to_sql('Stock_Halt',dbqu.conn,if_exists='append',index=False,chunksize=1000)