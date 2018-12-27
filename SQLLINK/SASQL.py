#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
利用sqlslchemay用于连接SQLServer的类
"""
from sqlalchemy import create_engine,exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INT, DateTime, DATETIME, TIMESTAMP, FLOAT, BIGINT, VARCHAR, NVARCHAR, DATE, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import pandas as pd

Base = declarative_base()

class DB(object):
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.engine = create_engine('mssql+pymssql://'+self.user+':'+self.pwd+'@'+self.host+'/'+self.db, pool_size=50)
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.engine.connect()
        # self.cur = self.conn.cursor()


    def ExecQuery(self, sql, df=None):
        obj = self.session.execute(sql)#.fetchall()
        if df==1:
            res = pd.DataFrame(columns=obj.keys(),data=obj.fetchall())
            return res
        else:
            return obj.fetchall()

    def ExecNonQuery(self, sql):
        self.session.execute(sql)
        self.session.commit()

    def __del__(self):  # 析构函数
        self.session.close()

class ScenarioAnalysis(DB):
    def __init__(self):
        DB.__init__(self, host='127.0.0.1', user='sa', pwd='ZAQ!2wsxCDE#', db='ScenarioAnalysis')

class DataCenter_Commodity(DB):
    def __init__(self):
        DB.__init__(self, host='127.0.0.1', user='sa', pwd='ZAQ!2wsxCDE#', db='DataCenter_Commodity')


class Nurex(DB):
    def __init__(self):
        DB.__init__(self, host='10.63.6.220', user='intern', pwd='A12345678!', db='Nurex')

class OptionContract(DB):
    def __init__(self):
        DB.__init__(self, host='10.63.6.78', user='sa', pwd='A12345678!', db='OptionContract')

# class Commodity(Base):
#     __tablename__ = "Commodity"
#     Date = Column(DateTime, primary_key=True)
#     CategoryID = Column(VARCHAR(20), primary_key=True)
#     CategoryName = Column(NVARCHAR(50), nullable=False)
#     ProductID = Column(VARCHAR(20), primary_key=True)
#     ProductName = Column(NVARCHAR(50), )
#     ClassID = Column(VARCHAR(10), primary_key=True)
#     ClassName = Column(NVARCHAR(50), nullable=False)
#     ItemID = Column(VARCHAR(20), primary_key=True)
#     ItemName = Column(NVARCHAR(100),nullable=False)
#     Frequency = Column(NVARCHAR(10), nullable=False)
#     Unit = Column(NVARCHAR(20), nullable=False)
#     Data = Column(FLOAT, nullable=True)
#     Source = Column(NVARCHAR(50), nullable=True)
#     UpdateSource = Column(NVARCHAR(50), nullable=True)
#     UpdateTime = Column(DateTime, server_default=func.now())
#     Remark = Column(NVARCHAR(100), nullable=True)
#


class DataCenter_Analysis(DB):
    def __init__(self):
        DB.__init__(self, host='127.0.0.1', user='sa', pwd='20180515', db='DataCenter_Analysis')

# class Future_Multiplier(Base):
#     __tablename__ = "Future_Multiplier"
#     ProductID = Column(VARCHAR(50), primary_key=True)
#     Multiplier = Column(FLOAT, nullable=False)
#     Unit = Column(NVARCHAR(50), nullable=False)
#     ReflashDate = Column(DateTime, nullable=False)
#     RecordDate = Column(DateTime, nullable=False)
#
# class HistData_Future(Base):
#     __tablename__ = "HistData_Future"
#     algoID = Column(INT, nullable=False)
#     productID = Column(VARCHAR(16), primary_key=True)
#     instrumentID = Column(VARCHAR(32), nullable=False)
#     tradingDate = Column(Date, primary_key=True)
#     openPrice = Column(FLOAT, nullable=True)
#     highPrice = Column(FLOAT, nullable=True)
#     lowPrice = Column(FLOAT, nullable=True)
#     closePrice = Column(FLOAT, nullable=True)
#     volume = Column(BIGINT, nullable=True)
#     turnover = Column(BIGINT, nullable=True)
#     openInterestAccumulate = Column(INT, nullable=True)
#     multiplier = Column(FLOAT, nullable=True)
#     updateTime = Column(DATETIME, nullable=True)
#     pricechangepercent = Column(FLOAT, nullable=True)
#
# class HistData_Stock(Base):
#     __tablename__ = "HistData_Stock"
#     Date = Column(Date, primary_key=True)
#     InstrumentID = Column(VARCHAR(50), primary_key=True)
#     openprice = Column(FLOAT, nullable=True)
#     highestprice = Column(FLOAT, nullable=True)
#     lowestprice = Column(FLOAT, nullable=True)
#     closeprice = Column(FLOAT, nullable=True)
#     PriceChangePercent = Column(FLOAT, nullable=True)
#
# class InstrumentInfo_Future(Base):
#     __tablename__ = "InstrumentInfo_Future"
#     ProducuID = Column(VARCHAR(50), primary_key=True)
#     ProducuName = Column(NVARCHAR(50), nullable=False)
#
# class InstrumentInfo_Stock(Base):
#     __tablename__ = "InstrumentInfo_Stock"
#     InstrumentID = Column(VARCHAR(50), primary_key=True)
#     InstrumentName = Column(NVARCHAR(50), nullable=False)
#
# class MarketEod(Base):
#     __tablename__ = "MarketEod"
#     Date = Column(DATE, primary_key=True)
#     InstrumentID = Column(VARCHAR(20), nullable=False)
#     PrevClosePrice = Column(FLOAT, nullable=True)
#     PrevSettlementPrice = Column(FLOAT, nullable=True)
#     ClosePrice = Column(FLOAT, nullable=True)
#     SettlementPrice = Column(FLOAT, nullable=True)
#
# class PositionEod(Base):
#     __tablename__ = "PositionEod"
#     Date = Column(DATE, primary_key=True)
#     AccountID = Column(VARCHAR(50), primary_key=True)
#     InstrumentID = Column(VARCHAR(50), primary_key=True)
#     Totalposition = Column(INT, primary_key=True)
#     portfolio = Column(VARCHAR(50), nullable=True)
#     direction = Column(VARCHAR(50), primary_key=True)
#     portfolioID = Column(VARCHAR(50), primary_key=True)
#     product = Column(VARCHAR(50), nullable=True)
#
# class SectorInfo_Stock(Base):
#     __tablename__ = "SectorInfo_Stock"
#     SectorID = Column(VARCHAR(20), primary_key=True)
#     SectorName = Column(NVARCHAR(50), primary_key=True)
#     InstrumentID = Column(VARCHAR(20), primary_key=True)
#     InstrumentName = Column(NVARCHAR(50) ,nullable=True)
#
# class VaR_Record(Base):
#     __tablename__ = "VaR_Record"
#     date = Column(DATE, primary_key=True)
#     portfolioID = Column(VARCHAR(50), primary_key=True)
#     InstrumentID = Column(VARCHAR(50), primary_key=True)
#     productID = Column(VARCHAR(50), primary_key=True)
#     VaR_95 = Column(FLOAT, nullable=True)
#     MarketValue = Column(FLOAT, nullable=True)
#     Exposure = Column(FLOAT, nullable=True)


class DB_DataCenter_Uqer(DB):
    def __init__(self):
        DB.__init__(self, host='127.0.0.1', user='sa', pwd='ZAQ!2wsxCDE#', db='DataCenter_Uqer')

# if __name__ == "__main__":
#     a = DataCenter_Analysis().session.query(HistData_Stock).filter(HistData_Stock.InstrumentID=='000001').all()
#     print(a)
#     print(type(a[0].Date))
    # print(type(a[0].RecordDate))

if __name__ == "__main__":
    dbsa = ScenarioAnalysis()
    print(dbsa.conn)
    query = "SELECT  TOP 1000 *  FROM [DataCenter_Analysis].[dbo].[HistData_Future]"
    df = dbsa.ExecQuery(query)
    print(df)