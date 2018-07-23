#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用递归和map查询全部子portfolio
"""
import sys
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import MSSQL

dbsa = MSSQL.DB_ScenarioAnalysis()

query  = "select * from MarketEod where Date = '20180720'"