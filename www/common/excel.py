#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
from www.common.other import Dict
from xlutils.copy import copy
import logging
from www.common.other import Dict
import logging
import os

BASE_DIR = os.path.dirname(__file__)
TestData = BASE_DIR + '/../../testdata/userdata.xls'

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
        if '{' in values and '}' in values:
            dictData = eval(values.encode('utf-8'))
            dictKeys = []
            dictValues = []
            for (k, v) in dictData.iteritems():
                dictKeys.append(k)
                dictValues.append(v)
            excelData[keys] = Dict(dictKeys, dictValues)
        else:
            excelData[keys] = values.encode('utf-8')
    return excelData

def write_excel(sheetname=u'Sheet1',rowkey=1, rowvalue=1, file = TestData):
    rb = xlrd.open_workbook(file, formatting_info=True)
    table = rb.sheet_by_name(sheetname)
    i = 0
    for sheet in rb.sheets():
        if sheetname == sheet.name:
            wb = copy(rb)
            ws = wb.get_sheet(i)
            nrows = table.nrows
            for rownum in range(1, nrows):
                if table.cell(rownum, 0).value == rowkey:
                    ws.write(rownum, 1, rowvalue)
                    wb.save(TestData)
                    break
        else:
            i+=1
    return eData(sheetname)

def getValue(sheetname, cellname, file = 'C:\\Users\\Roy\\PycharmProjects\\dltest\\testdata\\userdata.xlsx'):
    data = eData(sheetname,file)
    return data[cellname]




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    UserA = eData('TmlShop')
    #print UserA.orderCodWaitDeliver.paymentNo
    print type(UserA.orderCodWaitDeliver)
    print UserA.orderCodWaitDeliver
    print UserA.orderCodWaitDeliver.orderNo
    #UserA_new = write_excel('TmlShop', 'orderOnlineWaitPay', "test")
    # print UserA_new
    # print UserA_new.orderOnlineWaitPay
