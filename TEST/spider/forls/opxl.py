#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CXM

import openpyxl

wb = openpyxl.load_workbook(r'D:\Python\Project\TEST\spider\forls\OpenMarketOperationRecord.xlsx')
worksheet = wb.active

# wb.save(r'D:\Python\Project\TEST\spider\forls\OpenMarketOperationRecord.xlsx')
