#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(16).reshape((4,4)),index=['a','b','c','d'],columns=['one','two','three','four'])
df.set_index(['one','two'],inplace=True)

df.loc[0,1]['three']=4
