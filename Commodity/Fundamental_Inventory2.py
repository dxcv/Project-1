#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
基本面因子构成表-库存2
"""
import pandas as pd
import os
import numpy as np
import sys
from datetime import datetime
sys.path.append(r'D:\CXM\Project\SQLLINK')
from SQLLINK import SASQL



def getIndexName(df=None):
    a = []
    for col in df.columns:
        if col[0:-2] in a:
            pass
        else:
            a.append(col)
    return a

def getIndexNameList(index_name, df=None):
    a = []
    for col in df.columns:
        if col[0:len(index_name)] == index_name:
            a.append(col)
        else:
            pass
    return a


def getData(df,li): #列名相同，且同为日期的列pass
    for x in range(1,len(li)):
        source = df[[list[0], list[x]]]
        source = source.dropna(how='all')



filepath = 'Z:\personal\hebian\基本面数据\基本面因子组成结构表.xlsx'
df = pd.read_excel(io=filepath,sheet_name='库存2')

dbco = SASQL.DataCenter_Commodity()
list = getIndexName(df)
for x in list:
    m = x
    namelist = getIndexNameList(x,df)
    Datasource = df[[x]].iat[1,0]
    for y in range(1,len(namelist)):
        source = df[[m,namelist[y]]]
        source = source.dropna(how='all')
        if source.empty == False:
            if type(source.iat[10, 1]) == pd._libs.tslibs.timestamps.Timestamp:
                m = namelist[y]
            else:

                data = pd.DataFrame()
                data['TradingDate'] = source[m].iloc[4:]
                data.dropna(inplace=True)
                data['ProductID'] = x
                data['ProductName'] = source.iat[0, 0]
                data['IndexName'] = np.nan
                data['Secu_Arrb'] = source.iat[0, 1]
                data['Data'] = source[namelist[y]].iloc[4:]
                data['Frequency'] = source.iat[2,1]
                data['Unit'] = source.iat[1,1]
                data['DataSource'] = source.iat[3,1]
                # data.dropna(inplace=True)
                # data.dropna(how='all', inplace=True)

                print(x)
                data.drop_duplicates('TradingDate',inplace=True)
                data.to_sql('Commodity_Inventory', dbco.conn, if_exists='append', index=False, chunksize=1000)


