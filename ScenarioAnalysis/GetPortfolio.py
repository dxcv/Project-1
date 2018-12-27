# # -*- coding: utf-8 -*-
# """
# @author 陈祥明
#
# 依照portfolio、账户、板块获取持仓
# """
# import pandas as pd
# import numpy as np
# from SQLLINK import SASQL
# # from ScenarioAnalysis import Constant
#
# import sys
# # sys.path.append(r'D:\CXM\Project_New\SQLLINK')
# # # import SASQL
# sys.path.append(r'D:\CXM\Project_New\ScenarioAnalysis')
# # import MSSQL
# import Constant
# # import GetPosition
# import DataClean
#
# dbnu = SASQL.Nurex()
#
# query = "select PortfolioID,ParentID from Portfolio where Product='prop'"
#
# source = pd.read_sql(query,dbnu.conn,)
#
#
# def Getportfolio(ID, df=source):  # 递归查询
#     df1 = df[df['ParentID'] == ID]
#     name_li = np.array(df1[['PortfolioID']].drop_duplicates()).tolist()
#     li = [x[0] for x in name_li]
#     if li == []:
#         return df1
#     else:
#         return df1.append(list(map(Getportfolio, li)))
#
# portfolioli = ['ALL', 'alpha_prop', 'alpha_300', 'alpha_500', 'indexarb', 'indexarb2', 'macro', 'cta', 'stock']
# portfolio = {}
#
#
# for i in portfolioli:
#     if i == 'ALL':
#         portfolio['ALL'] = source
#     else:
#         portfolio[i] = Getportfolio(i).append(source[source['PortfolioID'] == i])
#
# portfolio["indexarb+indexarb2"] = portfolio['indexarb'].append(portfolio['indexarb2'])
#
# print(portfolio)
# # Dataframe查询ParentID下的子portfolioID
# # def getpositionbyparentID(df, ID):
# #     df0 = df[df['parentID'] == ID]
# #     name_df0 = df0[['portfolioID']].drop_duplicates()
# #     name_li0 = DataClean.DataframeTolist(name_df0)
# #     for x in range(0,len(name_li0)):
# #         df1 = df[df['parentID'] == name_li0[x][0]]
# #         df0 = df0.append(df1)
# #         name_df1 = df1[['portfolioID']].drop_duplicates()
# #         name_li1 = DataClean.DataframeTolist(name_df1)
# #         for y in range(0, len(name_li1)):
# #             df2 = df[df['parentID'] == name_li1[y][0]]
# #             df0 = df0.append(df2)
# #             name_df2 = df2[['portfolioID']].drop_duplicates()
# #             name_li2 = DataClean.DataframeTolist(name_df2)
# #             for z in range(0, len(name_li2)):
# #                 df3 = df[df['parentID'] == name_li2[z][0]]
# #                 df0 = df0.append(df3)
# #     return df0
# #
#
#
