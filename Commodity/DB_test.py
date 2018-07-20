# -*- coding: utf-8 -*-
"""
@author: 陈祥明
对Commondity数据库进行操作
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, DATE, DATETIME
from sqlalchemy.orm import sessionmaker



# # 初始化数据库连接
# engine = create_engine('mssql+pymssql://sa:20180515@127.0.0.1:1433/Data_Analysis', pool_size=100)
#
# # 创建对象的基类
# Base = declarative_base()
#
# # 创建会话类
# DBSession = sessionmaker(bind=engine)
#
# # 定义表对象
# class Future_Multiplier(Base):
#     # 表名
#     __tablename__ = 'Future_Multiplier'
#     # 表结构
#     ProductID = Column(String(50), primary_key=True)
#     Multiplier = Column(Float, nullable=False)
#     Unit = Column(String(50), nullable=False)
#     ReflashDate = Column(DateTime, nullable=False)
#     RecordDate = Column(DateTime, primary_key=True)
#
# def query():
#     session = DBSession()
#     aa = session.query(Future_Multiplier).filter(Future_Multiplier.ProductID == 'A', Future_Multiplier.RecordDate == '2018-07-16').all()
#     print(aa[0].ProductID)
#     session.close




class DB(object):
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.engine = create_engine('mssql+pymssql://'+self.user+':'+self.pwd+'@'+self.host+'/'+self.db, echo=True)
        self.base = declarative_base()
        self.session = sessionmaker(bind=self.engine)

    def ExecQuery(self, sql):
        conn = self.session()
        res = conn.execute(sql)
        conn.close()
        return res

    def ExecNonQuery(self, sql):
        conn = self.session()
        conn.execute(sql)
        conn.commit()

    # def Query(self, sql):
    #     with self.engine.connect() as conn:
    #         trans = conn.begin()
    #         try:
    #             re = conn.execute(sql)
    #             return re
    #         except:
    #             trans.rollback()
    #             raise


class Data_Analysis(DB):
    def __init__(self):
        DB.__init__(self, host='127.0.0.1', user='sa', pwd='20180515', db='DataCenter_Commondity')



# class Future

# if __name__ == '__main__':
#     da = Data_Analysis()
#     query = "insert into Future_Multiplier(ProductID, Multiplier, Unit, ReflashDate, RecordDate) values('{}',{},'{}','{}','{}')".format('A', 10, '111', '20180717', '20180717')
#     a = da.ExecNonQuery(query)
#     print('a:', a)
#     query = "select * from Future_Multiplier where RecordDate='{}'".format('20180717')
#     b = da.ExecQuery(query)
#     print('B:', b)
#     # for i in range(0, 1000):
#     #
#     #     print('访问数据库第'+str(i)+'次')
