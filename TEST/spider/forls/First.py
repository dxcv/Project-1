#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CXM


import re
import sys
sys.path.append(r'D:\Python\Project\TEST\spider\forls')
import Main

func = Main.Functions()
#获得公告的总页数
totalpage = int(re.compile('totalpage="...').findall(func.getcode(r"http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/17081/index1.html"))[0][-3:-1])



for i in range(1,totalpage+1):
    url = "http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/17081/index" + str(i) + ".html"
    source = func.getcode(url)
    pat_link = "/zhengcehuobisi/125207/125213/125431/125475/[0-9]+/index.html"
    linklist = re.compile(pat_link).findall(source)
    for link in linklist:
        url_detail = "http://www.pbc.gov.cn"+link
        source_detail = func.getcode(url_detail)
        detail = func.getdetail(source_detail)
        print(detail)





