#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
证券成分板块
"""
from uqer import DataAPI,Client
import sys
sys.path.append(r'D:\CXM\Project_New\DataCenter_Uqer')
import Constant
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
# import MSSQL
import SASQL

date = '20180808'#Constant.today
dbqu = SASQL.DB_DataCenter_Uqer()

login = Client(token=Constant.token)

col_query = "select name from syscolumns where id = object_id('{}')".format('Stock_SectorInfo')
cols = dbqu.ExecQuery(col_query)


df = DataAPI.SecTypeRelGet()
df.insert(0,'date',[date for x in range(0,df.shape[0])])
df.columns = [x[0] for x in cols]

df.to_sql('Stock_SectorInfo',dbqu.conn,if_exists='append',index=False,chunksize=1000)