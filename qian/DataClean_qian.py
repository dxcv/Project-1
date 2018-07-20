# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 17:38:49 2018

@author: 陈祥明
"""

import pandas as pd
import numpy as np
import openpyxl 
path = r'D:\CXM\Project_New\qian\template.xlsx'

source = pd.read_excel(io=path, sheet_name='1', header=0)

#data = source.groupby(source.index.map(lambda x: x.year))
yearlist = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
wb = openpyxl.load_workbook(path)
ws = wb['2']
for i in range(0, len(yearlist)):
    df0 = source.loc[yearlist[i]]
    df1 = df0[(df0.index.month != 2) | (df0.index.day != 29)].copy() # 去掉2月29号
    df1.fillna('#N/A', inplace=True)
    a = np.array(df1).tolist()
    for j in range(0, len(a)):
        ws.cell(row=j+2, column=i+2).value = a[j][0]

wb.save(path)
wb.close()

