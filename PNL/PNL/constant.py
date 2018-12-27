#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
项目中的常量
"""
from datetime import datetime,timedelta

today = datetime.today()
yestoday = (datetime.today()+timedelta(-1))

path_PNL = r'Z:\RiskM\损益\P&L_py_test.xlsx'

path_trading = r'Z:\产品相关\产品方案\场外期权\落地项目\交易汇总.xlsx'
