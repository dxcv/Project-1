#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
导入数据
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
        if str(col).find('.') == True:
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




dbco = SASQL.DataCenter_Commodity()
path = r'D:\CXM\Project\Commodity\基本面数据'
files = os.listdir(path)
for file in files:
    filepath = path+'\\'+file
    excel = pd.read_excel(io=filepath,sheet_name=None)
    for sheet in excel.keys():
        if sheet == '目录':
            pass
        else:
            df = excel[sheet]
            list = getIndexName(df)
            for x in list:
                m = x
                namelist = getIndexNameList(x,df)
                Datasource = df[[x]].iat[0,0]
                for y in range(1,len(namelist)):
                    source = df[[m,namelist[y]]]
                    # source = source.dropna(how='all')
                    if source.empty == False:
                        if type(source.iat[10, 1]) == pd._libs.tslibs.timestamps.Timestamp:
                            m = namelist[y]
                        else:
                            # source = source.dropna(how='all')
                            if str(source.iat[3, 0]) == '1':
                                data = pd.DataFrame()
                                data['Date'] = np.nan
                                data['WeekFlag'] = source[m].iloc[3:]
                                data.dropna(how='all',inplace=True)
                                data['ProductID'] = sheet
                                data['IndexName'] = x
                                data['DataName'] = source.iat[1,1]
                                data['Data'] = source[namelist[y]].iloc[3:]
                                data['Unit'] = source.iat[2, 1]
                                data['DataSource'] = Datasource
                                data['Date'] = datetime(1900, 1, 1, 0, 0)
                                data.dropna(how='all',inplace=True)
                                data[['Data']] = data[['Data']].apply(pd.to_numeric)
                                data.to_sql('test', dbco.conn, if_exists='append', index=False, chunksize=1000)
                                # try:
                                #     data.to_sql('test',dbco.conn,if_exists='append',index=False, chunksize=1000)
                                # except SASQL.exc.OperationalError as e:
                                #     print('----------OperationalError----------')
                                #     print(filepath)
                                #     print(sheet)
                                #     print(x)
                                #     print(source.iat[1,1])
                                # except ValueError as e:
                                #     print('----------ValueError----------')
                                #     print(filepath)
                                #     print(sheet)
                                #     print(x)
                                #     print(source.iat[1, 1])
                                # else:
                                #     pass
                            else:
                                data = pd.DataFrame()
                                data['Date'] = source[m].iloc[3:]
                                data.dropna(inplace=True)
                                data['WeekFlag'] = 0
                                data['ProductID'] = sheet
                                data['IndexName'] = x
                                data['DataName'] = source.iat[1,1]
                                data['Data'] = source[namelist[y]].iloc[3:]
                                data['Unit'] = source.iat[2,1]
                                data['DataSource'] = Datasource
                                data.dropna(inplace=True)
                                data.dropna(how='all', inplace=True)
                                # data[['Data']] = data[['Data']].apply(pd.to_numeric)

                                data.to_sql('test', dbco.conn, if_exists='append', index=False, chunksize=1000)
                                # try:
                                #     data.to_sql('test',dbco.conn,if_exists='append',index=False, chunksize=1000)
                                # except SASQL.exc.OperationalError as e:
                                #     print('----------OperationalError----------')
                                #     print(filepath)
                                #     print(sheet)
                                #     print(x)
                                #     print(source.iat[1, 1])
                                # except ValueError as e:
                                #     print('----------ValueError----------')
                                #     print(filepath)
                                #     print(sheet)
                                #     print(x)
                                #     print(source.iat[1, 1])
                                # else:
                                #     pass


