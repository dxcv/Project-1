# -*- coding: utf-8 -*-
"""
@author: 陈祥明
从tushare导入板块信息
"""
import tushare as ts
import sys
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import MSSQL
sys.path.append(r'D:\CXM\Project_New\ScenarioAnalysis')
import DataClean
import Constant

dbsa = MSSQL.DB_ScenarioAnalysis()
query = "delete from SectorInfo_Stock"
dbsa.ExecNonQuery(query)


hs300 = ts.get_hs300s()
# print(hs300)
a = DataClean.DataframeTolist(hs300)
for i in a:
    query1 = "insert into SectorInfo_Stock(SectorID,SectorName,InstrumentID,InstrumentName)  values('{0}','{1}','{2}','{3}')".format('hs300', '沪深300', i[1], i[2])
    dbsa.ExecNonQuery(query1)

zz500 = ts.get_zz500s()
b = DataClean.DataframeTolist(zz500)
for m in b:
    query2 = "insert into SectorInfo_Stock(SectorID,SectorName,InstrumentID,InstrumentName)  values('{0}','{1}','{2}','{3}')".format('zz500', '中证500', m[1], m[2])
    dbsa.ExecNonQuery(query2)

sz50 = ts.get_sz50s()
c = DataClean.DataframeTolist(sz50)
for n in c:
    query3 = "insert into SectorInfo_Stock(SectorID,SectorName,InstrumentID,InstrumentName)  values('{0}','{1}','{2}','{3}')".format('sz50', '上证50', n[1], n[2])
    dbsa.ExecNonQuery(query3)

# for i in a:
#     print(i)

# zz500 = ts.get_zz500s()
# sz50 = ts.get_sz50s()
#
#
#
# print(hs300)
# print(zz500)
# print(sz50)