# -*- coding: utf-8 -*-
"""
@author: 陈祥明
导入期货连续全部历史数据
"""
import sys
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
sys.path.append(r'D:\CXM\Project_New\ScenarioAnalysis')
import MSSQL
import Constant

date = Constant.date
dbsa = MSSQL.DB_ScenarioAnalysis()
dbfmc = MSSQL.DB_datacenterfuturesnew()

# 清楚当日已有数据
query0 = "delete from [HistData_Future] where tradingDate=\'{}\'".format(date)
dbsa.ExecNonQuery(query0)

# 获取全部品种
query1 = "select distinct productID from FUT_EOD_CONTINUING where tradingDate=\'{}\'".format(date)
productID = dbfmc.ExecQuery(query1)

for m in range(0, len(productID)):
    query2 = "select top 2 * from FUT_EOD_CONTINUING where productID='{0}' order by tradingDate desc".format(productID[m][0])
    record = dbfmc.ExecQuery(query2)
    pcp = (record[0][7]*record[0][11]/record[1][7]/record[1][11])-1
    query = "insert into HistData_Future([algoID],[productID],[instrumentID],[tradingDate],[openPrice],[highPrice],[lowPrice],[closePrice],[volume],[turnover],[openInterestAccumulate],[multiplier],[updateTime],[pricechangepercent]) values({0},'{1}','{2}','{3}',{4},{5},{6},{7},{8},{9},{10},{11},'{12}',{13})".format(record[0][0], record[0][1], record[0][2], record[0][3], record[0][4], record[0][5], record[0][6], record[0][7], record[0][8], record[0][9], record[0][10], record[0][11], record[0][12], pcp)
    dbsa.ExecNonQuery(query)