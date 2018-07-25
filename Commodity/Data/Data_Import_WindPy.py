#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从万得h获取数据并进行处理数据
"""
from WindPy import w
import pandas as pd
import numpy as np
import sys
sys.path.append(r'D:\CXM\Project_New\Commodity')
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import constant
import SASQL


dbdc = SASQL.DataCenter_Commodity()
tbco = SASQL.Commodity
path = constant.path_Data_Sorted

# 读取全部指标的WindId
xls = pd.ExcelFile(path) # Excel对象
nameli = xls.sheet_names
print(nameli)
xls_dic = {}
for i in nameli:
    xls_dic[i] = pd.read_excel(xls,sheet_name=i,header=0).fillna('#N/A')

def cutlist(li, width=15):
    a = []
    l = len(li)/width
    for x in range(0, int(l)):
        a.append(li[(width*x):(width*(x+1))])
    if li[int(l) * width:] == []:
        pass
    else:
        a.append(li[int(l)*width:])
    return a


w.start() # 启动Windpy

for i in nameli:
    source = xls_dic[i]
    li_index = [x[0] for x in np.array(source[['ItemID']].drop_duplicates()).tolist()] #生成全部ItemID的list
    li_index_cut = cutlist(li_index)
    for j in li_index_cut:
        str_index = ','.join(j) # 拼接全部ItemID，用于查询数据
        a = w.edb(str_index, '19000101', '20180724')
        df = pd.DataFrame(columns=a.Codes, index=a.Times) #将wind返回的对象处理成dataframe
        for m in range(0,len(a.Codes)):
            df[a.Codes[m]] = a.Data[m]
        for n in a.Codes:
            df0 = source[source['ItemID']==n]
            df1 = df[[n]].dropna()
            for x in range(0,df1.shape[0]):
                record = tbco(Date=df1.index[x], CategoryID=df0.iloc[0][0], CategoryName=df0.iloc[0][1],ProductID=df0.iloc[0][2], ProductName=df0.iloc[0][3], ClassID=df0.iloc[0][4],ClassName=df0.iloc[0][5], ItemID=df0.iloc[0][6], ItemName=df0.iloc[0][7],Frequency=df0.iloc[0][8], Unit=df0.iloc[0][9], Source=df0.iloc[0][10],UpdateSource=df0.iloc[0][11],Data=df1.iloc[x][0])
                dbdc.session.add(record)
                dbdc.session.commit()
dbdc.session.close()
w.stop()
# print(li_index)
# print(str_index)



    # a = w.edb('S5806088,S5806089', '20160101', '20180701')


# a = w.edb('S5806088,S5806089','20160101','20180701')
# df = pd.DataFrame(columns=a.Codes,index=a.Times)
# for i in range(0, len(a.Codes)):
#     df[a.Codes[i]] = a.Data[i]
# print(df)

# df0 = xls_dic['有色金属'][xls_dic['有色金属']['ItemID']=='S5806088']
# df1 = df[['S5806088']]
# df1 = df1.dropna()
#
# record = tbco(Date=df1.index[0],CategoryID=df0.iloc[0][0],CategoryName=df0.iloc[0][1],ProductID=df0.iloc[0][2],ProductName=df0.iloc[0][3],ClassID=df0.iloc[0][4],ClassName=df0.iloc[0][5],ItemID=df0.iloc[0][6],ItemName=df0.iloc[0][7],Frequency=df0.iloc[0][8],Unit=df0.iloc[0][9],Data=df1.iloc[0][0])
#
# dbdc.session.add(record)
# dbdc.session.commit()
#
# w.stop()