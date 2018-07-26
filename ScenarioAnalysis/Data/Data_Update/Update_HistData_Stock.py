# -*- coding: utf-8 -*-
"""
@author: 陈祥明
从uqer导入全部历史数据
"""
import uqer
import sys
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
sys.path.append(r'D:\CXM\Project_New\ScenarioAnalysis')
import MSSQL
import Constant

# 连接uqer
uqer.Client(token='f1b9bea1d0b4e489c5ab9b69c3e2326a1bee6057af858067dbd1546453f428b2')

#
dbsa = MSSQL.DB_ScenarioAnalysis()
date = Constant.date

# 清空原有表内数据
query = "delete from HistData_Stock where Date=\'{}\'".format(date)
dbsa.ExecNonQuery(query)

# 获取股票代码
query0 = "select InstrumentID from InstrumentInfo_Stock"
Stock_Info = dbsa.ExecQuery(query0)



# 获取A股当日数据并写入数据库
for i in Stock_Info:
    a = uqer.DataAPI.MktEqudGet(ticker=i[0], tradeDate=date, field="tradeDate,ticker,openPrice,highestPrice,lowestPrice,closePrice,chgPct", pandas="1")
    print("查询代码为" + i[0] + "股票数据成功")
    for j in range(0, a.shape[0]):
        query1 = "insert into HistData_Stock(Date,InstrumentID,openprice,highestprice,lowestprice,closeprice,PriceChangePercent) values(\'{0}\',\'{1}\',{2},{3},{4},{5},{6})".format(a.iloc[j]['tradeDate'], a.iloc[j]['ticker'], a.iloc[j]['openPrice'], a.iloc[j]['highestPrice'], a.iloc[j]['lowestPrice'], a.iloc[j]['closePrice'], a.iloc[j]['chgPct'])
        dbsa.ExecNonQuery(query1)
    print("写入代码为"+i[0]+"股票数据成功")

# 测试用
# a = uqer.DataAPI.MktEqudGet(ticker=Stock_Info[0][0], beginDate=u"20150101", endDate=today, field="tradeDate,ticker,secShortName,openPrice,highestPrice,lowestPrice,closePrice,chgPct", pandas="1")
#
# print(a)