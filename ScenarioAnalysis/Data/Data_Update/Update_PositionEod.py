# -*- coding: utf-8 -*-
"""
@author: 陈祥明
从Nerux导入PositionEod当日记录
"""
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
sys.path.append(r'D:\CXM\Project\ScenarioAnalysis')
import MSSQL
import Constant

date = Constant.date
dbsa = MSSQL.DB_ScenarioAnalysis()
dbnr = MSSQL.DB_Nurex()

query0 = "delete from PositionEod where Date='{}'".format(date)
dbsa.ExecNonQuery(query0)

query1 = "select [PositionEod].[Date],[PositionEod].AccountID,[PositionEod].[InstrumentID],[PositionEod].TotalPosition,[PositionEod].Portfolio,[PositionEod].[Direction],[Portfolio].[PortfolioID],Portfolio.ParentID,[Portfolio].[Product] from  [PositionEod],[Portfolio] where [PositionEod].Portfolio=[Portfolio].[PortfolioID] and [Portfolio].[Product]='prop' and [PositionEod].[Date]='{0}'".format(date)
record = dbnr.ExecQuery(query1)

for i in record:
    query = "insert into PositionEod(Date,AccountID,InstrumentID,TotalPosition,portfolio,direction,portfolioID,parentID,product) values('{0}','{1}','{2}',{3},'{4}','{5}','{6}','{7}','{8}')".format(i[0], i[1], i[2], i[3], i[4], i[5].encode('latin1').decode('gbk'), i[6], i[7], i[8])
    dbsa.ExecNonQuery(query)