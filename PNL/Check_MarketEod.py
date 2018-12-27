#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
检查marketEod中的价格是否正确
"""
import pandas as pd
import sys
sys.path.append(r'D:\CXM\Project\PNL')
import Constant
sys.path.append(r'D:\CXM\Project\SQLLINK')
import SASQL



dbsa = SASQL.ScenarioAnalysis()
dbnu = SASQL.Nurex()


def GetPrevDate(d,h):
    query = "select top {} TradeDate from Calendar where TradeDate<='{}' order by TradeDate desc".format(h+1,d)
    df = pd.read_sql(query,dbsa.conn)
    return df.iloc[h]['TradeDate']

#date = input("请输入要核对的日期：")
# query_cal = "SELECT [TradeDate] FROM [ScenarioAnalysis].[dbo].[Calendar] where TradeDate='{}'".format('20180101')
# cal = dbsa.ExecQuery(query_cal)

cal=[['2018-10-26'],['2018-10-29']]
for x in cal:

    date = x[0]
    print("当前日期为：" + x[0])
    prevdate = GetPrevDate(date,1)

    query_stock = "select * from HistData_Stock where Date='{}'".format(date)
    df_stock = pd.read_sql(query_stock,dbsa.conn,index_col='InstrumentID')

    query_stockpre = "select * from HistData_Stock where Date='{}'".format(prevdate)
    df_stockpre = pd.read_sql(query_stockpre,dbsa.conn,index_col='InstrumentID')


    query_future = "select * from HistData_Future_Daily where TradeDate='{}'".format(date)
    df_future = pd.read_sql(query_future,dbsa.conn,index_col='InstrumentID',)

    query_marketEod = "select * from MarketEod where Date = '{}'".format(date)
    df_marketEod = pd.read_sql(query_marketEod,dbnu.conn,index_col='InstrumentID')
    df_marketEod['InstrumentName'] = [x.encode('latin1').decode('gbk') for x in df_marketEod['InstrumentName']]




    for i in df_marketEod.index:

        if str.isalpha(i)==True:
            try:
                a = df_marketEod.loc[i]['PrevClosePrice']-df_future.loc[i]['PreClosePrice']
                b = df_marketEod.loc[i]['PrevSettlementPrice'] - df_future.loc[i]['PreSettlementPrice']
                c = df_marketEod.loc[i]['ClosePrice'] - df_future.loc[i]['ClosePrice']
                d = df_marketEod.loc[i]['SettlementPrice'] - df_future.loc[i]['SettlementPrice']
                e = df_marketEod.loc[i]['VolumeMultiple'] - df_future['multiplier']
            except KeyError as e:
                pass
            else:
                if a != 0 or b != 0 or c != 0 or d != 0 or e != 0:
                    print(' InstrumentID为'+i+',InstrumentName为'+df_marketEod.loc[i]['InstrumentName']+'价格有误')

        else:
            try:
               f = df_marketEod.loc[i]['PrevClosePrice'] - df_stockpre.loc[i]['closeprice']
               g = df_marketEod.loc[i]['ClosePrice'] - df_stock.loc[i]['closeprice']
            except KeyError as e:
                pass
            else:
                if f != 0 or g != 0:
                    print(' InstrumentID为' + i + ',InstrumentName为' + df_marketEod.loc[i]['InstrumentName'] + '价格有误')

