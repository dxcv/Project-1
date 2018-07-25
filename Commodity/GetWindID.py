#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
读取全部指标的WindId
"""
import pandas as pd
import sys
from WindPy import w
sys.path.append(r'D:\CXM\Project_New\Commodity')
import constant

path = constant.path_Data_Sorted

xls = pd.ExcelFile(path)
nameli = xls.sheet_names
print(nameli)
xls_dic = {}
for i in nameli:
    xls_dic[i] = pd.read_excel(xls,sheet_name=i,header=0)
# df = dataset[['ItemID']]
# print(df)