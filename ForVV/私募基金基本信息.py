#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
私募基金基本信息
"""

from uqer import DataAPI,Client
login = Client(token='07b082b1f42b91987660f0c2c19097bc3b10fa4b12f6af3274f82df930185f04')

df = DataAPI.PfundGet(pfStyleCD=['14,15'],statusCD=u"100",field=u"",pandas="1")

df.to_excel(r'C:\Users\Admin\Desktop\基金基本信息.xlsx',index=False)