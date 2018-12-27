#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: 陈祥明
从uqer导入全部股票历史数据
"""
from uqer import Client,DataAPI
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
sys.path.append(r'D:\CXM\Project\ScenarioAnalysis')
import SASQL
import Constant

import numpy as np

# 连接uqer
login = Client(token=Constant.token)

#
dbsa = SASQL.ScenarioAnalysis()

date = Constant.date

# 清空原有表内数据
query = "delete from HistData_Stock  where (InstrumentID like '1%' or InstrumentID like '5%') and Date='{}'".format(date)
dbsa.ExecNonQuery(query)

col_query = "select name from syscolumns where id = object_id('{}')".format('HistData_Stock')
cols = dbsa.ExecQuery(col_query)

df_all = DataAPI.FundGet(etfLof="ETF",listStatusCd="L",field="",pandas="1")
df = df_all[(df_all.tradeAbbrName.str.contains('上证50ETF')==True) | (df_all.tradeAbbrName.str.contains('中证500ETF')==True) | (df_all.tradeAbbrName.str.contains('沪深300ETF')==True)][['secID','tradeAbbrName']]

ETFli = [x[0] for x in np.array(df[['secID']]).tolist()]


data = DataAPI.MktFunddGet(secID=ETFli,tradeDate=date,field="tradeDate,ticker,preClosePrice,openPrice,highestPrice,lowestPrice,closePrice,CHGPct",pandas="1")



data.columns = [x[0] for x in cols]
data.to_sql('HistData_Stock',dbsa.conn,if_exists='append',index=False,chunksize=1000)

