# -*- coding: utf-8 -*-
"""
@author: 陈祥明

用于计算市值、敞口、VaR
"""
import pandas as pd
from datetime import datetime,timedelta
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
sys.path.append(r'D:\CXM\Project\ScenarioAnalysis')
import MSSQL
import Constant
# import GetPosition
import Calculator
import DataClean

# import Constant as co
# import GetPosition

dbsa = MSSQL.DB_ScenarioAnalysis()
#
# def Daysago(x=200):
#     daysago = datetime.today() + timedelta(-x)
#     return daysago.strftime('%Y%m%d')


# 用于计算的函数
# 计算股票市值及敞口
def StockValue(InstrumentID, position, position_net, Date):
    query1 = "select closeprice from HistData_Stock where InstrumentID='{0}' and Date='{1}'".format(InstrumentID, Date)
    closeprice = dbsa.ExecQuery(query1)
    if closeprice == []:
        return 0, 0
    else:
        MV = closeprice[0][0]*position
        Expo = closeprice[0][0]*position_net
        return MV, Expo

# 计算单个期货合约市值及敞口
def FutureValue(InstrumentID, position, position_net, Date):
    a = list(filter(str.isalpha, str(InstrumentID)))
    productID = ''.join(a).upper()
    # productID = str.join(a).upper()
    query1 = "select SettlementPrice from MarketEod where InstrumentID='{0}' and Date='{1}'".format(InstrumentID, Date)
    SettlementPrice = dbsa.ExecQuery(query1)
    query2 = "select Multiplier from Future_Multiplier where ProductID='{0}' and RecordDate='{1}'".format(productID, Date)
    m = dbsa.ExecQuery(query2)
    MV = SettlementPrice[0][0]*m[0][0]*position
    Expo = SettlementPrice[0][0]*m[0][0]*position_net
    return MV, Expo
    
# 计算单支票的历史波动
# Expo为敞口
# 股票
def StockVaR(InstrumentID, Expo, Date, Interval=200):
    # 获取历史时间段的涨跌幅
    query = "select top {0} PriceChangePercent from HistData_Stock where InstrumentID = '{1}'  and Date <= '{2}' order by Date desc".format(Interval, InstrumentID, Date)
    pcp = dbsa.ExecQuery(query)
    if pcp is []:
        pass
    else:
        SV = [Expo*x[0] for x in pcp]
        # SV = int(Position)*closeprice[0][0]*pcp[0][0]
        # 返回一个list
        return SV

# 期货
def FutureVaR(InstrumentID, Expo, Date, Interval=200):
    a = list(filter(str.isalpha, str(InstrumentID)))
    productID = ''.join(a).upper()
    query = 'select top {0} PriceChangePercent from HistData_Future_Continuing where productID = \'{1}\' and tradingDate <= \'{2}\' order by tradingDate desc'.format(Interval, productID, Date)
    pcp = dbsa.ExecQuery(query)
    FV = [Expo*x[0] for x in pcp]
    # FV = Position*closeprice[0][0]*pcp[0][0]*m[0][0]
    # 返回一个list
    return FV

# 计算组合的市值及敞口
def PortfolioMvOrExpo(df, Date): # 传入仓位df
    df['MV'] = 0
    df['Expo'] = 0  # 生成新列，记录市值和敞口
    stock = DataClean.StockOrFuture(df, len(df))[0]
    future = DataClean.StockOrFuture(df, len(df))[1]
    for m in stock:
        res = StockValue(m, df.loc[m][0], df.loc[m][1], Date)
        df.loc[m]['MV'] = res[0]
        df.loc[m]['Expo'] = res[1]
    for n in future:
        res = FutureValue(n, df.loc[n][0], df.loc[n][1], Date)
        df.loc[n]['MV'] = res[0]
        df.loc[n]['Expo'] = res[1]
    return df

# 计算组合的VaR
def PortfolioVaR(df, date):
    Namelist = list(df.index)
    # 声明一个空的Dataframe，准备填充数据
    df_var = pd.DataFrame(columns=Namelist)
    position_stock = DataClean.StockOrFuture(df, len(df))[0]
    position_future = DataClean.StockOrFuture(df, len(df))[1]
    for i in position_stock:
        # 解决股票历史数据不满足两百天的问题
        df_var[i] = pd.Series(StockVaR(i, df.loc[i]['Expo'], date))
    for j in position_future:
        df_var[j] = pd.Series(FutureVaR(j, df.loc[j]['Expo'], date))
    df_var.fillna(0)
    return df_var

# 计算组合的市值

#####################################计算市值及敞口###################################
#MV_Expo_df={}
#li = co.targetID_list 
##计算组合市值、敞口,保留结果
#for x in range(0,len(li)):
#    position_df = GetPosition.Positions[li[x]]
#    position_df['MV']=0
#    position_df['Expo']=0
#    position_stock = DC.StockOrFuture(position_df,len(position_df))[0]
#    position_future = DC.StockOrFuture(position_df,len(position_df))[1]
#    for m in range(0,len(position_stock)):
#        res = StockValue(position_stock[m],position_df.loc[position_stock[m]][0],position_df.loc[position_stock[m]][1],date)
#        position_df.loc[position_stock[m]]['MV']=res[0]
#        position_df.loc[position_stock[m]]['Expo']=res[1]
#            
#    for n in range(0,len(position_future)):
#        res = FutureValue(position_future[n],position_df.loc[position_future[n]][0],position_df.loc[position_future[n]][1],date)
#        position_df.loc[position_future[n]]['MV']=res[0]
#        position_df.loc[position_future[n]]['Expo']=res[1]
#    MV_Expo_df[li[x]] = position_df


#
#
#VaR_df = {}
#for y in range(0,len(li)):
#    VaR_df[li[y]]=PortfolioVaR(MV_Expo_df[li[y]],date)
#
#print MV_Expo_df
#print VaR_df
#
#
##dbvar.close()


