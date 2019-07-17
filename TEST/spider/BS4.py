#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
beautifulsoup
"""
from bs4 import BeautifulSoup
from urllib import request
from urllib.error import HTTPError


url = "http://www.pythonscraping.com/pages/page3.html"
try:
    html = request.urlopen(url)
except HTTPError as e:
    print(e)
else:
    bsObj = BeautifulSoup(html,"lxml")
    # print(bsObj)
    li = bsObj.find("table",{"id":"giftList"}).children
    for i in li:
        print(i)