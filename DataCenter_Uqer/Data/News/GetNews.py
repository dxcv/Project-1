#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
分时段获取新闻
"""
import email.mime.multipart
import email.mime.text
import smtplib
import pandas as pd

import uqer
from uqer import DataAPI
from datetime import datetime,timedelta
import pandas as pd
import sys
sys.path.append(r'D:\CXM\Project_New\DataCenter_Uqer')
import Constant
sys.path.append(r'D:\CXM\Project_New\SQLLINK')
import MSSQL


# 获取过去半小时的时间段
def getstarttime(x=30):
    bt = datetime.today() + timedelta(minutes=-x)
    return bt.strftime("%H:%M")


date = Constant.today
bt = getstarttime()
et = datetime.today().strftime("%H:%M")

uqer.Client(token=Constant.token)

df = DataAPI.NewsInfoByTimeGet(newsPublishDate=date, beginTime=bt, endTime=et)

df.fillna('无')
df['NewsURL'] = 0
dbuq = MSSQL.DB_DataCenter_Uqer()


for x in range(0, df.shape[0]):
    a = DataAPI.NewsBodyGet(newsID=str(df.iloc[x][0]))
    df.loc[df['newsID'] == df.iloc[x][0], 'NewsURL'] = a.iloc[0][2]

pd.set_option('display.max_colwidth', -1)

# 将df写入数据库
msg = email.mime.multipart.MIMEMultipart()
msg['from'] = "1872917132@qq.com"
msg['to'] = 'chen_xiangming@outlook.com'
msg['subject'] = date+' '+bt+'-'+et+'分时段新闻'

content = df[['newsTitle', 'newsSummary', 'NewsURL']].to_html(index=False)

txt = email.mime.text.MIMEText(content, 'html', 'utf-8')
msg.attach(txt)
server = smtplib.SMTP('smtp.qq.com', 587) #
# server.set_debuglevel(1)

server.ehlo()
server.starttls()


server.login('1872917132@qq.com', 'jiopspedmxzhddcf')
server.sendmail('1872917132@qq.com', 'chen_xiangming@outlook.com', msg.as_string())
server.quit()

pd.set_option('display.max_colwidth', 15)

# # 将df写入数据库
# for i in range(0, df.shape[0]):
#     query = "insert into News_Info(NewsID,Title,Summary,OriginSource,Author,PublishSite,PublishTime,InsertTime,NewsURL) values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(df.iloc[i][0],df.iloc[i][1],df.iloc[i][2],df.iloc[i][3],df.iloc[i][4],df.iloc[i][5],df.iloc[i][6],df.iloc[i][7],df.iloc[i][8])
#     dbuq.ExecNonQuery(query)
#     print("写入新闻ID为"+str(df.iloc[i][0])+"的记录成功")