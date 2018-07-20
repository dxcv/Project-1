"""
从数据库获取数据为dataframe
"""
import pandas as pd
import sys
from datetime import date
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import MSSQL
import SASQL

# dbda = SASQL.DataCenter_Analysis()
# histdata_stock = SASQL.HistData_Stock
#
# a = dbda.session.query(histdata_stock).filter(histdata_stock.InstrumentID=='000001').all()
#
# # print(a[0])
# # print(dir(a[0]))
# # print(a[0].__getattribute__)
# df = pd.DataFrame(columns=['InstrumentID','openprice','highestprice','closeprice','lowestprice','PriceChangePercent'])
# for i in range(0, len(a)):
#     # df.iloc[0].index = date(a[i].Date)
#     df.iloc[0]['openprice'] = a[i].openprice
#     df.iloc[0]['highestprice'] = a[i].highestprice
#     df.iloc[0]['closeprice'] = a[i].closeprice
#     df.iloc[0]['lowestprice'] = a[i].lowestprice
#     df.iloc[0]['PriceChangePercent'] = a[i].PriceChangePercent

dbda = MSSQL.DB_DataCenter_Analysis()
query0 = "select * from HistData_Stock where InstrumentID='{}'".format('000001')
que
a = dbda.ExecQuery(query)

df = pd.DataFrame(columns=['date', 'InstrumentID','openprice','highestprice','closeprice','lowestprice','PriceChangePercent'],data=a)

