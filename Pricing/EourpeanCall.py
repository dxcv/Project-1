#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
欧式期权定价
"""

from QuantLib import *

today = Date(15,8,2018)
Settings_instance().evaluationDate = today

option = EuropeanOption(PlainVanillaPayoff(Option.Call,100), EuropeanExercise(Date(31,12,2018)))

'''设定一些参数'''
u = SimpleQuote(100.0)
r = SimpleQuote(0.01)
vol = SimpleQuote(0.20)

riskFreeCurve = FlatForward(0,TARGET(),QuoteHandle(r),Actual360())
volatility = BlackConstantVol(0,TARGET(), QuoteHandle(vol),Actual360())

porcess = BlackScholesProcess(QuoteHandle(u),riskFreeTS=YieldTermStructureHandle(riskFreeCurve),volTS=BlackVolTermStructureHandle(volatility))

engine = AnalyticEuropeanEngine(porcess)

option.setPricingEngine(engine)
print(option.NPV())
print(option.delta())
print(option.gamma())
print(option.vega())
print(option.theta())

