#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成Twapprice
"""

import pandas as pd
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

filepath = r'C:\Users\Admin\Desktop\互换执行20180911合并.xlsx'

df = pd.read_excel(io=filepath,converters={'证券代码':str})
df.set_index('证券代码',inplace=True)

for i in df.index:
    t = df.at[i,'time']

