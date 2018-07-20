"""
dataframe获取数据并进行处理
"""
import pandas as pd
import pymssql
from datetime import datetime
import sys
sys.path.append(r'D:\CXM\Project_New\DataAnalysis')
import constant
import time

conn = constant.conn

query = "select * from HistData_Stock where InstrumentID='{}'".format('000001')

data = pd.read_sql(sql=query, con=conn, index_col='Date')

# pandas读取数据库将会将Date格式转化为str，将index中的str转化为date
data.index = [datetime.strptime(x, '%Y-%m-%d') for x in data.index]

#