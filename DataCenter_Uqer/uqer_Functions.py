#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
优矿函数测试
"""

from uqer import DataAPI,Client
login = Client(token='07b082b1f42b91987660f0c2c19097bc3b10fa4b12f6af3274f82df930185f04')

'''

 沪深股票

'''

#股票基本信息
# df = DataAPI.EquGet(secID=u"",ticker=u"",equTypeCD=u"A",listStatusCD=u"",field=u"",pandas="1")

# 公司基本信息
# df = DataAPI.PartyIDGet(partyID="",partyName=u"平安",field=u"",pandas="1")

# 证券编码及基本上市信息

# 证券板块成分
# df = DataAPI.SecTypeRelGet()

# 沪港通合资格股票名单
# df = DataAPI.EquSHHKConsGet(intoDate = '20180813')



# 行业分类标准
# df = DataAPI.IndustryGet(industryVersion=u"SW")


# 激励授予特别条件
# df = DataAPI.EquSpecCondGet(ticker='002210',beginDate='20180101')

# 股票行业分类
# df = DataAPI.EquIndustryGet(intoDate='20180813')


# 上市公司员工
# df = DataAPI.EquShareEmployeesGet(ticker='000001')

# 上市公司管理层
# df = DataAPI.EquManagersGet(ticker=u"000001")

# 上市公司管理层人员介绍
# df = DataAPI.EquManagersInfoGet(ticker=u"000001")

# 上市公司高管薪酬
# df = DataAPI.EquExecsHoldingsGet(ticker=u"000001")

# 上市公司委员会成员情况
# df = DataAPI.EquCommitteeGet(ticker=u"000001")

# 董事长与总经理变更表
# df = DataAPI.EquManageChgGet(ticker="000001")

# 上市公司实际控制人
# df = DataAPI.EquActualControllerGet(ticker=u"002262")

# 上市公司兼任情况
# df = DataAPI.EquManagementConcurrentlyGet(ticker=u"000001")

# 合并资产负债表
# df = DataAPI.FdmtBSGet(ticker=u"000001")


# 沪深股票日行情，返回全部股票数据，包括A股和B股
# print(help(uqer.DataAPI.MktEqudGet))
a = DataAPI.MktEqudGet(ticker='000001',tradeDate='20181126',field="openPrice")
# print(a)

# 指数日行情 存在nan值
# a = DataAPI.MktIdxdGet(tradeDate='20180807')

# 沪深证券停复牌
'''
更新时要注意可能会出现重复信息
'''
# a = DataAPI.SecHaltGet(ticker='000001',beginDate='20100101',endDate='20180809')

# 沪深大宗交易
# a = uqer.DataAPI.MktBlockdGet(tradeDate="20180803")

# 港股日行情
# a = DataAPI.MktHKEqudGet(tradeDate='20180808')

# 沪深股票前复权行情
# a = DataAPI.MktEqudAdjGet(tradeDate='20180808')

# 沪深股票前复权因子
# a = DataAPI.MktAdjfGet(ticker="000001")


# 涨跌停板幅度变动
# a = DataAPI.MktLimitGet(tradeDate='20180808')

# 沪深股票今日停复牌
# df = DataAPI.SecTipsGet()

# 个股日资金流向
# df = DataAPI.MktEquFlowGet(tradeDate="20180809")

# 行业日资金流向
# a = DataAPI.MktIndustryFlowGet(tradeDate='20180809')

# 沪深股票后复权因子
# df = DataAPI.MktAdjfAfGet(ticker="000001")

# 股票日资金流向单类明细
# df = DataAPI.MktEquFlowOrderGet(ticker="000001")

# 行业日资金流向
# df = DataAPI.MktIndustryFlowOrderGet(tradeDate='20180809')

# 股票公开交易信息_股票（龙虎榜_股票）
# df = DataAPI.MktRankListStocksGet(tradeDate='20180808')

# 股票公开交易信息_营业部（龙虎榜_营业部）
# df = DataAPI.MktRankListSalesGet(tradeDate=u"20180808")

# a = DataAPI.FutuGet(contractStatus='L')

# 期货日行情,返回全部期货合约行情（主力以持仓量计算）
# print(help(uqer.DataAPI.MktFutdGet))
# a = uqer.DataAPI.MktFutdGet(tradeDate='20180802')
# print(a)

# df = DataAPI.CCXE.FutuVarcfCCXEGet(varUniCode=u"",exchangeCD=u"XDCE",deliMethod=u"",field=u"varUniCode,exchangeCD,deliMethod,contMult",pandas="1")


'''
期权
'''
# 期权基本信息
# df = DataAPI.OptGet(contractStatus='L')



# a = DataAPI.IdxGet()

# # 获取新闻信息
# df = DataAPI.NewsInfoByTimeGet(newsPublishDate='20180807')
# df0 = DataAPI.NewsInfoByTimeGet(newsPublishDate='20180806', beginTime='09:30', endTime='10:00')
# df1 = DataAPI.NewsInfoByTimeGet(newsPublishDate='20180806', beginTime='10:00', endTime='10:30')

# 根据ID获取新闻全文
# a = DataAPI.NewsBodyGet(newsID='47894136')


# uqer.
# ETF
# df = DataAPI.FundGet(etfLof="ETF",listStatusCd="L",field="ticker,radeAbbrName",pandas="1")


# 基金

# df = DataAPI.PfundGet(pfStyleCD=['14,15'],statusCD=u"100",field=u"",pandas="1")
