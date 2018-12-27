# -*- coding: utf-8 -*-
"""
Created on Mon Jul 09 10:00:03 2018

@author: 陈祥明
"""
import time


#常用变量
date = time.strftime('%Y%m%d', time.localtime())

portfolioID_list = ['ALL', 'alpha_prop', 'alpha_300', 'alpha_500', 'indexarb', 'indexarb2', 'macro', 'cta', 'stock']

targetID_list = ['ALL', 'alpha_prop', 'alpha_300', 'alpha_500', 'indexarb+indexarb2', 'macro', 'cta', 'stock']

accountlist = ['77772', '77773', '77774', '77775', '77776', '77777', '77778', '77779']

path_position = u'D:\\CXM\\报表\\仓位\\Position.xlsx'

path_var = u'D:\\CXM\\报表\\VaR\\VaR.xlsx'

path_list1 = [u'D:\\CXM\\报表\\VaR\\', date, u'VaR日报表.xlsx']

path_list2 = [u'Z:\\personal\\倪振豪\\VaR日报\\', date, u'VaR日报表.xlsx']

path_list = [u'D:\\CXM\\报表\\仓位\\', date, u'仓位日报表.xlsx']

path_var_save1 = ''.join(path_list1)

path_var_save2 = ''.join(path_list2)

path_position_save = ''.join(path_list)

token = '07b082b1f42b91987660f0c2c19097bc3b10fa4b12f6af3274f82df930185f04'