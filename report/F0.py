#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
证券公司参与股指期货、国债期货交易专项监管报表--自营业务
"""
from datetime import datetime,timedelta
import pandas as pd
import sys
sys.path.append(r'D:\CXM\Project\SQLLINK')

lastmonth = (datetime.today()+timedelta(-60)).strftime('%Y%m')
month = (datetime.today()+timedelta(-30)).strftime('%Y%m')
# month = datetime.date.today().strftime('%Y%m')
df = pd.read_excel('F0上海团队201809月.xlsx',usecols="B:P",skiprows="1",skipfooter='11')
