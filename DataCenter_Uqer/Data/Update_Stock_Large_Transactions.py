#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
沪深股票大宗交易行情
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

df_Stock_Large_Transactions = DataAPI.MktBlockdGet(tradeDate=date)
df_Stock_Large_Transactions.columns = ['TradeDate','SecID','Code','AssetClass','ExchangeCD','Name','CurrenyCD','TradePrice','TradeValue','TradeVol','BuyerBD','SellerBD']

df_Stock_Large_Transactions.to_sql('Stock_Large_Transactions',dbqu.conn,if_exists='append',index=False,chunksize=1000)

