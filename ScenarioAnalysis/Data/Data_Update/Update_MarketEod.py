# -*- coding: utf-8 -*-
"""
@author: 陈祥明
从Nerux导入MarketEod
"""
import sys
import sys
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
sys.path.append(r'D:\CXM\Project_New\ScenarioAnalysis')
import MSSQL
import Constant

date = Constant.date
dbnr = MSSQL.DB_Nurex()
dbsa = MSSQL.DB_ScenarioAnalysis()

query0 = "delete from MarketEod where Date=\'{}\'".format(date)
dbsa.ExecNonQuery(query0)

query1 = "select [Date],[InstrumentID],[PrevClosePrice],[PrevSettlementPrice],[ClosePrice],[SettlementPrice] from MarketEod where Date=\'{}\'".format(date)
record = dbnr.ExecQuery(query1)

print("共计"+str(len(record))+"条记录")
for i in record:
    query = "insert into [MarketEod]([Date],[InstrumentID],[PrevClosePrice],[PrevSettlementPrice],[ClosePrice],[SettlementPrice]) values(\'{0}\',\'{1}\',{2},{3},{4},{5})".format(i[0], i[1], i[2], i[3], i[4], i[5])
    dbsa.ExecNonQuery(query)

