#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新每日期货行情数据
"""

from uqer import DataAPI,Client
import pandas as pd
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
import SASQL
sys.path.append(r'D:\CXM\Project\ScenarioAnalysis')
import Constant

date = '20180828'#Constant.date

login = Client(token=Constant.token)

dbsa = SASQL.ScenarioAnalysis()

del_query = "delete from HistData_Future_Daily where TradeDate='{}'".format(date)
dbsa.ExecNonQuery(del_query)

col_query = "select name from syscolumns where id = object_id('{}')".format('HistData_Future_Daily')
cols = dbsa.ExecQuery(col_query)


df = DataAPI.MktFutdGet(tradeDate=date)
df.set_index('ticker', inplace=True)


df0 = DataAPI.FutuGet(contractStatus="L",field=['ticker','contMultNum'],pandas="1")
df0.set_index('ticker', inplace=True)

result = pd.merge(df,df0,how='inner',left_on='ticker',right_index=True)
result.insert(1,'code',result.index)
result.columns = [x[0] for x in cols]
result.to_sql('HistData_Future_Daily',dbsa.conn,if_exists='append',index=False,chunksize=1000)