#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CXM

#人行网站用js整体渲染反爬，第一次用selenium写爬虫

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
import urllib.request
from bs4 import BeautifulSoup
import html.parser



#获取网页源代码 str
def getcode(url):
    # 不显示webdriver弹出窗口
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    driver = webdriver.Chrome(chrome_options=chrome_options) # 打开浏览器
    driver.get(url) #用webdriver打开人行政策货币司
    source = driver.page_source #获取网页源代码 str
    driver.close()  #回收资源
    return source
# print(source)


def getdetail(source):
    #获取文件标题
    pat_title = '<h2 style="font-size: 16px;color: #333;">(.*?)</h2>'
    title = re.compile(pat_title).findall(source)

    ########正文部分#######
    #文字部分
    pat_content = '<p>(.*?)</p>'
    content = re.compile(pat_content).findall(source)
    # 匹配日期
    datelist = re.findall(r"\d+\.?\d*", content[0])
    date = datelist[0] + '/' + datelist[1] + '/' + datelist[2]

    #表格标题
    pat_title1 = '<span style="font-size: medium"><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span>'
    title1 = re.compile(pat_title1).findall(source)

    if title1: #网页中没有表格不进行进一步的解析
        # 期限及中标率
        pat_content1 = '<span style="font-family: arial, sans-serif">(.*?)</span></span></span><span style="color: #222222"><span style="font-family: 宋体">(.*?)</span>'
        content1 = re.compile(pat_content1).findall(source)
        # 利率
        pat_content2 = '<span style="font-family: arial, sans-serif"><span style="font-size: medium">(.*?)</span>'
        content2 = re.compile(pat_content2).findall(source)
        detail = content[0] + title1[0] + "为" + content1[0][0] + content1[0][1] + "，" + title1[1] + "为" + content1[1][0] + content1[1][1] + "," + title1[1] + content2[0] + "。"
    else:
        detail = content[0]

    return date,title[0],detail

#获得公告的总页数
totalpage = int(re.compile('totalpage="...').findall(getcode("http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/17081/index1.html"))[0][-3:-1])



for i in range(1,totalpage+1):
    url = "http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/17081/index"+ str(i) +".html"
    source = getcode(url)
    pat_link = "/zhengcehuobisi/125207/125213/125431/125475/[0-9]+/index.html"
    linklist = re.compile(pat_link).findall(source)
    for link in linklist:
        url_detail = "http://www.pbc.gov.cn"+link
        source_detail = getcode(url_detail)
        detail = getdetail(source_detail)
        print(detail)




# # ****************** Scroll to the bottom, and click the "view more" button *********
# pat_str = "/zhengcehuobisi/125207/125213/125431/125475/[0-9]+/[index[1-9]+.html|index.html]"
# source = getcode("http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/17081/index2.html")
# linklist = re.compile(pat_str).findall(source)
#
# detail = getdetail(getcode("http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/3850663/index.html"))
# print(linklist[:5])
# print(detail)



