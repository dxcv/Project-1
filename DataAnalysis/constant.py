"""
常量
"""
import pymssql

path_group = r'D:\CXM\Project_New\DataAnalysis\Data\groupby_test.csv'

conn = pymssql.connect(host='127.0.0.1', user='sa', password='20180515', database='DataCenter_Analysis', charset='utf8')