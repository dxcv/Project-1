#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把Excel处理成panel数据
"""

import pandas as pd

df = pd.read_excel(r'D:\CXM\STATA\Data\Source\456.xls',index_col=0,header=0)

a = df.stack()

b = a.reset_index(level=[0,1])
b.columns=['Country','Year','gold']

# b.to_excel(r'C:\Users\ZHAIYUE\Desktop\test.xlsx',index=False)
b.to_stata(r'C:\Users\ZHAIYUE\Desktop\test.dta',write_index=False,)