# -*- coding: utf-8 -*-
"""
@author: 陈祥明
导入期货乘数全部历史数据
"""

from SQLLINK import MSSQL

dbsa = MSSQL.DB_ScenarioAnalysis()
dbfmc = MSSQL.DB_datacenterfuturesnew()

query0 = "delete from Future_Multiplier"
dbsa.ExecQuery(query0)

query1 = "select * from FUT_MULTIPLIER"
hist = dbfmc.ExecQuery(query1)

for i in hist:
    query2 = "insert into Future_Multiplier(ProductID,Multiplier,Unit,ReflashDate,RecordDate) values (\'{0}\',{1},\'{2}\',\'{3}\',\'{4}\')".format(i[0], i[1], i[2].encode('latin1').decode('gbk'), i[3], i[4])
    dbsa.ExecNonQuery(query2)

