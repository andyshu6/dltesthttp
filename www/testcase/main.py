#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import ts_ws_invoice_delInvoice
import ts_ws_invoice_getInvoiceList
import ts_ws_invoice_modifyInvoice
import ts_ws_login_login
import ts_ws_merch_getCategoryList
import ts_ws_merch_getMerchDetail
import ts_ws_merch_getMerchList
import ts_ws_regist_getArea
import ts_ws_regist_getTerminalShopTypeList
import ts_ws_version_compareAppVersion
from www.common.database import create_engine
from www.testcase import ts_ws_invoice_setDefaultInvoice
from www.testcase.invoice import ts_ws_invoice_addInvoice

if __name__ == '__main__':

    create_engine()
    runner = unittest.TextTestRunner()
    runner.run(ts_ws_login_login.suite())
    runner.run(ts_ws_version_compareAppVersion.suite())
    runner.run(ts_ws_invoice_addInvoice.suite())
    runner.run(ts_ws_invoice_delInvoice.suite())
    runner.run(ts_ws_invoice_getInvoiceList.suite())
    runner.run(ts_ws_invoice_modifyInvoice.suite())
    runner.run(ts_ws_invoice_setDefaultInvoice.suite())
    runner.run(ts_ws_merch_getCategoryList.suite())

    # 商品
    runner.run(ts_ws_merch_getCategoryList.suite())
    runner.run(ts_ws_merch_getMerchList.suite())
    runner.run(ts_ws_merch_getMerchDetail.suite())

    # 注册
    runner.run(ts_ws_regist_getTerminalShopTypeList.suite())
    runner.run(ts_ws_regist_getArea.suite())