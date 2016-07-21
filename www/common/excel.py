#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import logging
from www.common.other import Dict
import logging
import os

BASE_DIR = os.path.dirname(__file__)
TestData = BASE_DIR + '/../../testdata/userdata.xlsx'

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        logging.info(str(e))

def eData(sheetname=u'Sheet1', file = TestData):
    data = open_excel(file)
    table = data.sheet_by_name(sheetname)
    nrows = table.nrows
    excelData = Dict()
    for rownum in range(1,nrows):
        keys = table.cell(rownum,0).value
        values = table.cell(rownum,1).value
        excelData[keys] = values.encode('utf-8')
    return excelData

def getValue(sheetname, cellname, file = 'C:\\Users\\Roy\\PycharmProjects\\dltest\\testdata\\userdata.xlsx'):
    data = eData(sheetname,file)
    return data[cellname]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    UserA = eData('DealMager')
    print UserA
    print UserA.username

    logging.info(UserA.companyName)
    print UserA.companyName
    print getValue('DealMager', 'companyName')
