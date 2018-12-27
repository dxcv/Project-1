#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把Excel处理成panel数据
"""

import pandas as pd
import os
import numpy as np

# 获取原始数据文件夹中的所有文件
pathfromNumber = r'D:\CXM\Paper\Data\Original_BankScope\Number'
pathfromRatio = r'D:\CXM\Paper\Data\Original_BankScope\Ratios'
pathto = r'D:\CXM\Paper\Data\Cleaned'

files = os.listdir(pathfromNumber)

# a = pd.read_excel('D:\\CXM\\Paper\\Data\\OriginalData\\Number\\TotalOffBanlanceSheetItems.xlsx',index_col=0)
dfli = []
colli = []
for file in files:
    filepath = pathfromNumber+'\\'+file
    a = pd.read_excel(io=filepath, sheet_name=0, index_col=0, header=0)
    # # df.drop(columns=['证券简称'], inplace=True)
    # # df.index = [x.split('.')[0] for x in df.index]
    # # df.drop(columns=['证券简称'],inplace=True)
    a.columns = [x.split('\nCNY\n')[1] for x in a.columns]
    b = a.stack()
    # b = a.apply(lambda x:''.join(x.split(',')))
    colli.append(file.split('.')[0])
    dfli.append(b)
#
files = os.listdir(pathfromRatio)
for file in files:
    filepath = pathfromRatio+'\\'+file
    a = pd.read_excel(io=filepath, sheet_name=0, index_col=0, header=0)
    a.columns = [x.split('\n%\n')[1] for x in a.columns]
    b = a.stack()
    # b = a.apply(lambda x:''.join(x.split(',')))
    colli.append(file.split('.')[0])
    dfli.append(b)

df = pd.concat(dfli, axis=1, join='outer',sort=True)


#
# result = df.reset_index(level=[1])
# result.columns = ['BankName', 'Year'] + colli
#
# result.set_index('Year',inplace=True)
#
# # 强制转换数据类型
# # b = b.infer_objects()
# # result = result.apply(pd.to_numeric(float))
# # result = result.astype(float,errors='ignore')
#
#
# result.to_excel(pathto+'\\sortedfromBS.xlsx',index=False)
# # result.to_stata(pathto+'\\dtafortest.dta',write_index=False)