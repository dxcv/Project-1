#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
写入前一日仓位记录
"""

import pandas as pd
import openpyxl
from datetime import date,timedelta
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
import SASQL
sys.path.append(r'D:\CXM\Project\PNL\PNL')
import constant


today = constant.today.strftime('%Y-%m-%d %H:%M:%S')
yestoday = constant.yestoday.strftime('%Y%m%d')
dbnu = SASQL.Nurex()
# path_PNL = r'Z:\RiskM\损益\2017损益20180903_test.xlsm'
path_PNL = constant.path_PNL

# path_AccountStas = r'D:\CXM\Project\PNL\损益核对\综合信息查询_单元资产20180903.xlsx'
#
# AccountStas = pd.read_excel(io=path_AccountStas,sheet_name=0,header=0,index_col='资产单元编号')
#
# AccountID = ['77771','77772','77773','77774','77775','77776','77777','77778','77779']
#
# df = pd.read_excel(io=path_PNL,sheet_name='衍生品部',header=0,converters={'日期':str})
# df.set_index('日期',inplace=True)

query_posEod = "select Date,AccountID,InstrumentID,Portfolio,Direction,Price,TotalPosition,FundOccupied,MarketValue from PositionEod where Date = '{}'".format(yestoday)

positionEod = pd.read_sql(sql=query_posEod,con=dbnu.conn)
positionEod['Direction'] = [x.encode('latin1').decode('gbk') for x in positionEod['Direction']]

wb = openpyxl.load_workbook(filename=path_PNL)
ws = wb['posEod']

for i in range(0,positionEod.shape[0]):
    for j in range(0,positionEod.shape[1]):
        ws.cell(row=i+2,column=j+1).value = positionEod.iat[i,j]

wb.save(path_PNL)
wb.close()