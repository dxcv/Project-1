#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
QuantLib中对日期的操作
"""
from QuantLib import *

chn_calendar = China()

begindate = Date(16,8,2018)

raw_date = begindate +Period(60,Days)

chn_date = chn_calendar.advance(begindate,Period(60,Days))

print(raw_date)
print(chn_date)
