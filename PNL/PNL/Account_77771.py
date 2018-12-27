#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新sheet衍生品部77771
"""

import pandas as pd
import openpyxl
from datetime import datetime,timedelta
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
import SASQL
sys.path.append(r'D:\CXM\Project\PNL\PNL')
import constant



yestoday = '2018-09-03'#constant.yestoday.strftime('%Y-%m-%d')
dbnu = SASQL.Nurex()
dbOC = SASQL.OptionContract()

path_capital = r'D:\CXM\Project\PNL\PNL\损益\综合信息查询_单元资产20180903.xls'
path_cashflow = r'D:\CXM\Project\PNL\PNL\损益\综合信息查询_资金流水20180903.xls'
path_trading = constant.path_trading
path_PNL = constant.path_PNL

df_capital = pd.read_excel(path_capital,sheet_name=0,header=0,converters={'资产单元编号':str})
df_capital.set_index('资产单元编号',inplace=True)
df_cashflows = pd.read_excel(path_cashflow,sheet_name=0,header=0,converters={'资产单元编号':str})
df_trading = pd.read_excel(path_cashflow,sheet_name='权益汇总',header=0,converters={'日期':str})
df_trading['日期'] = [x[0:10] for x in df_trading['日期']]
df_trading.set_index('日期',inplace=True)


AccountID = '77771'
df_77771 = pd.read_excel(path_PNL,sheet_name='衍生品部'+AccountID,converters={'日期':str})
df_77771['日期'] = [x[0:10] for x in df_77771['日期']]
df_77771.set_index('日期',inplace=True)


query_MV = "SELECT SUM(MarketValue) FROM [Nurex].[dbo].[PositionEod] where Date='{}' and AccountID='{}'".format(yestoday,AccountID)
df_stat = pd.read_sql(sql=query_MV,con=dbnu.conn)


# 写入新记录
df_77771.at[yestoday,'持仓市值'] = df_stat.iat[0,0]
df_77771.at[yestoday,'现金'] = df_capital.at[AccountID,'当前现金余额']
df_77771.at[yestoday,AccountID+'总资产'] = df_77771.at[yestoday,'持仓市值'] + df_77771.at[yestoday,'现金']


df_cashchange = df_cashflows[((df_cashflows['发生业务'] == '减少现金') | (df_cashflows['发生业务'] == '增加现金')) & df_cashflows['资产单元编号'] == AccountID]
if df_cashchange.empty is True:
    pass
else:
    df_77771.at[yestoday,'资金变动'] = df_cashchange.sum('发生金额')


df_77771.at[yestoday,'期权总权益'] = df_trading.at[yestoday,'汇总权益']
df_77771.at[yestoday,'保证金账户余额'] = df_77771.sum('保证金账户资金变动')