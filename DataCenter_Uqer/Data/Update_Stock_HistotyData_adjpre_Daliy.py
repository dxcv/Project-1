#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新前复权行情
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

df = DataAPI.MktEqudAdjGet(tradeDate=date)
df.columns = ['SecID','Code','Name','ExchangeCD','TradeDate','PreClosePrice','ActPreClosePrice','OpenPrice','HighestPrice','LowestPrice','ClosePrice','TurnoverVol','NegMarketValue','DealAmount','TurnoverRate','AccumAdjFactor','TurnoverValue','MarketValue','IsOpen']

df.to_sql('Stock_HistoryData_AdjPre_Daily',dbqu.conn,if_exists='append',index=False,chunksize=1000)