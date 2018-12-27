#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
核对恒生数据
"""

import pandas as pd
import os
import numpy as np
import sys
sys.path.append(r'D:\CXM\Project\PNL')
import Constant
sys.path.append(r'D:\CXM\Project\SQLLINK')
import SASQL

date = '20180831'#Constant.today
# Account = ['77771','77772','77773','77774','77775','77776','77777','77778','77779']
# path_HS = r'D:\CXM\Project\PNL\恒生数据\综合信息查询_汇总证券0827.xls'
# df_HS = pd.read_excel(io=path_HS,header=0,converters={'证券代码': str})
# df_HS.set_index('证券名称',inplace=True)
dbnu = SASQL.Nurex()

# 读取今日按账户分类的恒生数据
path = r'D:\CXM\Project\PNL\恒生数据\\'+date  # 查找恒生数据文件夹
files = os.listdir(path)
for file in files:
    filepath = path+'\\'+file
    df_HS = pd.read_excel(io=filepath,header=0,usecols='C:D,O,BN',converters={'证券代码': str})
    df_HS.sort_values(by='证券代码',inplace=True)
    # df_HS.set_index('证券代码', inplace=True)
    AccountID = file.split('-')[0]
    querydate = (file.split('-')[1]).split('.')[0]
    if AccountID=='77774':
        query = "select * from PositionEod where  AccountID in ('77774','7777402') and Date = '{}'".format(querydate)
    else:
        query = "select * from PositionEod where  AccountID = '{}' and Date = '{}'".format(AccountID,querydate)

    df_PE_Original = pd.read_sql(query, dbnu.conn,index_col='InstrumentID')

    # 对两种不同的数据源做处理
    # 恒生
    df_HS['持仓多空标志'] = list(map(lambda x: x[0], df_HS['持仓多空标志']))
    # df_PE['InstrumentName'] = list(map(lambda x:x.encode('latin1').decode('gbk') if x != None else x == np.nan, df_MK['InstrumentName']))

    # Nurex
    df_PE_Original['Direction'] = list(map(lambda x: x.encode('latin1').decode('gbk') if x != None else x == np.nan, df_PE_Original['Direction']))

    # df_PE = df_PE_Original.groupby(['InstrumentID', 'Direction']).sum()

    for i in range(0,df_PE_Original.shape[0]):
        if str.isdigit(df_PE_Original.iloc[i].name) == True:
            if df_PE_Original.iat[i,5] == '空':
                df_PE_Original.iat[i,3] = -df_PE_Original.iat[i,3]
                df_PE_Original.iat[i,5] = '多'
                # df_PE_Original.iloc[i]['TotalPosition']. = -df_PE_Original.copy().iloc[i]['TotalPosition']
                # df_PE_Original.iloc[i]['Direction'] = '多'
            else:
                pass
        else:
            pass


    # # 用多重索引核对仓位大小
    df_PE = df_PE_Original.groupby(['InstrumentID', 'Direction']).sum()
    df_HS.set_index(['证券代码','持仓多空标志'],inplace=True)

    # 将两个df合并
    df = pd.concat([df_HS,df_PE], axis=1, join='outer')

    # 比对仓位及多空
    df['check'] = df['持仓数量'] - df['TotalPosition']
    result = df[df['check'] != 0]
    if result.empty is True:
        print("账号为"+AccountID+"下的仓位无误！")
    else:
        result.reset_index([0,1],inplace=True)
        for i in range(0,result.shape[0]):
            print("在账号"+AccountID+"下"+querydate+'日')
            if result.loc[i]['check'] > 0:
                print("     证券代码为"+result.loc[i]['level_0']+"在"+result.loc[i]['level_1']+"仓上有误,恒生系统中比Nurex中多出"+str(result.loc[i]['check'])+"单位")
            else:
                print("     证券代码为"+result.loc[i]['level_0']+"在"+result.loc[i]['level_1']+"仓上有误,Nurex中比恒生系统中多出" + str(abs(result.loc[i]['check'])) + "单位")