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
driver.get("http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/3461874/index.html") #用webdriver打开人行政策货币司
source = driver.page_source#.replace('\n','').replace('\n','').replace(' ','') #获取网页源代码 str
driver.close()  #回收资源
# print(source)


#获取正文标题
pat_title_article = '<h2 style="font-size: 16px;color: #333;">(.*?)</h2>'
title_article = re.compile(pat_title_article).findall(source)

########正文内容#######

# 匹配日期
pat_date = '<span id="shijian">(.*?)</span>'
date = re.compile(pat_date).findall(source)[0][:10]

#查找通知正文部分
pat_content = '<p align="left">(.*?)</p>'
content = re.compile(pat_content).findall(source)
if content == []:
    pat_content = '<p>(.*?)</p>'
    content = re.compile(pat_content).findall(source)
    detail = content[0]
else:
    detail = content[0]

#查找页面中的表格
pat_table = '<table align="center" border="1" cellpadding="0" cellspacing="0" style="border-bottom: windowtext 1px solid; border-left: windowtext 1px solid; width: 526px; border-top: windowtext 1px solid; border-right: windowtext 1px solid" width="526">([\s\S]*?)<tbody>([\s\S]*?)</tbody>([\s\S]*?)</table>'#.replace(' ','')
table = re.compile(pat_table).findall(source)

if table == []: #通知中没有表格不做进一步的解析
    pass
else:
    detail_table_content = []
    for t in table:
        #列标题
        pat_title_table_column = '<span style="font-size: medium"><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span>'
        title_table_column = re.compile(pat_title_table_column).findall(t[1])
        ###表格内容
        #带汉字
        pat_table_content1 = '<span style="font-family: arial, sans-serif">(.*?)</span></span></span><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span>'
        table_content1 = re.compile(pat_table_content1).findall(t[1])
        #不带汉字
        pat_table_content2 = '<span style="font-family: arial, sans-serif"><span style="font-size: medium">(.*?)</span>'
        table_content2 = re.compile(pat_table_content2).findall(t[1])
        row = len(table_content2)
        for i in range(0,row):
            if title_table_column[1]=='中标量':
                detail_table_content.insert(len(detail_table_content),'逆回购操作情况:' + title_table_column[0]+'为'+''.join(table_content1[i*2])+","+title_table_column[1]+'为'+''.join(table_content1[i*2+1]) + "," + title_table_column[2]+'为'+table_content2[i])
            elif title_table_column[1]=='操作量':
                detail_table_content.insert(len(detail_table_content),'MLF操作情况:' + title_table_column[0]+'为'+''.join(table_content1[i*2])+","+title_table_column[1]+'为'+''.join(table_content1[i*2+1]) + "," + title_table_column[2]+'为'+table_content2[i])
            else:
                detail_table_content.insert(len(detail_table_content),date+"当日情况存在异常")

for x in detail_table_content:
    print(x)





if table == []:
    pat_content = '<p align="left">(.*?)</p>'.replace(' ', '')
    content = re.compile(pat_content).findall(source)
    if content == []:
        pat_content = '<p>(.*?)</p>'
        content = re.compile(pat_content).findall(source)
        detail = content[0]
    else:
        detail = content[0]


pat_title_column = '<span style="font-size: medium"><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span>'.replace(' ','')
title_column = re.compile(pat_title_column).findall(source)

if title_column == []: #网页中没有表格不进行进一步的解析，没有表格的通告中p标签的有靠左的属性
    pass
else:
    #文字部分，带表格
    pat_content = '<p>(.*?)</p>'
    content = re.compile(pat_content).findall(source)
    ########################### 查找逆回购操作的表格 ###############################
    pat_table_RR_title_column = '<p align="center"><strong><span style="font-size: 16px"><span style="color: #222222"><span style="font-family: 宋体">.......</span></span></span></strong></p><p></p><table align="center" border="1" cellpadding="0" cellspacing="0" style="border-bottom: windowtext 1px solid; border-left: windowtext 1px solid; width: 526px; border-top: windowtext 1px solid; border-right: windowtext 1px solid" width="526"><tbody><tr><td style="border-bottom: windowtext 1px solid; border-left: windowtext 1px solid; width: 175px; height: 21px; border-top: windowtext 1px solid; border-right: windowtext 1px solid"><p align="center"><span style="font-size: medium"><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span></span></span></p> </td><td style="border-bottom: windowtext 1px solid; border-left: windowtext 1px solid; width: 175px; height: 21px; border-top: windowtext 1px solid; border-right: windowtext 1px solid"><p align="center"><span style="font-size: medium"><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span></span></span></p> </td><td style="border-bottom: windowtext 1px solid; border-left: windowtext 1px solid; width: 175px; height: 21px; border-top: windowtext 1px solid; border-right: windowtext 1px solid"><p align="center"><span style="font-size: medium"><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span></span></span></p>  </td></tr>'.replace(' ','')
    pat_table_RR_content = '<tr><td style="border-bottom: windowtext 1px solid; border-left: windowtext 1px solid; width: 175px; height: 21px; border-top: windowtext 1px solid; border-right: windowtext 1px solid"><p align="center"><span style="font-size: medium"><span style="color: #222222"><span style="font-family: arial, sans-serif">(.*?)</span></span></span><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span></span></p> </td> <td style="border-bottom: windowtext 1px solid; border-left: windowtext 1px solid; width: 175px; height: 21px; border-top: windowtext 1px solid; border-right: windowtext 1px solid"><p align="center"><span style="font-size: medium"><span style="color: #222222"><span style="font-family: arial, sans-serif">(.*?)</span></span></span><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span></span></p> </td><td style="border-bottom: windowtext 1px solid; border-left: windowtext 1px solid; width: 175px; height: 21px; border-top: windowtext 1px solid; border-right: windowtext 1px solid"><p align="center"><span style="color: #222222"><span style="font-family: arial, sans-serif"><span style="font-size: medium">(.*?)</span></span></span></p> </td></tr>'.replace(' ','')
    str_RR_list = [pat_table_RR_title_column, pat_table_RR_content,'</tbody></table>']
    num = 1
    pat_table_RR = ''.join(str_RR_list)
    content_table_RR = re.compile(pat_table_RR).findall(source)
    while content_table_RR != []:
        num = num + 1
        str_RR_list.insert(num,pat_table_RR_content)
        pat_table_RR = ''.join(str_RR_list)
        content_table_RR = re.compile(pat_table_RR).findall(source)

    # 期限及中标率
    pat_table_1 = '<span style="font-family: arial, sans-serif">(.*?)</span></span></span><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span>'
    content_table_1 = re.compile(pat_table_1).findall(source)
    # 利率
    pat_table_2 = '<span style="font-family: arial, sans-serif"><span style="font-size: medium">(.*?)</span>'
    content_table_2 = re.compile(pat_table_2).findall(source)
    ##############################不同类型的通知标题还不一样，我傻了###################################
    pat_title_table_RR = '<strong><span style="color: #222222"><span style="font-family: 宋体"><span style="font-size: medium">(.*?)</span></span></span></strong>'
    title_table_RR = re.compile(pat_title_table_RR).findall(source)
    if title_table_RR == []:
        pat_title_table_MLF = '<strong><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span></span></strong></span><strong><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span></span></strong>'
        title_table_MLF = re.compile(pat_title_table_MLF).findall(source)
        detail = content[0] + title_table_MLF[0][0] + title_table_MLF[0][1] + ":" + title_column[0] + "为" + content_table_1[0][0] + content_table_1[0][1] + "，" + title_column[1] + "为" + content_table_1[1][0] + content_table_1[1][1] + "," + title_column[1] + "为" + content_table_2[0] + "。"
    else:
        detail = content[0] + ''.join(title_table_RR) + ":" + title_column[0] + "为" + content_table_1[0][0] + content_table_1[0][1] + "，" + title_column[1] + "为" + content_table_1[1][0] + content_table_1[1][1] + "," + title_column[2] + "为" + content_table_2[0] + "。"

pat_contentalt = '<p align="left">(.*?)</p>'
contentalt = re.compile(pat_contentalt).findall(source)

print(contentalt[0])


pat_title = '<h2 style="font-size: 16px;color: #333;">(.*?)</h2>'
title = re.compile(pat_title).findall(source)

pat_content = '<p>(.*?)</p>'
content = re.compile(pat_content).findall(source)

pat_title1 = '<span style="font-size: medium"><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span>'
title1 = re.compile(pat_title1).findall(source)

pat_content1 = '<span style="font-family: arial, sans-serif">(.*?)</span></span></span><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span>'
content1 = re.compile(pat_content1).findall(source)

pat_content2= '<span style="font-family: arial, sans-serif"><span style="font-size: medium">(.*?)</span>'
content2 = re.compile(pat_content2).findall(source)


# datelist = re.findall(r"\d+\.?\d*", content[0])
# date = datelist[0] + '/' + datelist[1] + '/' + datelist[2]
detail = content[0] + title1[0] + "为" + content1[0][0] + content1[0][1] + "，" + title1[1] + "为" + content1[1][0] + content1[1][1] + "," + title1[1] + content2[0] + "。"
print(detail)
