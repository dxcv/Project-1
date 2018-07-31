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
import MSSQL


# dbdc = SASQL.DataCenter_Commodity()
# tbco = SASQL.Commodity
dbdc = MSSQL.DB_DataCenter_Commodity()
path = constant.path_Data_Sorted

# 读取全部指标的WindId
xls = pd.ExcelFile(path) # Excel对象
nameli = xls.sheet_names
print(nameli)
xls_dic = {}
for i in nameli:
    xls_dic[i] = pd.read_excel(xls, sheet_name=i, header=0).fillna('#N/A')

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
        a = w.edb(str_index, '19000101', '20180730')
        df = pd.DataFrame(columns=a.Codes, index=a.Times) #将wind返回的对象处理成dataframe
        for m in range(0,len(a.Codes)):
            df[a.Codes[m]] = a.Data[m]
        for n in a.Codes:
            df0 = source[source['ItemID']==n]
            df1 = df[[n]].dropna()
            for x in range(0,df1.shape[0]):
                try:
                    query = "insert into Commodity(Date,CategoryID,CategoryName,ProductID, ProductName, ClassID,ClassName,ItemID,ItemName,Frequency,Unit,Source,UpdateSource,Data) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{})".format(df1.index[x], df0.iloc[0][0], df0.iloc[0][1],df0.iloc[0][2], df0.iloc[0][3], df0.iloc[0][4], df0.iloc[0][5], df0.iloc[0][6], df0.iloc[0][7],df0.iloc[0][8], df0.iloc[0][9], df0.iloc[0][10], df0.iloc[0][11],df1.iloc[x][0])
                except IndexError as e:
                    print("Wind代码为"+str(ItemID=df0.iloc[0][6])+"的字段没有数据")
#                 record = tbco(Date=df1.index[x], CategoryID=df0.iloc[0][0], CategoryName=df0.iloc[0][1],ProductID=df0.iloc[0][2], ProductName=df0.iloc[0][3], ClassID=df0.iloc[0][4],ClassName=df0.iloc[0][5], ItemID=df0.iloc[0][6], ItemName=df0.iloc[0][7],Frequency=df0.iloc[0][8], Unit=df0.iloc[0][9], Source=df0.iloc[0][10],UpdateSource=df0.iloc[0][11],Data=df1.iloc[x][0])
#                 dbdc.session.add(record)
#                 dbdc.session.commit()
# dbdc.session.close()
                else:
                    dbdc.ExecNonQuery(query)
w.stop()
