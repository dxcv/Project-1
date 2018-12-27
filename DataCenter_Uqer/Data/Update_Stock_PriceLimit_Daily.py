#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
涨跌停版幅度变动
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
df = DataAPI.MktLimitGet(tradeDate='20180808')
df.columns = ['SecID','Code','SecShortName','SecShortNameEn','ExchangeCD','TradeDate','LimitUpPrice','LimitDownPrice','UpLimitReachedTimes','DownLimitReachedTimes']

df.to_sql('Stock_PriceLimit_Daliy',dbqu.conn,if_exists='append',index=False,chunksize=1000)
