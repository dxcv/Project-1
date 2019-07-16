#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把Excel处理成panel数据
"""

import pandas as pd
import os
import numpy as np
import math

# 获取原始数据文件夹中的所有文件
pathfromNumber = r'D:\Paper\Data\Original_BankScope\Number'
pathfromRatio = r'D:\Paper\Data\Original_BankScope\Ratios'
pathfromTS = r'D:\Paper\Data\Original_BankScope\TimeSeries'
pathbankname = r'D:\Paper\Data\Original_BankScope\BankName_all.xlsx'
pathto = r'D:\Paper\Data\Cleaned'

files = os.listdir(pathfromNumber)


dfli = []
colli = []
for file in files:
    filepath = pathfromNumber+'\\'+file
    a = pd.read_excel(io=filepath, sheet_name=0, index_col=0, header=0)
    a.columns = [int(x.split('\nCNY\n')[1]) for x in a.columns]
    b = a.stack()
    # b = a.apply(lambda x:''.join(x.split(',')))
    # c = b.apply(lambda x: x/100000000 if isinstance(x, int) == True else x)
    colli.append(file.split('.')[0])
    dfli.append(b)
#
files = os.listdir(pathfromRatio)
for file in files:
    filepath = pathfromRatio+'\\'+file
    a = pd.read_excel(io=filepath, sheet_name=0, index_col=0, header=0)
    a.columns = [int(x.split('\n%\n')[1]) for x in a.columns]
    b = a.stack()
    colli.append(file.split('.')[0])
    dfli.append(b)

df = pd.concat(dfli, axis=1, join='outer',sort=True)


result1 = df.reset_index(level=[0,1])
result1.columns = ['BankName','Year'] + colli
# 将年份这一列的数据类型转换
result1 = result1.set_index(['Year','BankName'])

tsli = [result1]
files = os.listdir(pathfromTS)
for file in files:
    filepath = pathfromTS+'\\'+file
    a = pd.read_excel(io=filepath, sheet_name=0, index_col=0, header=0)
    colli.append(file.split('.')[0])
    result1 = pd.merge(result1,a,how='left',left_on='Year',right_index=True)


result1 = result1.reset_index(level=[0])

bankname = pd.read_excel(io=pathbankname, sheet_name=0, index_col=0, header=0,usecols="A:C")

result = pd.merge(bankname,result1,how='inner',left_on='BankName',right_index=True)
result.replace('n.a.',np.nan,inplace=True)
result.replace('n.s.',np.nan,inplace=True)

result = pd.DataFrame(result,dtype=np.float)

# result['MainOperatingIncome'] = result['OperatingIncome'] - result['OtherOperatingIncome']
# result['MainInterestIncome'] = result['TotalInterestIncome'] - result['OtherInterestIncome']

# result['II'] = result['Interestincomeoncustomerloans'] + result['Interestincomeoninterbankloans'] + result['Interestincomeonstock']+result['OtherInterestIncome']
result['NII'] = result['FeeandCommission']
# result['NII'] = result['OperatingIncome']+result['OtherInterestIncome']-result['II']

result['NIIR'] = result['NII']/result['OperatingIncome']*100

# result['NIIR2'] = result['NIIR']*result['NIIR']
# result['NDI'] =  result['NII'] / result['II']*100

# result['TOFER'] = result['Totaloffbanlancesheetexposure']/result['TA']*100

# result['LnTA'] = [math.log(x) for x in result['TA']]
# result['LnM2'] = [math.log(x) for x in result['M2']]
# result['LnGM2'] = [math.log(x) for x in result['GM2']]
# result['LnNIIR'] = [abs(math.log(abs(x))) for x in result['GM2']]

# result['DPL'] = result['Loans']/result['TotalDeposit']*100
#
# result['ILR'] = result['ILGLR']*result['GrossLoans']/result['Loans']*100
result['FAR'] = result['FixedAssets']/result['TA']*100

# result['z1'] = result['ROA']-result['CAR']
# var = pd.DataFrame(result.groupby(by=result.index)['ROA'].mean())
# var.columns = ['Roa_mean']
# result = pd.merge(result,var,how='left',left_on='BankName',right_index=True)
# result['Z'] = abs(result['z1']-result['Roa_mean'])

# result['LnZ'] = [math.log(x) for x in result['Z']]
# result['NII_DLMI'] = result['NII']*result['DLMI']
# result['NII_NDLMI'] = result['NII']*result['NDLMI']
# result['NII_MI'] = result['NII']*result['MI']


# result['NIIR_DLMI'] = result['NIIR']*result['DLMI']
# result['NIIR_NDLMI'] = result['NIIR']*result['NDLMI']
# result['NIIR_MI'] = result['NIIR']*result['MI']
#
# result['NDI_DLMI'] = result['NDI']*result['DLMI']
# result['NDI_NDLMI'] = result['NDI']*result['NDLMI']
# result['NDI_MI'] = result['NDI']*result['MI']
#
# result['TOFER_DLMI'] = result['TOFER']*result['DLMI']
# result['TOFER_NDLMI'] = result['TOFER']*result['NDLMI']
# result['TOFER_MI'] = result['TOFER']*result['MI']




result.dropna(how='all')

result.to_excel(pathto+'\\BankName_all.xlsx',index=True)
result.to_stata(pathto+'\\BankName_all.dta',write_index=False)