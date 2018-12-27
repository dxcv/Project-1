#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
私募基金情况统计, 数据易超限
"""

from WindPy import w
from openpyxl import load_workbook
from datetime import datetime,timedelta
import pandas as pd
import numpy as np
import calendar
from functools import reduce
import math

#获取今年的第一天
def getBeginDate():
    y = datetime.today().year
    BeginDate = datetime(y,1,1).strftime("%Y-%m-%d")
    return BeginDate

def getEndDate():
    y = datetime.today().year
    m = datetime.today().month-1
    days = calendar.monthrange(y,m)[1]
    EndDate = datetime(y,m,days).strftime("%Y-%m-%d")
    return EndDate

def excelAddSheet(dataframe, excelWriter, sheet_name):
    book = load_workbook(excelWriter.path)
    excelWriter.book = book
    dataframe.to_excel(excel_writer=excelWriter, sheet_name=sheet_name, index=None)
    excelWriter.save()
    excelWriter.close()


def DataCleanWind(Windobj): # 处理万得返回的数据，将Wind对象处理成list
    df = pd.DataFrame(columns=Windobj.Fields, index=Windobj.Times)  # 将wind返回的对象处理成dataframe
    for m in range(0, len(Windobj.Fields)):
        df[Windobj.Fields[m]] = Windobj.Data[m]
    return df


def getRiskFreeRate(bt,et): #获得一年期无风险国债收益率的几何平均
    Windobj = w.edb("S0059744",beginTime=bt, endTime=et)
    while Windobj.ErrorCode == -40520007:
        Windobj = w.edb("S0059744", beginTime=bt, endTime=et)
    RiskFreeRate = pow(reduce(lambda x,y:x*y,Windobj.Data[0]),1.0/len(Windobj.Data[0]))/100
    return RiskFreeRate #返回df，列名为CLOSE

def getData(wcode,bt,et,ifAnnualized=1,col="return,nav"):
    Windobj = w.wsd(codes=wcode, fields=col, beginTime=bt, endTime=et,options="annualized=" + str(ifAnnualized))
    if Windobj.ErrorCode == -40520007:
        df = pd.DataFrame()
        print(wcode+"无数据")
    elif Windobj.ErrorCode==-40522017:
        df = pd.DataFrame()
        print("数据超限")
    else:
        df = DataCleanWind(Windobj)
        df.replace({None: np.nan},inplace=True)
        df.dropna(how='any')
    return df #返回dataframe，默认第一列为RETURN,第二列为NAV


def getRatios(df,RF):  #依照传入的dataframe计算相关指标
    if df.empty==True:
        pass
    else:
        ret = (np.array(df[['RETURN']].drop_duplicates()).tolist())[0][0]/100 #期间年化收益
        std = df['NAV'].std() #波动率，用标准差表示
        if std == 0:
            SR = std
        else:
            SR = (ret-RF)/std/100

        df['MaxDrawDown'] = np.nan #计算最大回撤
        for x in range(1,len(df)):
            a = df.head(x)
            b = a['NAV'].max()
            c = df.iat[x-1,1]
            d = min(c-b,0)
            e = d/b
            df.iat[x-1,2] = e
        MDD = abs(df['MaxDrawDown'].min()) #最大回撤

        return ret,std,MDD,SR


BeginDate = getBeginDate() #需要时手动更改
EndDate = getEndDate()

ToPath = r'D:\CXM\Project\策略收益统计'+'\\'+EndDate.split('-')[0]+'年至今量化私募市场表现.xlsx'
ExcelWriter = pd.ExcelWriter(ToPath,engine='openpyxl')

pd.DataFrame().to_excel(ToPath)  #excel必需已经存在，因此先建立一个空的sheet

w.start()
RF = getRiskFreeRate(BeginDate,EndDate)
filepath = r'D:\CXM\Project\策略收益统计\策略收益汇总.xlsx'

IndexExcel = pd.read_excel(filepath,sheet_name=None,header=0,index_col=0)

for x in IndexExcel.keys():
    Indexdf = IndexExcel[x]
    for y in Indexdf.index:
        print(y)
        data = getData(y, BeginDate, EndDate)
        # print(data)
        result = getRatios(data, RF)
        print(result)
        Indexdf.at[y, '年化收益率'] == result[0]
        Indexdf.at[y, '波动率'] == result[1]
        Indexdf.at[y, '最大回撤'] == result[2]
        Indexdf.at[y, 'sharp'] == result[3]
    Indexdf.dropna(inplace=True)
    excelAddSheet(dataframe=Indexdf, excelWriter=ExcelWriter, sheet_name=x)


