#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GJ03.拆分订单（新增）
http://127.0.0.1:8080/mallws/orders/separateOrder.json
{
    "token":"123",                          // 必须
    "orderNo":"10621581690013",                  // 必须 订单号
    "separateOrderAmount":[                 // 每个子订单的拆分金额（单位：分）
        "50000",
        "200000",
        "5000"
        ]
}

{
    "code": 200,
    "description": "执行成功!",
    "model": {
        "success": "0",                                     // 成功 0-成功      1-不成功    2-您还有剩余金额未拆分
        "orderNo":"123123123",                              // 订单号
        "paymentList":[
            {
                "separatePaymentNo":"201510021725-A-01",    // 拆分后的支付单号
                "separateOrderAmount":"50000"               // 拆分后的子订单号对应的支付金额(单位：分)
            }
        ]
     },
    "metadata": {
        "type": 0,
        "clazz": "cn.com.hd.mall.web.webservices.entity.response.order.SeparateOrderResponse"
    }
}
"""

import unittest

from www.common.database import *
from www.common.excel import *
from www.common.webservice import *

class separateOrder(unittest.TestCase):
    pass


def suite():
    suite=unittest.TestSuite()
    return suite