#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从wind获取当日实时行
"""
from datetime import datetime
from WindPy import w

w.start()

tradebegintime = str(datetime.today().year)+'-'+str(datetime.today().month)+'-'+str(datetime.today().day)+' 09:30:00'
tradeendtime = str(datetime.today().year)+'-'+str(datetime.today().month)+'-'+str(datetime.today().day)+' 11:30:00'

a = w.wsi('000001.sz','amt', beginTime=tradebegintime, endTime=tradeendtime)
# a= w.htocode('000001', "stocka")