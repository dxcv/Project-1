#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CXM

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re



chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
driver = webdriver.Chrome(chrome_options=chrome_options) # 打开浏览器
driver.get("http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/2927369/index.html") #用webdriver打开人行政策货币司
source = driver.page_source#.replace('\n','').replace('\n','').replace(' ','') #获取网页源代码 str
driver.close()  #回收资源
# print(source)


#获取正文标题
pat_title_article = '<h2 style="font-size: 16px;color: #333;">(.*?)</h2>'#.replace(' ','')
title_article = re.compile(pat_title_article).findall(source)

########正文内容#######

# 匹配日期
pat_date = '<span id="shijian">(.*?)</span>'#.replace(' ','')
date = re.compile(pat_date).findall(source)[0][:10]

#查找通知正文部分
pat_content = '<p>(.*?)</p>'
content = re.compile(pat_content).findall(source)
if content == [] or content[0]=='':
    pat_content = '<p align="left">(.*?)</p>'#.replace(' ','')
    content = re.compile(pat_content).findall(source)
    detail = content[0]
else:
    detail = content[0]

#查找页面中的表格
pat_table = '<table align="center" border="1" cellpadding="0" cellspacing="0" style="border-bottom: windowtext 1px solid; border-left: windowtext 1px solid; width: 526px; border-top: windowtext 1px solid; border-right: windowtext 1px solid" width="526">([\s\S]*?)<tbody>([\s\S]*?)</tbody>([\s\S]*?)</table>'
table = re.compile(pat_table).findall(source)
table_alt_1 = []
table_alt_2 = []
table_alt_3 = []
table_alt_4 = []
if table == []:#添加特例
    pat_table_alt_1 = '<table align="center" border="1" cellpadding="0" cellspacing="0" style="border-right: windowtext 1px solid; border-top: windowtext 1px solid; border-left: windowtext 1px solid; width: 526px; border-bottom: windowtext 1px solid" width="526">([\s\S]*?)<tbody>([\s\S]*?)</tbody>([\s\S]*?)</table>'#.replace(' ','')
    table_alt_1 = re.compile(pat_table_alt_1).findall(source)
    if table_alt_1 == []:
        pat_table_alt_2 = '<table align="center" border="1" cellpadding="0" cellspacing="0" style="border: 1px solid windowtext; width: 526px; margin:0 auto;" width="526">([\s\S]*?)<tbody>([\s\S]*?)</tbody>([\s\S]*?)</table>'
        table_alt_2 = re.compile(pat_table_alt_2).findall(source)
        if table_alt_2 == []:
            pat_table_alt_3 = '<table align="center" border="1" cellpadding="0" cellspacing="0" style="border: 1px solid windowtext; width: 526px;" width="526">([\s\S]*?)<tbody>([\s\S]*?)</tbody>([\s\S]*?)</table>'
            table_alt_3 = re.compile(pat_table_alt_3).findall(source)
            if table_alt_3 == []:
                pat_table_alt_4 = '<table align="center" border="1" cellpadding="0" cellspacing="0" style="border: 1px solid windowtext; width: 526px;" width="526">([\s\S]*?)<tbody>([\s\S]*?)</tbody>([\s\S]*?)</table>'
                table_alt_4 = re.compile(pat_table_alt_4).findall(source)
            else:
                pass
        else:
            pass
    else:
        pass
else:
    pass

detail_table_content = []
if table == []: #通知中没有表格不做进一步的解析
    pass
else:

    for t in table:
        #列标题
        pat_title_table_column ='<span style="font-size: medium;"><span style="color: rgb(34, 34, 34);"><span style="font-family: 宋体;">(.*?)</span>'#.replace(' ','')
        title_table_column = re.compile(pat_title_table_column).findall(t[1])
        ###表格内容
        #带汉字
        pat_table_content1 = '<span style="font-size: medium;"><span style="color: rgb(34, 34, 34);"><span style="font-family: arial, sans-serif;">(.*?)</span></span></span><span style="color: rgb(34, 34, 34);"><span style="font-family: 宋体;">(.*?)</span>'#.replace(' ','')
        table_content1 = re.compile(pat_table_content1).findall(t[1])
        #不带汉字
        pat_table_content2 = '<span style="color: rgb(34, 34, 34);"><span style="font-family: arial, sans-serif;"><span style="font-size: medium;">(.*?)</span>'#.replace(' ','')
        table_content2 = re.compile(pat_table_content2).findall(t[1])
        row = len(table_content2)
        if row == 0:
            # 列标题
            pat_title_table_column = '<span style="font-size: 12px"><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span>'  # .replace(' ','')
            title_table_column = re.compile(pat_title_table_column).findall(t[1])
            ###表格内容
            # 带汉字
            pat_table_content1 = '<span style="font-size: 12px"><span style="color: #222222"><span style="font-family: arial, sans-serif">(.*?)</span><span style="font-family: 宋体">(.*?)</span></span></span>'  # .replace(' ','')
            table_content1 = re.compile(pat_table_content1).findall(t[1])
            # 不带汉字
            pat_table_content2 = '<span style="font-size: 12px"><span style="color: #222222"><span style="font-family: arial, sans-serif">(.*?)</span></span></span>'  # .replace(' ','')
            table_content2 = re.compile(pat_table_content2).findall(t[1])
            row = int(len(table_content1)/2)
            if row == 0:
                for t in table:
                    # 列标题
                    # 默认括号里的内容为group，要匹配括号里的文字要对括号转义
                    pat_title_table_column = '<span style="color: #222222"><span style="font-family: 宋体">(.*?)</span></span>'  # .replace(' ','')
                    title_table_column = re.compile(pat_title_table_column).findall(t[1])
                    ###表格内容
                    # 带汉字
                    pat_table_content1 = '<span style="color: #222222"><span style="font-family: arial, sans-serif">(.*?)</span></span><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span>'  # .replace(' ','')
                    table_content1 = re.compile(pat_table_content1).findall(t[1])
                    # 不带汉字
                    pat_table_content2 = '<span style="color: #222222"><span style="font-family: arial, sans-serif">(.*?)</span>'  # .replace(' ','')
                    table_content2 = re.compile(pat_table_content2).findall(t[1])
                    row = int(len(table_content1)/2)
                    for i in range(0, row):
                        if title_table_column[2] == '中标利率':
                            detail_table_content.insert(len(detail_table_content),
                                                        '逆回购操作情况:' + title_table_column[0] + '为' + ''.join(
                                                            table_content1[i * 2]) + "," + title_table_column[
                                                            1] + '为' + ''.join(
                                                            table_content1[i * 2 + 1]) + "," +
                                                        title_table_column[2] + '为' + table_content2[i])
                        elif title_table_column[2] == '操作利率':
                            detail_table_content.insert(len(detail_table_content),
                                                        'MLF操作情况:' + title_table_column[0] + '为' + ''.join(
                                                            table_content1[i * 2]) + "," + title_table_column[
                                                            1] + '为' + ''.join(
                                                            table_content1[i * 2 + 1]) + "," +
                                                        title_table_column[2] + '为' + table_content2[i])
                        else:
                            detail_table_content.insert(len(detail_table_content), date + "当日情况存在异常")
            for i in range(0,row):
                if title_table_column[2]=='中标利率':
                    detail_table_content.insert(len(detail_table_content),'逆回购操作情况:' + title_table_column[0]+'为'+''.join(table_content1[i*2])+","+title_table_column[1]+'为'+''.join(table_content1[i*2+1]) + "," + title_table_column[2]+'为'+table_content2[2])
                elif title_table_column[2]=='操作利率':
                    detail_table_content.insert(len(detail_table_content),'MLF操作情况:' + title_table_column[0]+'为'+''.join(table_content1[i*2])+","+title_table_column[1]+'为'+''.join(table_content1[i*2+1]) + "," + title_table_column[2]+'为'+table_content2[2])
                else:
                    detail_table_content.insert(len(detail_table_content),date+"当日情况存在异常")
        else:
            for i in range(0,row):
                if title_table_column[2]=='中标利率':
                    detail_table_content.insert(len(detail_table_content),'逆回购操作情况:' + title_table_column[0]+'为'+''.join(table_content1[i*2])+","+title_table_column[1]+'为'+''.join(table_content1[i*2+1]) + "," + title_table_column[2]+'为'+table_content2[i])
                elif title_table_column[2]=='操作利率':
                    detail_table_content.insert(len(detail_table_content),'MLF操作情况:' + title_table_column[0]+'为'+''.join(table_content1[i*2])+","+title_table_column[1]+'为'+''.join(table_content1[i*2+1]) + "," + title_table_column[2]+'为'+table_content2[i])
                else:
                    detail_table_content.insert(len(detail_table_content),date+"当日情况存在异常")

if table_alt_1 == []: #通知中没有特例表格-1-不做进一步的解析
    pass
else:

    for t in table_alt_1:
        #列标题
        pat_title_table_column ='<span style="font-size: medium"><span style="font-family: 宋体"><span style="color: #222222">(.*?)</span></span></span>'#.replace(' ','')
        title_table_column = re.compile(pat_title_table_column).findall(t[1])
        ###表格内容
        #带汉字
        pat_table_content1 = '<span style="color: #222222">(.*?)</span></span></span><span style="font-family: 宋体"><span style="color: #222222">(.*?)</span>'#.replace(' ','')
        table_content1 = re.compile(pat_table_content1).findall(t[1])
        #不带汉字
        pat_table_content2 = '<span style="font-family: arial,sans-serif"><span style="color: #222222"><span style="font-size: medium">(.*?)</span>'#.replace(' ','')
        table_content2 = re.compile(pat_table_content2).findall(t[1])
        row = len(table_content2)
        for i in range(0,row):
            if title_table_column[2]=='中标利率':
                detail_table_content.insert(len(detail_table_content),'逆回购操作情况:' + title_table_column[0]+'为'+''.join(table_content1[i*2])+","+title_table_column[1]+'为'+''.join(table_content1[i*2+1]) + "," + title_table_column[2]+'为'+table_content2[i])
            elif title_table_column[2]=='操作利率':
                detail_table_content.insert(len(detail_table_content),'MLF操作情况:' + title_table_column[0]+'为'+''.join(table_content1[i*2])+","+title_table_column[1]+'为'+''.join(table_content1[i*2+1]) + "," + title_table_column[2]+'为'+table_content2[i])
            else:
                detail_table_content.insert(len(detail_table_content),date+"当日情况存在异常")



if table_alt_2 == [] and table_alt_3==[]:  # 通知中没有特例表格-2-(2017年1月（含）前)不做进一步的解析
    pass
else:
    for t in table_alt_2 or table_alt_3:
        # 列标题
        pat_title_table_column = '<td style="border: 1px solid windowtext; width: 175px; height: 21px;"><p align="center"><span style="font-size: medium;"><span style="color: rgb\(34, 34, 34\);"><span style="font-family: 宋体;">(.*?)</span></span></span></p> </td>'  # .replace(' ','')
        title_table_column = re.compile(pat_title_table_column).findall(t[1])
        ###表格内容
        # 带汉字
        pat_table_content1 = '<span style="font-size: medium;"><span style="color: rgb\(34, 34, 34\);"><span style="font-family: arial, sans-serif;">(.*?)</span></span></span><span style="color: rgb\(34, 34, 34\);"><span style="font-family: 宋体;">(.*?)</span></span>'  # .replace(' ','')
        table_content1 = re.compile(pat_table_content1).findall(t[1])
        # 不带汉字
        pat_table_content2 = '<span style="color: rgb\(34, 34, 34\);"><span style="font-family: arial, sans-serif;"><span style="font-size: medium;">(.*?)</span></span></span>'  # .replace(' ','')
        table_content2 = re.compile(pat_table_content2).findall(t[1])
        row = int(len(table_content2)/2)
        if row == 0:
            pat_title_table_column = '<span style="font-size: medium;"><span style="font-family: 宋体;"><span style="color: rgb\(34, 34, 34\);">(.*?)</span>'  # .replace(' ','')
            title_table_column = re.compile(pat_title_table_column).findall(t[1])
            ###表格内容
            # 带汉字
            pat_table_content1 = '<span style="font-family: arial,sans-serif;"><span style="color: rgb\(34, 34, 34\);"><span style="font-size: medium;">(.*?)</span></span></span><span style="font-size: medium;"><span style="font-family: 宋体;"><span style="color: rgb\(34, 34, 34\);">(.*?)</span>'  # .replace(' ','')
            table_content1 = re.compile(pat_table_content1).findall(t[1])
            # 不带汉字
            pat_table_content2 = '<span style="font-family: arial,sans-serif;"><span style="color: rgb/(34, 34, 34/);"><span style="font-size: medium;">(.*?)</span>'  # .replace(' ','')
            table_content2 = re.compile(pat_table_content2).findall(t[1])
            row = int(len(table_content2) / 2)
            for i in range(0, row):
                if title_table_column[2] == '中标利率':
                    detail_table_content.insert(len(detail_table_content),'逆回购操作情况:' + title_table_column[0] + '为' + ''.join(table_content1[i * 2]) + "," + title_table_column[1] + '为' + ''.join(table_content1[i * 2 + 1]) + "," +title_table_column[2] + '为' + table_content2[i])
                elif title_table_column[2] == '操作利率':
                    detail_table_content.insert(len(detail_table_content),'MLF操作情况:' + title_table_column[0] + '为' + ''.join(table_content1[i * 2]) + "," + title_table_column[1] + '为' + ''.join(table_content1[i * 2 + 1]) + "," + title_table_column[2] + '为' + table_content2[i])
                else:
                    detail_table_content.insert(len(detail_table_content), date + "当日情况存在异常")
        else:
            for i in range(0, row):
                if title_table_column[2] == '中标利率':
                    detail_table_content.insert(len(detail_table_content),'逆回购操作情况:' + title_table_column[0] + '为' + ''.join(table_content1[i * 2]) + "," + title_table_column[1] + '为' + ''.join(table_content1[i * 2 + 1]) + "," +title_table_column[2] + '为' + table_content2[i])
                elif title_table_column[2] == '操作利率':
                    detail_table_content.insert(len(detail_table_content),'MLF操作情况:' + title_table_column[0] + '为' + ''.join(table_content1[i * 2]) + "," + title_table_column[1] + '为' + ''.join(table_content1[i * 2 + 1]) + "," + title_table_column[2] + '为' + table_content2[i])
                else:
                    detail_table_content.insert(len(detail_table_content), date + "当日情况存在异常")

if table_alt_4 == []:
    pass
else:
    for t in table_alt_4:
        pat_title_table_column = '<span style="font-size: medium;"><span style="color: rgb(34, 34, 34);"><span style="font-family: 宋体;">(.*?)</span>'  # .replace(' ','')
        title_table_column = re.compile(pat_title_table_column).findall(t[1])
        ###表格内容
        # 带汉字
        pat_table_content1 = '<span style="font-size: medium;"><span style="color: rgb\(34, 34, 34\);"><span style="font-family: arial, sans-serif;">(.*?)</span></span></span><span style="color: rgb\(34, 34, 34\);"><span style="font-family: 宋体;">(.*?)</span>'  # .replace(' ','')
        table_content1 = re.compile(pat_table_content1).findall(t[1])
        # 不带汉字
        pat_table_content2 = '<span style="color: rgb\(34, 34, 34\);"><span style="font-family: arial, sans-serif;"><span style="font-size: medium;">(.*?)</span>'  # .replace(' ','')
        table_content2 = re.compile(pat_table_content2).findall(t[1])
        row = (len(table_content1)/2)
        for i in range(0, row):
            if title_table_column[2] == '中标利率':
                detail_table_content.insert(len(detail_table_content),
                                            '逆回购操作情况:' + title_table_column[0] + '为' + ''.join(
                                                table_content1[i * 2]) + "," + title_table_column[
                                                1] + '为' + ''.join(
                                                table_content1[i * 2 + 1]) + "," +
                                            title_table_column[2] + '为' + table_content2[i])
            elif title_table_column[2] == '操作利率':
                detail_table_content.insert(len(detail_table_content),
                                            'MLF操作情况:' + title_table_column[0] + '为' + ''.join(
                                                table_content1[i * 2]) + "," + title_table_column[
                                                1] + '为' + ''.join(
                                                table_content1[i * 2 + 1]) + "," +
                                            title_table_column[2] + '为' + table_content2[i])

a = date,title_article[0],detail+';'.join(detail_table_content)
print(date,title_article[0],detail+';'.join(detail_table_content))