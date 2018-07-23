# -*- coding: utf-8 -*-
"""

@author: 陈祥明

计算VaR主程序

"""

import pandas as pd
import numpy as np
import openpyxl
import sys
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import MSSQL
sys.path.append(r'D:\CXM\Project_New\ScenarioAnalysis')
import Constant
import GetPosition
import Calculator
import DataClean

#################################获取当日部门整体仓位情况##############################
date = Constant.date
dbsa = MSSQL.DB_ScenarioAnalysis()
target_list = Constant.targetID_list  # 目标组合
positions = {}

# 获取全部门仓位情况
query = 'select * from positionEod where Date=\'{}\' and portfolioID<>\'otc\''.format(date)
Source = dbsa.ExecQuery(query)
if Source == []:
    print('今日仓位数据尚未更新')
else:
    Dataset = []
    for i in range(0, len(Source)):
        a = (Source[i][2], Source[i][3], Source[i][5].encode('latin1').decode('gbk'), Source[i][6], Source[i][7])
        Dataset.append(a)



    # 获取整个仓位情况，生成Dataframe，生成新列position，用于计算敞口
    data = pd.DataFrame(Dataset, columns=['InstrumentID', 'Totalposition', 'direction', 'portfolioID', 'parentID'])
    data['position'] = data['Totalposition']
    data.loc[data['direction'] == '空', 'position'] = -data.loc[data['direction'] == '空', 'Totalposition']
    li = Constant.portfolioID_list  # portfolio的ID


    def Getposition(ID, df=data):
        df1 = df[df['parentID'] == ID]
        name_li = np.array(df1[['portfolioID']].drop_duplicates()).tolist()
        li = [x[0] for x in name_li]
        if li == []:
            return df1
        else:
            return df1.append(list(map(Getposition, li)))

    for i in li:
        if i == 'ALL':
            positions['ALL'] = data
        else:
            positions[i] = Getposition(i).append(data[data['portfolioID']==i])
    positions["indexarb+indexarb2"] = positions['indexarb'].append(positions['indexarb2'])

    #

        # 输出至Excel
    path_position = Constant.path_position
    path_position_save = Constant.path_position_save
    wb = openpyxl.load_workbook(path_position)
    for i in target_list:
        ws = wb[i]
        df_to_excel = positions[i]
        for x in range(0, df_to_excel.shape[0]):
            for y in range(0, df_to_excel.shape[1]-1):
                ws.cell(row=x+2, column=y+1).value = df_to_excel.iloc[x][y]
    wb.save(path_position_save)
    wb.close()

    #


    # 生成目标组合仓位情况
    results = {}
    for x in range(0, len(target_list)):
        results[target_list[x]] = positions[target_list[x]].groupby('InstrumentID').sum()

    # print(positions['ALL'])

    ###################################      计算市值及敞口     ###############################
    MV_Expo_df = {}
    # 计算组合市值、敞口,保留结果
    for x in target_list:
        df_mv_expo = Calculator.PortfolioMvOrExpo(results[x], date)
        MV_Expo_df[x] = df_mv_expo

    ############################         计算VaR       ##########################
    VaR_df = {}
    for y in target_list:
        VaR_df[y] = Calculator.PortfolioVaR(MV_Expo_df[y], date)
        VaR_df[y].fillna(0, inplace=True)  # 处理因为货基或者股票存续时间不足两百天带来的缺失值

    #print MV_Expo_df
    #print VaR_df


    #
    #
    ###################   获取单支票的VaR、市值、及敞口,写入数据库   ##################
    VaRset = VaR_df['ALL']
    MV_Exposet = MV_Expo_df['ALL']
    var_record_single = []
    for i in VaRset.columns:
       a = DataClean.getOrder_df(VaRset, i)
       b = str(i)
       if str.isdigit(b)==True:
           query = "insert into VaR_record(date,portfolioID,InstrumentID,productID,VaR_95,Marketvalue,Exposure) values('{0}','{1}','{2}','{3}',{4},{5},{6})".format(date, '无', i, 'stock', a, MV_Exposet.loc[i]['MV'], MV_Exposet.loc[i]['Expo'])
           dbsa.ExecNonQuery(query)
           # c = (date, '无', VaRset.columns[i], 'stock', a, MV_Exposet.loc[VaRset.columns[i]]['MV'],MV_Exposet.loc[VaRset.columns[i]]['Expo'])
           # var_record_single.append(c)
       else:
           c = list(filter(str.isalpha, str(i)))
           productID = ''.join(c).upper()
           # productID = str(filter(str.isalpha, str(i))).upper()
           query = "insert into VaR_record(date,portfolioID,InstrumentID,productID,VaR_95,Marketvalue,Exposure) values('{0}','{1}','{2}','{3}',{4},{5},{6})".format(date, '无', i, productID, a, MV_Exposet.loc[i]['MV'], MV_Exposet.loc[i]['Expo'])
           dbsa.ExecNonQuery(query)
           # c=(date, '无', VaRset.columns[i], productID, a, MV_Exposet.loc[VaRset.columns[i]]['MV'], MV_Exposet.loc[VaRset.columns[i]]['Expo'])
           # var_record_single.append(c)


    # ##############################获取组合VaR及敞口#################################
    #
    # 获取VaR记录
    var_record_portfolio = {}
    for i in target_list:
        df_var = VaR_df[i]
        df_var['col_sum'] = df_var.apply(lambda x: x.sum(), axis=1)
    #    var_record_portfolio[target_list[i]] = df_var
        var_record_portfolio[i] = DataClean.getOrder_df(df_var, 'col_sum')

    mv_record_portfolio = {}
    expo_record_portfolio = {}

    # 获取市值及敞口记录

    for i in target_list:
        df = MV_Expo_df[i]
        df.loc['row_sum'] = df.apply(lambda x: x.sum())
        mv_record_portfolio[i] = df.loc['row_sum']['MV']
        expo_record_portfolio[i] = df.loc['row_sum']['Expo']

    # 将组合的VaR、市值、敞口存入数据库
    for i in target_list:
        # print(target_list[i], var_record_portfolio[target_list[i]], mv_record_portfolio[target_list[i]], expo_record_portfolio[target_list[i]])
        query = "insert into VaR_record(date,portfolioID,InstrumentID,productID,VaR_95,Marketvalue,Exposure) values(\'{0}\',\'{1}\',\'{2}\',\'{3}\',{4},{5},{6})".format(date, i, '无', 'portfolio', var_record_portfolio[i], mv_record_portfolio[i], expo_record_portfolio[i])
        dbsa.ExecNonQuery(query)

