#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
发送请求
python3写法
"""
# urllib2包已经拆分
import urllib
from urllib import request
from urllib import parse
from http import cookiejar
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

# values = {'username':'123','password':'123'}
# url = 'http://httpbin.org/post'
# headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'}
# data = parse.urlencode(values).encode(encoding='utf8')
# req = request.Request(url, data, headers, method='POST')
# reponse = request.urlopen(req)
# print(reponse.read().decode('utf8'))

# 高级用法

username =