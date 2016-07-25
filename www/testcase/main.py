#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append(sys.path[0])


import unittest

from www.common.database import create_engine

from www.testcase.ts_ws_login import login
from www.testcase.ts_ws_version import compareAppVersion
from www.testcase.ts_ws_password import modifyPassword

from www.testcase.ts_ws_common import getAllAreaList
from www.testcase.ts_ws_common import getAreaListByCondition
from www.testcase.ts_ws_common import getAreaListStandAlone
from www.testcase.ts_ws_common import getBannerList
from www.testcase.ts_ws_common import getCouponParam
from www.testcase.ts_ws_common import getTopicList
from www.testcase.ts_ws_common import userAgreementUrl

from www.testcase.ts_ws_invoice import addInvoice
from www.testcase.ts_ws_invoice import delInvoice
from www.testcase.ts_ws_invoice import getInvoiceList
from www.testcase.ts_ws_invoice import modifyInvoice
from www.testcase.ts_ws_invoice import setDefaultInvoice

from www.testcase.ts_ws_merch import getCategoryList
from www.testcase.ts_ws_merch import getMerchDetail
from www.testcase.ts_ws_merch import getMerchList

from www.testcase.ts_ws_regist import getArea
from www.testcase.ts_ws_regist import getTerminalShopTypeList

from www.testcase.ts_ws_shoppingcart import addShoppingcart
from www.testcase.ts_ws_shoppingcart import createOrderByShoppingcart
from www.testcase.ts_ws_shoppingcart import delShoppingcartByProductIds
from www.testcase.ts_ws_shoppingcart import getPreViewOrderByShoppingcart
from www.testcase.ts_ws_shoppingcart import getShoppingcartSize
from www.testcase.ts_ws_shoppingcart import modifyShoppingcartCount
from www.testcase.ts_ws_shoppingcart import toShoppingcart


if __name__ == '__main__':

    create_engine()
    runner = unittest.TextTestRunner()

    # 登录、升级、修改密码
    runner.run(login.suite())
    runner.run(compareAppVersion.suite())
    runner.run(modifyPassword.suite())

    # 公共
    runner.run(getAllAreaList.suite())
    runner.run(getAreaListByCondition.suite())
    runner.run(getAreaListStandAlone.suite())
    runner.run(getBannerList.suite())
    runner.run(getCouponParam.suite())
    runner.run(getTopicList.suite())
    runner.run(userAgreementUrl.suite())

    # 发票
    runner.run(addInvoice.suite())
    runner.run(delInvoice.suite())
    runner.run(getInvoiceList.suite())
    runner.run(modifyInvoice.suite())
    runner.run(setDefaultInvoice.suite())

    # 商品
    runner.run(getCategoryList.suite())
    runner.run(getMerchDetail.suite())
    runner.run(getMerchList.suite())

    # 注册
    runner.run(getArea.suite())
    runner.run(getTerminalShopTypeList.suite())

    # 购物车
    runner.run(addShoppingcart.suite())
    runner.run(createOrderByShoppingcart.suite())
    runner.run(delShoppingcartByProductIds.suite())
    runner.run(getPreViewOrderByShoppingcart.suite())
    runner.run(getShoppingcartSize.suite())
    runner.run(modifyShoppingcartCount.suite())
    runner.run(toShoppingcart.suite())




