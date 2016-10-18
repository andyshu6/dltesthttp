#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GJ04.查看已拆分订单（新增）
http://127.0.0.1:8080/mallws/orders/getSeparateOrderList.json
{

    "token":"123",                          // 必须
    "orderNo":"123123123"                   // 必须 订单号
}

{
    "code": 200,
    "description": "执行成功!",
    "model": {
        "success": "0",                                     // 成功 0-成功 1-不成功
        "paymentInfoList":[
            {
                "separatePaymentNo":"201510021725-A-01",    // 拆分后的支付单号
                "separateOrderAmount":"50000"               // 拆分后的子订单号对应的支付金额（单位：分）
                "payStatus":"01"                           //  支付状态(00-未支付，01-已支付)
            }
        ]
     },
    "metadata": {
        "type": 0,
        "clazz": "cn.com.hd.mall.web.webservices.entity.response.order.CheckSeparateOrderListsResponse"
    }
}
"""

import unittest

from www.common.database import *
from www.common.excel import *
from www.common.webservice import *

class getSeparateOrderList(unittest.TestCase):
    pass

    # S1.查看拆分订单


    # S2.查看其他人的拆分订单


    # S3.查看未拆分订单


def suite():
    suite=unittest.TestSuite()
    return suite