#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用递归和map查询全部子portfolio
"""
from functools import reduce

import pandas as pd
import numpy as np
import sys
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import MSSQL


dbsa = MSSQL.DB_ScenarioAnalysis()
query  = "select * from positionEod where Date = '20180720'"
source = dbsa.ExecQuery(query)
Dataset = []
for i in source:
    a = (i[2], i[3], i[5].encode('latin1').decode('gbk'), i[6], i[7])
    Dataset.append(a)

data = pd.DataFrame(Dataset,columns=['InstrumentID', 'Totalposition', 'direction', 'portfolioID', 'parentID'])

df_empty = pd.DataFrame(columns=['InstrumentID', 'Totalposition', 'direction', 'portfolioID', 'parentID'])



def Getposition(ID, df=data):
    df1 = df[df['parentID'] == ID]
    name_li = np.array(df1[['portfolioID']].drop_duplicates()).tolist()
    li = [x[0] for x in name_li]
    if li == []:
        return df1
    else:
        return df1.append(list(map(Getposition, li)))

res = Getposition('alpha_300').append(data[data['portfolioID']=='alpha_300'])
print(res)
print(res.shape[0])
# print(res)







