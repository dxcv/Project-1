#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ETF历史数据
"""

import numpy as np
from uqer import Client,DataAPI
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
sys.path.append(r'D:\CXM\Project\ScenarioAnalysis')
import SASQL
import Constant

login = Client(token=Constant.token)
df_all = DataAPI.FundGet(etfLof="ETF",listStatusCd="L",field="",pandas="1")
df = df_all[(df_all.tradeAbbrName.str.contains('上证50ETF')==True) | (df_all.tradeAbbrName.str.contains('中证500ETF')==True) | (df_all.tradeAbbrName.str.contains('沪深300ETF')==True)][['secID','tradeAbbrName']]
#
dbsa = SASQL.ScenarioAnalysis()
#
#
col_query = "select name from syscolumns where id = object_id('{}')".format('HistData_Stock')
cols = dbsa.ExecQuery(col_query)

for i in range(0,df.shape[0]):
    # query = "delete from HistData_Stock where InstrumentID=''".format(df.iat[i,0])
    data = DataAPI.MktFunddGet(secID=df.iat[i,0],beginDate="20150101",endDate="20181109",field="tradeDate,ticker,preClosePrice,openPrice,highestPrice,lowestPrice,closePrice,CHGPct",pandas="1")

    # data['navChgPct'] = [x[0] for x in np.array(data[['navChgPct']]/100).tolist()]
    data.columns = [x[0] for x in cols]
    data.to_sql('HistData_Stock', dbsa.conn, if_exists='append', index=False, chunksize=1000)
    # print(data.head(5))
    print(df.iat[i,0])