# -*- coding: utf-8 -*-
"""
@author 陈祥明

利用pymssql用于连接SQLServer的类
"""


import pymssql
#测试github同步

# 数据库类
class MSSQL(object):
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        self.cur = self.conn.cursor()

    def ExecQuery(self, sql):  # 执行查询语句
        self.cur.execute(sql)
        resList = self.cur.fetchall()
        return resList

    def ExecNonQuery(self, sql):  # 执行非查询语句
        self.cur.execute(sql)
        self.conn.commit()  # 执行结果提交数据库
        return

    def __del__(self):  # 析构函数
        self.conn.close()
        return
#
# class DB_VaR(MSSQL):
#     def __init__(self):
#         MSSQL.__init__(self, host='127.0.0.1', user='sa', pwd='ZAQ!2wsxCDE#', db='VaR')
#



# if __name__ == "__main__":
    # print("test")
    # dbsa = DB_ScenarioAnalysis()
    # sql = "select top 1 * from positioneod"
    # for i in range(1, 1000):
    #     print("==" + str(i) + "==")
    #     rows = dbsa.ExecQuery(sql)
    #     print(len(rows))

