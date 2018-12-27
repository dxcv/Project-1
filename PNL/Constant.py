#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
常量
"""
from datetime import datetime,timedelta

today = datetime.today().strftime('%Y%m%d')

yestoday = (datetime.today()+timedelta(-1)).strftime('%Y%m%d')