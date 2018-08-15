# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 17:38:49 2018

@author: 陈祥明
"""
from datetime import datetime
import pandas as pd
import numpy as np
from openpyxl import load_workbook
path = r'D:\CXM\Project_New\qian\template.xlsx'

excel = load_workbook(path)
writer = pd.ExcelWriter(path,engine='openpyxl')
writer.book=excel

source = pd.read_excel(io=path,sheet_name='Source',header=0,index_col=0)

# yearlist = source.index.year

dfli = []
for i in range(2004,2019):
    df = source[source.index.year == i]
    df.columns = [i]
    df1 = pd.DataFrame(index=[x.strftime('%m-%d') for x in df.index],data=np.array(df[[i]]).tolist(),columns=[i])
    df1.fillna('#N/A',inplace=True)
    dfli.append(df1)

result = pd.concat(dfli,axis=1,join='outer',sort=True)

# result.to_excel(r'D:\CXM\Project_New\qian\template.xlsx',sheet_name='2',mode='a')
result.to_excel(writer,'Cleaned')
writer.save()