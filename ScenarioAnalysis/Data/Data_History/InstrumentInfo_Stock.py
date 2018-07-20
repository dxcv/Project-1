# -*- coding: utf-8 -*-
"""
@author: 陈祥明
从tushare导入股票信息
"""
import tushare as ts
from SQLLINK import MSSQL

dbsa = MSSQL.DB_ScenarioAnalysis()

stock_info = ts.get_stock_basics()
stock_info.insert(0, 'code', stock_info.index)

query0 = "delete from InstrumentInfo_Stock"
dbsa.ExecNonQuery(query0)

for i in range(0, stock_info.shape[0]):
    query = "insert into InstrumentInfo_Stock(InstrumentID,InstrumentName) values(\'{0}\',\'{1}\')".format(stock_info.iloc[i]['code'], stock_info.iloc[i]['name'])
    dbsa.ExecNonQuery(query)

# print(stock_info)