#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GJ05.请求拆分订单（新增）
http://127.0.0.1:8080/mallws/orders/preSeparateOrder.json
{
    "token":"123",                          // 必须
    "orderNo":"123123123",                  // 必须 订单号
}
{
    "code": 200,
    "description": "执行成功!",
    "model": {
        "orderNo":"123123123",              // 订单号
        "orderAmount":"50000",              // 订单金额
        "success": "0",                     // 成功 0-成功  1-不成功
        "separateOrderTimes":"7",           // 订单可以拆分次数  如果不能拆分，则为0
        "buyerName":"123",                  // 买家名

     },
    "metadata": {
        "type": 0,
        "clazz": "cn.com.hd.mall.web.webservices.entity.response.order.PreSeparateOrderResponse"
    }

}
"""

import unittest

from www.common.database import *
from www.common.excel import *
from www.common.webservice import *

class preSeparateOrder(unittest.TestCase):
    pass


def suite():
    suite=unittest.TestSuite()
    return suite