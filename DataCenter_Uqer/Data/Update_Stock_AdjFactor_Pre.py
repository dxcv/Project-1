#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新前复权因子
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

df = DataAPI.MktAdjfGet(ticker="000001")
df.columns = ['SecID','Code','ExchangeCD','SecShortName','SecShortNameEn','ExDivDate','PerCashDiv','PerShareDivRatio','PerShareTransRatio','AllotmentRatio','AllotmentPrice','AdjFactor','AccumAdjFactor','EndDate']


df.to_sql('Stock_AdjFactor_Pre',dbqu.conn,if_exists='append',index=False,chunksize=1000)