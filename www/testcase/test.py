#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
path = sys.path[0] + '/../..'
sys.path.append(path)
import unittest


from www.common.database import *
create_engine()
# from www.testcase.ts_ws_account import activatePhone
# from www.testcase.ts_ws_merch import getNewMerchList
# from www.testcase.ts_ws_shoppingcart import checkSwitch
# from www.common import env_init
# from www.testcase.ts_ws_login import login
# from www.testcase.ts_ws_shoppingcart import sendMessage
# from www.operation.order import createOrder
# from www.common.excel import eData
# from www.testcase.ts_ws_orders import cancel
# from www.testcase.ts_ws_orders import deliver,auditCancel
# from www.testcase.ts_ws_shoppingcart import createOrderByShoppingcartNew
# from www.testcase.ts_ws_common import getCouponParam
# from www.testcase.ts_ws_orders import getBuyerOrderCount
# from www.testcase.ts_ws_orders import getSellerOrderCount
# from www.testcase.ts_ws_message import count
# from www.testcase.ts_ws_orders import getOrderLog
from www.testcase.ts_ws_orders import getSellerOrderList
from www.testcase.ts_ws_login import login
#from www.testcase.ts_ws_orders import getBuyerOrderDetail

if __name__ == '__main__':

    # UserShop = eData('TmlShop')
    # UserShop2 = eData('TmlShop2')
    # Merch1 = eData('Merch1')
    # Merch2 = eData('Merch2')
    # Merch4 = eData('Merch4')


    # import json
    # b='{"customerId":"cb595ea8968a4b87b885d08a2834904e","status":null}'
    # d = json.loads(b)
    # print d


    #env_init.run()
    runner = unittest.TextTestRunner()
    #runner.run(login.suite())
    #runner.run(getSellerOrderList.suite())
    from www.testcase.ts_ws_orders import deliver
    from www.testcase.ts_ws_orders import getBuyerOrderDetail, getBuyerOrderList,getOrderLog,getSellerOrderList,getSellerOrderDetail
    # runner.run(getBuyerOrderDetail.suite())
    runner.run(getBuyerOrderList.suite())
    runner.run(getOrderLog.suite())
    runner.run(getSellerOrderList.suite())
    # runner.run(getSellerOrderDetail.suite())
    runner.run(deliver.suite())
    #runner.run(getBuyerOrderDetail.suite())
    #runner.run(createOrderByShoppingcartNew.suite())
    #runner.run(count.suite())
    #runner.run(auditCancel.suite())
    #runner.run(getSellerOrderCount.suite())
    # runner.run(deliver.suite())
    #runner.run(login.suite())
    #runner.run(addInvoice.suite())
    # runner.run(getCompanyInfo.suite())
    # runner.run(getAcctInfo.suite())
    # runner.run(activatePhone.suite())
    #runner.run(login.suite())
    # runner.run(resetPsw.suite())
    # runner.run(getValCodeForPsw.suite())
    # runner.run(addFavorite.suite())
    # runner.run(checkSwitch.suite())
    #filePath = "pyResult.html"
    #fp = file(filePath,'wb')
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Python Test Report',description='This  is Python  Report')
    #runner.run(getCategoryList.suite())
    # runner.run(toChangeOrderPricePage.suite())
    # runner.run(deliverChangePrice.suite())
    # runner.run(getMerchDetail.suite())
    # runner.run(getMerchList.suite())
    # runner.run(getNewMerchList.suite())
    # runner.run(getNewMerchDetail.suite())
    # runner.run(getPromotionList.suite())
    # runner.run(getRecommendList.suite())
    # runner.run(getOftenBuyList.suite())
    #runner.run(addDeliverAddress.suite())
    #runner.run(modifyPassword.suite())
    #fp.close()
    #runner.run(ts_ws_invoice_getInvoiceList.suite())
    #runner.run(ts_ws_invoice_modifyInvoice.suite())
    #runner.run(ts_ws_invoice_setDefaultInvoice.suite())

    #runner.run(ts_ws_common_getTopicList.suite())


