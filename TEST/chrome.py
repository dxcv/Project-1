#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
chromedriver+headless
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
a = driver.get("https://cnblogs.com/")
print(a)