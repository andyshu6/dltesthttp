#!/usr/bin/env python
# -*- coding: utf-8 -*-

import HTMLTestRunner

import sys
path = sys.path[0] + '/../..'
sys.path.append(path)
import unittest

from www.testcase.ts_ws_login import login
from www.common.database import *
from www.testcase.ts_ws_shoppingcart import createOrderByShoppingcart
from www.testcase.ts_ws_password import modifyPassword
from www.testcase.ts_ws_merch import getMerchList
from www.testcase.ts_ws_shoppingcart import addShoppingcart
from www.testcase.ts_ws_deliverAddress import addDeliverAddress
from www.testcase.ts_ws_deliverAddress import delDeliverAddress
from www.testcase.ts_ws_deliverAddress import getDeliverAddressList
from www.testcase.ts_ws_deliverAddress import getTerminalAddress
from www.testcase.ts_ws_deliverAddress import modifyDeliverAddress
from www.testcase.ts_ws_deliverAddress import setDefaultDeliverAddress
from www.testcase.ts_ws_favorite import addFavorite
from www.testcase.ts_ws_favorite import getFavoriteList
from www.testcase.ts_ws_favorite import getFavoriteListSize
from www.testcase.ts_ws_favorite import delFavorite

if __name__ == '__main__':


    create_engine()
    runner = unittest.TextTestRunner()
    #runner.run(login.suite())

    #filePath = "pyResult.html"
    #fp = file(filePath,'wb')
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Python Test Report',description='This  is Python  Report')

    runner.run(createOrderByShoppingcart.suite())
    #runner.run(modifyPassword.suite())

    #runner.run(login.suite())
    runner.run(addFavorite.suite())
    runner.run(getFavoriteList.suite())
    runner.run(getFavoriteListSize.suite())
    runner.run(delFavorite.suite())

    #fp.close()
    #runner.run(ts_ws_invoice_getInvoiceList.suite())
    #runner.run(ts_ws_invoice_modifyInvoice.suite())
    #runner.run(ts_ws_invoice_setDefaultInvoice.suite())
    #runner.run(ts_ws_common_getTopicList.suite())

