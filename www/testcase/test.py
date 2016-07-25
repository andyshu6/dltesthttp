#!/usr/bin/env python
# -*- coding: utf-8 -*-

import HTMLTestRunner

import sys
sys.path.append(sys.path[0])
import unittest
from www.common.database import *
from www.testcase.ts_ws_shoppingcart import createOrderByShoppingcart

if __name__ == '__main__':


    create_engine()
    runner = unittest.TextTestRunner()
    runner.run(createOrderByShoppingcart.suite())

    #filePath = "pyResult.html"
    #fp = file(filePath,'wb')
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Python Test Report',description='This  is Python  Report')
    #runner.run(createOrderByShoppingcart.suite())
    #fp.close()
    #runner.run(ts_ws_invoice_getInvoiceList.suite())
    #runner.run(ts_ws_invoice_modifyInvoice.suite())
    #runner.run(ts_ws_invoice_setDefaultInvoice.suite())

    #runner.run(ts_ws_common_getTopicList.suite())

