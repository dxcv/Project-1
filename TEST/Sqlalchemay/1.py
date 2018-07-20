"""
用于学习sqlalchemay的第一个文件
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date,
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接
engine = create_engine('mssql+pymssql://sa:20180515@127.0.0.1:1433/Data_Analysis', echo=True)

# 创建对象的基类
Base = declarative_base()

# 创建会话类
DBSession = sessionmaker(bind=engine)

# 定义表对象
class Future_Multiplier(Base):
    # 表名
    __tablename__ = 'Future_Multiplier'
    # 表结构
    ID = Column(String(20), primary_key=True)
    Name = Column(String(50), nullable=False)





