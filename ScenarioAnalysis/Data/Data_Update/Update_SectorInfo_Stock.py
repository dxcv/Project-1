# -*- coding: utf-8 -*-
"""
@author: 陈祥明
从tushare导入板块信息
"""
from uqer import Client,DataAPI
import tushare as ts
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
import SASQL
sys.path.append(r'D:\CXM\Project\ScenarioAnalysis')
import DataClean
import Constant

Date = Constant.date
dbsa = SASQL.ScenarioAnalysis()
query = "delete from SectorInfo_Stock"
dbsa.ExecNonQuery(query)

login = Client(token=Constant.token)
df = DataAPI.FundGet(etfLof="ETF",listStatusCd="L",field="",pandas="1")

# df_ =df[(df.tradeAbbrName.str.contains('沪深300ETF')==True) | (df.tradeAbbrName.str.contains('中证500ETF')==True) | (df.tradeAbbrName.str.contains('上证50ETF')==True)]

# 沪深300
df_HS300 = df[(df.tradeAbbrName.str.contains('沪深300ETF')==True)][['ticker','tradeAbbrName']]
df_HS300.columns = ['InstrumentID','InstrumentName']
df_HS300.insert(0,'SectorName','沪深300')
df_HS300.insert(0,'SectorID','hs300')
df_HS300.to_sql('SectorInfo_Stock', dbsa.conn, if_exists='append', index=False, chunksize=1000)

#中证500
df_ZZ300 = df[(df.tradeAbbrName.str.contains('中证500ETF')==True)][['ticker','tradeAbbrName']]
df_ZZ300.columns = ['InstrumentID','InstrumentName']
df_ZZ300.insert(0,'SectorName','中证500ETF')
df_ZZ300.insert(0,'SectorID','zz500')
df_ZZ300.to_sql('SectorInfo_Stock', dbsa.conn, if_exists='append', index=False, chunksize=1000)

# 上证50
df_HZ50 = df[(df.tradeAbbrName.str.contains('上证50ETF')==True)][['ticker','tradeAbbrName']]
df_HZ50.columns = ['InstrumentID','InstrumentName']
df_HZ50.insert(0,'SectorName','上证50ETF')
df_HZ50.insert(0,'SectorID','sz50')
df_HZ50.to_sql('SectorInfo_Stock', dbsa.conn, if_exists='append', index=False, chunksize=1000)





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
# print(hs300)
# print(zz500)
# print(sz50)