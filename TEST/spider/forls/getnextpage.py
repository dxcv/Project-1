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
driver.get("http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/3850663/index.html") #用webdriver打开人行政策货币司
source = driver.page_source #获取网页源代码 str
driver.close()  #回收资源

pat = '<a style="cursor:pointer" onclick="queryArticleByCondition(this,(.*?))" tagname=(.*?) class="pagingNormal">下一页</a>'
link = re.compile(pat).findall(source)