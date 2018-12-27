#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
连接postgresql数据库的类
"""
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INT, DateTime, DATETIME, TIMESTAMP, FLOAT, BIGINT, VARCHAR, NVARCHAR, DATE, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

class PostgreDB(object):
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.engine = create_engine("postgresql+psycopg2://{}:{}@{}/{}".format(self.user,self.pwd,self.host,self.db), pool_size=100)
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.engine.connect()

    # 执行原生sql
    def ExecQuery(self, sql, df=None): # 默认返回ResultProxy对象
        obj = self.session.execute(sql)
        if df == 1:
            res = pd.DataFrame(columns=obj.keys(),data=obj.fetchall())
            return res
        else:
            return obj

    def ExecNonQuery(self, sql):
        self.session.execute(sql)
        self.session.commit()

    def __del__(self):  # 析构函数
        self.session.close()

class Alpha(PostgreDB):
    def __init__(self):
        PostgreDB.__init__(self, host='10.63.6.220:5432', user='tourist', pwd='A12345678!', db='alpha')



if __name__ == "__main__":
    dbal = Alpha()
    print(dbal.conn)
    query = "select top 1000 (*) from index_market order by trade_date desc"
    df = dbal.ExecQuery(query)
    print(df)