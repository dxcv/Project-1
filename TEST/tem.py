#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把list切片输出
"""


li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

l = len(li)/5
# if l==0:
#     for x in range(0,int(l)):
#         print(li[(5*x):(5*(x+1))])
# else:
a = []
for x in range(0,int(l)):
    print(li[(5*x):(5*(x+1))])
    a.append(li[(5*x):(5*(x+1))])
print(li[int(l)*5:])
if li[int(l)*5:]==[]:
    pass
else:
    a.append(li[int(l)*5:])
print(a)
