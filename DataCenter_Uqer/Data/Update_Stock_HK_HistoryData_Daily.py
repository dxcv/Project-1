#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新港股日行情
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
df = DataAPI.MktHKEqudGet(tradeDate=date)

df.columns = ['SecID','Code','ExchangeCD','SecShortName','TradeDate','PreClosePrice','ActPreClosePrice','OpenPrice','HighestPrice','LowestPrice','ClosePrice','TurnoverVol','TurnovarValue','SMA_10','SMA_20','SMA_50','SMA_250']

df.to_sql('Stock_HK_HistoryData_Daily',dbqu.conn,if_exists='append',index=False,chunksize=1000)
