# -*- coding: utf-8 -*-
"""
@author: 陈祥明
导入期货连续全部历史数据
"""

import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
sys.path.append(r'D:\CXM\Project\ScenarioAnalysis')
import MSSQL

dbsa = MSSQL.DB_ScenarioAnalysis()
dbfmc = MSSQL.DB_datacenterfuturesnew()

query0 = "delete from [HistData_Future_Continuing]"
dbsa.ExecNonQuery(query0)

query1 = "select distinct productID from FUT_EOD_CONTINUING"
productID = dbfmc.ExecQuery(query1)



for m in range(0, len(productID)):
    query2 = "select * from FUT_EOD_CONTINUING where productID='{0}' order by tradingDate".format(productID[m][0])
    hist = dbfmc.ExecQuery(query2)
    for n in range(1, len(hist)):
        pcp = (hist[n][7]*hist[n][11]/hist[n-1][7]/hist[n-1][11])-1
        query = "insert into HistData_Future_Continuing([algoID],[productID],[instrumentID],[tradingDate],[openPrice],[highPrice],[lowPrice],[closePrice],[volume],[turnover],[openInterestAccumulate],[multiplier],[updateTime],[pricechangepercent]) values({0},'{1}','{2}','{3}',{4},{5},{6},{7},{8},{9},{10},{11},'{12}',{13})".format(hist[n][0], hist[n][1], hist[n][2], hist[n][3], hist[n][4], hist[n][5], hist[n][6], hist[n][7], hist[n][8], hist[n][9], hist[n][10], hist[n][11], hist[n][12], pcp)
        dbsa.ExecNonQuery(query)
    print('写入期货种类为'+productID[m][0]+'的数据成功')