"""
处理Excel
"""
import pandas as pd
import sys
sys.path.append(r'D:\CXM\Project_New\Commodity')
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import MSSQL

path = r'C:\Users\ZHAIYUE\Desktop\ddd.xls'

dataset = pd.read_excel(io=path, sheet_name='Sheet1', header=0, index_col=0)

# print(dataset.index)
# print(dataset.columns.values)
dbdc = MSSQL.DB_DataCenter_Commondity()

for i in dataset.columns.values:
    df = dataset[[i]].dropna(axis=0, how='all')
#     print(df)
    for j in range(0, df.shape[0]):
        query = "insert into [Data](Date,ItemID,record) values('{}','{}','{}')".format(df.index[j], str(i), df.iloc[j][i])
        dbdc.ExecNonQuery(query)
    print('写入指标ID为'+str(i)+'记录成功')


