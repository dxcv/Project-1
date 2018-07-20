# -*- coding: utf-8 -*-
"""
@author: 陈祥明
从Nerux导入MarketEod
"""
from SQLLINK import MSSQL

dbnr = MSSQL.DB_Nurex()
dbsa = MSSQL.DB_ScenarioAnalysis()

query0 = "delete from MarketEod"
dbsa.ExecNonQuery(query0)

query1 = "select [Date],[InstrumentID],[PrevClosePrice],[PrevSettlementPrice],[ClosePrice],[SettlementPrice] from MarketEod"
hist = dbnr.ExecQuery(query1)
print("共计"+str(len(hist))+"条记录")
for i in hist:
    query = "insert into [MarketEod]([Date],[InstrumentID],[PrevClosePrice],[PrevSettlementPrice],[ClosePrice],[SettlementPrice]) values(\'{0}\',\'{1}\',{2},{3},{4},{5})".format(i[0], i[1], i[2], i[3], i[4], i[5])
    dbsa.ExecNonQuery(query)

