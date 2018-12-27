#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
依照客户优先级生成新的swapneworder
"""

from datetime import datetime
import pandas as pd
import os

today = datetime.today().strftime('%Y%m%d')
# today = '20180815'

# 获取新增可选股票
# path_demand1 = "Z:\\personal\\倪振豪\\OptionTest\\调仓日卖出指令\\"+today+"\\新增可选股票.xlsx"
path_demand1 = r'D:\CXM\Project\Swap\SwapNewOrder\测试用数据\新增可选股票.xlsx'
demand1 = pd.read_excel(io=path_demand1,index_col=0,header=0,usecols="A:C")
demand1.index = [x[0:6] for x in demand1.index]

# 获取新增需求
customerrank = ["锦彤","尚湖稳健","蒙森投资","高频投资"]
path_order = r'D:\CXM\Project\Swap\SwapNewOrder\测试用数据\新增需求'  # +"\\"+today
orderli = []
# orderfile = os.listdir(path_order)
for x in customerrank:
    orderflie = path_order+"\\"+x+"-新增需求-"+today+".xlsx"
    try:
        order = pd.read_excel(io=orderflie,header=0,usecols="A:D",converters={'code': str})
        order.set_index('code',inplace=True)
        # order.reset_index('code',inplace=True)
    except FileNotFoundError as e:
        print("今日"+x+"没有新增需求")
    else:
        for y in order.index:
            if order.loc[y]['volume']<0:
                pass
            else:
                if demand1.loc[y]['股票数量']>0:
                    res = demand1.loc[y]['股票数量'] - order.loc[y]['volume']
                    if res >= 0:
                        demand1.loc[y]['股票数量'] == res
                    else:
                        order.loc[y]['volume'] = demand1.loc[y]['股票数量']
        orderli.append(order)

neworder = pd.concat(orderli, axis=0)

path_neworder = r'D:\CXM\Project\Swap\SwapNewOrder\测试用数据\swap_new_order-20180828_test.xlsx'

neworder.to_excel(path_neworder,index=True)