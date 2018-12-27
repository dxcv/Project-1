#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
股票交易公开信息_股票(龙虎榜_股票)
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

col_query = "select name from syscolumns where id = object_id('{}')".format('Stock_Abnormal_Single_Daily')
cols = dbqu.ExecQuery(col_query)


df = DataAPI.MktRankListSalesGet(tradeDate='20180809')
df.columns = [x[0] for x in cols]

df.to_sql('Stock_Abnormal_Single_Daily',dbqu.conn,if_exists='append',index=False,chunksize=1000)