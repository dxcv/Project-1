# -*- coding: utf-8 -*-
"""
Created on Fri Jun 08 13:12:54 2018

@author: 陈祥明
"""

from sqlalchemy import *
from sqlalchemy.orm import *
engine = create_engine('mssql+pymssql://sa:20180515@127.0.0.1/Data', echo=True)

#绑定元信息
metadata = MetaData(engine)

#创建表格，初始化数据库
user = Table('user', metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String(50)))
address = Table('address', metadata, 
    Column('id', Integer, primary_key = True),
    Column('user_id', None, ForeignKey('user.id')), 
    Column('email', String(50), nullable = False),
)
#创建数据表，如果数据表存在则忽视
metadata.create_all(engine)
#获取数据库链接，以备后面使用
conn = engine.connect()