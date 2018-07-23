# -*- coding: utf-8 -*-
"""
@author 陈祥明

依照portfolio、账户、板块获取持仓
"""
# import pandas as pd
# import ScenarioAnalysis
# from SQLLINK import MSSQL
# from ScenarioAnalysis import Constant

import sys
# sys.path.append(r'D:\CXM\Project_New\SQLLINK')
# sys.path.append(r'D:\CXM\Project_New\ScenarioAnalysis')
# import MSSQL
# import Constant
# import GetPosition
import DataClean



# Dataframe查询ParentID下的子portfolioID
def getpositionbyparentID(df, ID):
    df0 = df[df['parentID'] == ID]
    name_df0 = df0[['portfolioID']].drop_duplicates()
    name_li0 = DataClean.DataframeTolist(name_df0)
    for x in range(0,len(name_li0)):
        df1 = df[df['parentID'] == name_li0[x][0]]
        df0 = df0.append(df1)
        name_df1 = df1[['portfolioID']].drop_duplicates()
        name_li1 = DataClean.DataframeTolist(name_df1)
        for y in range(0, len(name_li1)):
            df2 = df[df['parentID'] == name_li1[y][0]]
            df0 = df0.append(df2)
            name_df2 = df2[['portfolioID']].drop_duplicates()
            name_li2 = DataClean.DataframeTolist(name_df2)
            for z in range(0, len(name_li2)):
                df3 = df[df['parentID'] == name_li2[z][0]]
                df0 = df0.append(df3)
    return df0



# # ###########################################获取当日部门仓位情况######################################
# # 数据来源为VaR数据库
# # 获取全部门仓位情况
# date = Constant.date
# dbvar = MSSQL.DB_VaR() #VaR实例
#
# query = 'select * from positionEod where Date=\'{}\' and portfolioID<>\'otc\''.format(date)
# Source = dbvar.ExecQuery(query)
#
# positions = {}
# if Source == []:
#    print('今日仓位数据尚未更新')
# else:
#    Dataset = []
#    for i in range(0, len(Source)):
#        a = (Source[i][2], Source[i][4], Source[i][6].encode('latin1').decode('gbk'), Source[i][7], Source[i][8])
#        Dataset.append(a)
# # print Dataset
# # 获取整个仓位情况，生成Dataframe，生成新列position，便于计算敞口
#    df = pd.DataFrame(Dataset, columns=['InstrumentID', 'Totalposition', 'direction', 'portfolioID', 'parentID'])
#    df['position'] = df['Totalposition']
#    df.loc[df['direction'] == '空', 'position'] = -df.loc[df['direction'] == '空', 'Totalposition']
#    li = Constant.portfolioID_list  # portfolio的ID
#    for i in range(0, len(li)):
#        if li[i] == 'ALL':
#            positions['ALL'] = df
#        else:
#            df0 = df[df['portfolioID'] == li[i]]
#            df1 = getpositionbyparentID(df, li[i])
#            df2 = df0.append(df1)
#            positions[li[i]] = df2
#    positions["indexarb+indexarb2"] = positions['indexarb'].append(positions['indexarb2'])
#
# # 输出至Excel
# #
# # 生成目标组合仓位情况
# target_list = Constant.targetID_list  # 目标组合
# results = {}
# for x in range(0, len(target_list)):
#     results[target_list[x]] = positions[target_list[x]].groupby('InstrumentID').sum()
#
# # print(positions['ALL'])
