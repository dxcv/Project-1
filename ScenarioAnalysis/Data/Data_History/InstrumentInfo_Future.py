# -*- coding: utf-8 -*-
"""
@author: 陈祥明
从Excel导入期货全部品种
"""

import pandas as pd
from SQLLINK import MSSQL
dbsa = MSSQL.DB_ScenarioAnalysis()

query0 = "delete from InstrumentInfo_Future"
dbsa.ExecNonQuery(query0)

Future_Info = pd.read_excel(r"D:\CXM\Project_New\ScenarioAnalysis\HistoryData\InstrumentInfo_future.xlsx")

for i in range(0, Future_Info.shape[0]):
    query = "insert into InstrumentInfo_Future(ProductID,ProductName) values(\'{0}\',\'{1}\')".format(Future_Info.iloc[i]['InstrumentID'], Future_Info.iloc[i]['InstrumentName'])
    dbsa.ExecNonQuery(query)


# print(type(Future_Info))
# print(Future_Info)

