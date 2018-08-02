#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从万得更新数据数据
"""
from WindPy import w
import pandas as pd
import numpy as np
from datetime import datetime
import sys
import gc
sys.path.append(r'D:\CXM\Project_New\Commodity')
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import constant
import MSSQL



# dbdc = SASQL.DataCenter_Commodity()
# tbco = SASQL.Commodity
today = constant.date
dbdc = MSSQL.DB_DataCenter_Commodity()
path = constant.path_Data_Sorted

# 读取全部指标的WindId
xls = pd.ExcelFile(path) # Excel对象
nameli = xls.sheet_names
print(nameli)
xls_dic = {}
for i in nameli:
    xls_dic[i] = pd.read_excel(xls, sheet_name=i, header=0).fillna('#N/A')

def cutlist(li, width=5): # 将长list分隔，按一定长度输出
    a = []
    l = len(li)/width
    for x in range(0, int(l)):
        a.append(li[(width*x):(width*(x+1))])
    if li[int(l) * width:] == []:
        pass
    else:
        a.append(li[int(l)*width:])
    return a


def patchdict(dic, k): #将字典中的dataframe全部拼接
    a = dic[k[0]]
    for i in range(1, len(k)):
        a = pd.concat([a,dic[k[i]]])
    return a

def DataCleanWind(Windobj): # 处理万得返回的数据，将Wind对象处理成list
    df = pd.DataFrame(columns=Windobj.Codes, index=Windobj.Times)  # 将wind返回的对象处理成dataframe
    for m in range(0, len(Windobj.Codes)):
        df[Windobj.Codes[m]] = Windobj.Data[m]
    return df

source = patchdict(xls_dic, nameli)  # 全部字段
del xls_dic
del xls
gc.collect()

str_index_cut = []
li_index = [x[0] for x in np.array(source[['ItemID']].drop_duplicates()).tolist()] #生成全部ItemID的list
a = cutlist(li_index)
for j in a:
    str_index = ','.join(j)  # 拼接全部ItemID，用于查询数据
    str_index_cut.append(str_index)

w.start() # 启动Windpy

for x in str_index_cut:
    # str_index = ','.join(j) # 拼接全部ItemID，用于查询数据
    a = w.edb(x, today, today)
    df = DataCleanWind(a)
    del a
    gc.collect()
    for n in df.columns:
        df0 = source[source['ItemID'] == n].drop_duplicates()
        df1 = df[[n]].dropna()
        for y in range(0, df0.shape[0]):
            for z in range(0, df1.shape[0]):
                try:
                    query = "insert into Commodity(Date,CategoryID,CategoryName,ProductID, ProductName, ClassID,ClassName,ItemID,ItemName,Frequency,Unit,Source,UpdateSource,Data) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{})".format(df1.index[z], df0.iloc[y][0], df0.iloc[y][1],df0.iloc[y][2], df0.iloc[y][3], df0.iloc[y][4], df0.iloc[y][5], df0.iloc[y][6], df0.iloc[y][7],df0.iloc[y][8], df0.iloc[y][9], df0.iloc[y][10], df0.iloc[y][11],df1.iloc[z][0])
                    # print(query)
                except IndexError as e:
                    print(e)
                    print(str(n))
                else:
                    dbdc.ExecNonQuery(query)
            print("Wind代码为" + str(n) + "的数据写入成功")
        del df0
        del df1
        gc.collect()  #回收内存,防止内存被挤爆=。=
    del df
    gc.collect()
w.stop()
