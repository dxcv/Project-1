# -*- coding: utf-8 -*-
"""
@author: 陈祥明
从uqer导入全部股票历史数据
"""
import uqer
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
sys.path.append(r'D:\CXM\Project\ScenarioAnalysis')
import SASQL
import Constant

# 连接uqer
uqer.Client(token=Constant.token)

#
dbsa = SASQL.ScenarioAnalysis()

date = Constant.date

# 清空原有表内数据
query = "delete from HistData_Stock where Date='{}'".format(date)
dbsa.ExecNonQuery(query)

col_query = "select name from syscolumns where id = object_id('{}')".format('HistData_Stock')
cols = dbsa.ExecQuery(col_query)

df = uqer.DataAPI.MktEqudGet(tradeDate=date, field="tradeDate,ticker,preClosePrice,openPrice,highestPrice,lowestPrice,closePrice,chgPct", pandas="1")
df.columns = [x[0] for x in cols]

df.to_sql('HistData_Stock',dbsa.conn,if_exists='append',index=False,chunksize=1000)




# # 获取全部A股股票代码
# query0 = "select InstrumentID from InstrumentInfo_Stock"
# Stock_Info = dbsa.ExecQuery(query0)


# 获取A股当日数据并写入数据库
# for i in Stock_Info:
#     a = uqer.DataAPI.MktEqudGet(ticker=i[0], tradeDate=date, field="tradeDate,ticker,openPrice,highestPrice,lowestPrice,closePrice,chgPct", pandas="1")
#     # print(a)
#     # print("查询代码为" + i[0] + "股票数据成功")
#     try:
#         query1 = "insert into HistData_Stock(Date,InstrumentID,openprice,highestprice,lowestprice,closeprice,PriceChangePercent) values(\'{0}\',\'{1}\',{2},{3},{4},{5},{6})".format(a.iloc[0]['tradeDate'], a.iloc[0]['ticker'], a.iloc[0]['openPrice'], a.iloc[0]['highestPrice'], a.iloc[0]['lowestPrice'], a.iloc[0]['closePrice'], a.iloc[0]['chgPct'])
#     except IndexError as e:
#         print(e)
#         print("代码为"+i[0]+"的股票为新上市股票，无数据")
#     else:
#         dbsa.ExecNonQuery(query1)
#         print("写入代码为"+i[0]+"股票数据成功")

# 测试用
# a = uqer.DataAPI.MktEqudGet(ticker=Stock_Info[0][0], beginDate=u"20150101", endDate=today, field="tradeDate,ticker,secShortName,openPrice,highestPrice,lowestPrice,closePrice,chgPct", pandas="1")
#
# print(a)



