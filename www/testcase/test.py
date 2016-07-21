#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from www.common.database import *
from www.testcase import ts_ws_invoice_addInvoice
import ts_ws_invoice_delInvoice
import HTMLTestRunner
import ts_ws_shoppingcart_getPreViewOrderByShoppingcart

if __name__ == '__main__':

    #filePath = "//Users//Mr_Chen//Desktop//PythonWork//pyResult.html"

    create_engine()
    #runner = unittest.TextTestRunner()
    filePath = "pyResult.html"
    fp = file(filePath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Python Test Report',description='This  is Python  Report')
    runner.run(ts_ws_shoppingcart_getPreViewOrderByShoppingcart.suite())
    fp.close()
    #runner.run(ts_ws_invoice_getInvoiceList.suite())
    #runner.run(ts_ws_invoice_modifyInvoice.suite())
    #runner.run(ts_ws_invoice_setDefaultInvoice.suite())

    #runner.run(ts_ws_common_getTopicList.suite())

