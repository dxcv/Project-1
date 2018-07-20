# -*- coding: utf-8 -*-
"""
@author: 陈祥明
导入期货乘数当日数据数据
"""


import sys
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
sys.path.append(r'D:\CXM\Project_New\ScenarioAnalysis')
import MSSQL
import Constant

date = Constant.date
dbfu = MSSQL.DB_datacenterfuturesnew()
dbsa = MSSQL.DB_ScenarioAnalysis()

query0 = "delete from Future_Multiplier where RecordDate=\'{}\'".format(date)
dbsa.ExecNonQuery(query0)

query1 = "select * from FUT_MULTIPLIER where RecordDate=\'{}\'".format(date)
record = dbfu.ExecQuery(query1)

for i in record:
    query = "insert into Future_Multiplier(ProductID,Multiplier,Unit,ReflashDate,RecordDate) values (\'{0}\',{1},\'{2}\',\'{3}\',\'{4}\')".format(i[0], i[1], i[2].encode('latin1').decode('gbk'), i[3], i[4])
    dbsa.ExecNonQuery(query)