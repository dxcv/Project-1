#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
基本面因子构成表-库存1
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从万得h获取数据并进行处理数据
"""
from WindPy import w
import pandas as pd
import numpy as np
import sys
import gc
sys.path.append(r'D:\CXM\Project\Commodity')
sys.path.append(r'D:\CXM\Project\SQLLINK')
import constant
import SASQL


dbdc = SASQL.DataCenter_Commodity()

path = 'Z:\personal\hebian\基本面数据\基本面因子组成结构表.xlsx'

# 读取全部指标的WindId
source = pd.read_excel(path, sheet_name='库存1', header=0)

print(source.shape[0])

w.start() # 启动Windpy

for x in range(0,source.shape[0]):
    # str_index = ','.join(j) # 拼接全部ItemID，用于查询数据
    a = w.edb(source.iat[x,6], "2010-01-01", "2018-11-26")
    df = pd.DataFrame()
    df['TradingDate'] = a.Times
    df['ProductID'] = source.iat[x,0]
    df['ProductName'] = source.iat[x,1]
    df['IndexName'] = np.nan
    df['Secu_Arrb'] = source.iat[x, 2]
    df['Data'] = a.Data[0]
    df['Frequency'] = source.iat[x, 4]
    df['Unit'] = source.iat[x, 3]
    df['DataSource'] = source.iat[x, 5]
    print(source.iat[x,0])
    df.to_sql('Commodity_Inventory', dbdc.conn, if_exists='append', index=False, chunksize=1000)
w.stop()
