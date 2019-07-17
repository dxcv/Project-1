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
driver.get("http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/3852933/index.html") #用webdriver打开人行政策货币司
source = driver.page_source #获取网页源代码 str
driver.close()  #回收资源
# print(source)

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
