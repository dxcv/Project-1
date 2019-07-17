#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CXM

import urllib.request
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
driver = webdriver.Chrome(chrome_options=chrome_options) # 打开浏览器
driver.get("http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/17081/index1.html") #用webdriver打开人行政策货币司
source = driver.page_source #获取网页源代码 str
driver.close()  #回收资源

# pat_str = "/zhengcehuobisi/125207/125213/125431/125475/[0-9]+/[index[1-9]+.html|index.html]"
pat_str = 'totalpage="...'
linklist = re.compile(pat_str).findall(source)

# for link in linklist:
#     print(link)
#
# url = "http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html"
#
# req = urllib.request.Request(url)
#
# data = str(urllib.request.urlopen(req).read(),encoding="utf-8")
#
# pat = "/zhengcehuobisi/125207/125213/125431/125475/[0-9]+/[index.html]"
#
# ##### 测试用
# string = "/zhengcehuobisi/125207/125213/125431/125475/3844768/index.html"
# result = re.match(pat,string)
# print(result)
# ######
#
# # result = re.compile(pat).findall(data)
# # print(result)


# def getlink(url_str,pat_str):
#     #模拟成浏览器
#     headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
#     opener = urllib.request.build_opener()
#     opener.addheaders = [headers]
#     #将opener安装为全局
#     urllib.request.install_opener(opener)
#     data = str(urllib.request.urlopen(url_str).read(), encoding="utf-8")
#     link = re.compile(pat_str).findall(data)
#     link = list(set(link))
#     return link
#
# url_str = "http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html"
# pat_str = "/zhengcehuobisi/125207/125213/125431/125475/[0-9]+/[index.html]"
#
# linklist = getlink(url_str, pat_str)
#
# print(linklist)