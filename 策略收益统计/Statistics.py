#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
私募基金情况统计
"""

import pandas as pd
import numpy as np
from uqer import Client,DataAPI

Client(token = '74af102f6de8e63ebb1b3cb80a6ccff887c76a06f361c73ed5edf9feb81595f2')

df = DataAPI.PfundGet(statusCD='100',field="secID,secIDInt,secFullName,invStgyCD,invStgy,invStgyChildCD,invStgyChild")


# a.to_excel(r'C:\Users\Admin\Desktop\基金基本信息.xlsx')
idli = np.array(df[['secID']].unstack()).tolist()

data = DataAPI.PfundPerfIndicGet(dataDate=u"20181102",window=u"7",secID=idli,field='secID,secIDInt,secFullName,establishDate,pfStyleCD,pfStyle,statusCD,status,invStgyCD',pandas="1")