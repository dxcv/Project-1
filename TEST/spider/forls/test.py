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
driver.get("http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/3245262/index.html") #用webdriver打开人行政策货币司
source = driver.page_source#.replace('\n','').replace('\n','').replace(' ','') #获取网页源代码 str
driver.close()  #回收资源

pat_title_table_column = '<span style="font-size: medium;"><span style="color: rgb(34, 34, 34);"><span style="font-family: 宋体;">(.+?)</span></span></span>'#.replace(' ','')
title_table_column = re.compile(pat_title_table_column).findall(source)
print(pat_title_table_column)
print(title_table_column)