#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
chromedriver
"""
from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)
