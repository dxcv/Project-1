#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成交易日历
"""

import pandas as pd
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')
import SASQL

dbsa = SASQL.ScenarioAnalysis()


query_del = "delete from Calendar"
dbsa.ExecNonQuery(query_del)

query1 = "select distinct(Date) from HistData_Stock order by Date desc"
df = pd.read_sql(query1,dbsa.conn)


df.columns = ['TradeDate']

df.to_sql('Calendar',dbsa.conn,if_exists='append',index=False,chunksize=1000)

