#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成热力图
"""

import seaborn as sns
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import openpyxl


path = 'D:\CXM\Paper\利率市场化\图表\图数据_相关系数.xlsx'

wb = openpyxl.load_workbook(path)
sheet_names = wb.sheetnames
wb.close()


for name in sheet_names:
    df = pd.read_excel(io=path,sheet_name=name,header=0,index_col=0)

    cor = df.corr()
    # ax = cor.plot()
    # fig = ax.get_figure()

    plt.figure(figsize=(cor.shape[1]+3, cor.shape[1]-2))
    sns.heatmap(data=cor,vmax=1,vmin=0,annot=True,cbar=False)
    plt.yticks(rotation=360)
    plt.savefig('D:\CXM\Paper\利率市场化\图表'+'\\'+name+'.png')