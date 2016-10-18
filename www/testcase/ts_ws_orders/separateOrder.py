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
from www.operation.order import createOrder

class separateOrder(unittest.TestCase):
    UserShop = eData('TmlShop')
    DealMager = eData('DealMager')
    DealMager2 = eData('DealMager2')
    Merch = eData('Merch1')


    wsUserShop = webservice()
    wsUserShop.login(UserShop.username, UserShop.password)
    wsDealMager = webservice()
    wsDealMager.login(DealMager.username, DealMager.password)
    wsDealMager2 = webservice()
    wsDealMager2.login(DealMager2.username, DealMager2.password)

    # S1.货到付款待发货订单拆分订单(2单)
    def test_separateOrder_separat(self):
        order = createOrder(self.UserShop, self.Merch)
        sepOrder = self.wsDealMager.separateOrder(orderNo=order.orderNo, separateOrderAmount=[str(int(order.price)-100),'100'])
        self.assertSepOrder(sepOrder, order)

    # S2.货到付款待收货订单拆分订单(10单)
    def test_separateOrder_separat(self):
        order = createOrder(self.UserShop, self.Merch)
        sepOrder = self.wsDealMager.separateOrder(orderNo=order.orderNo, separateOrderAmount=[str(int(order.price)-100),'100'])
        self.assertSepOrder(sepOrder, order)

    # S3.只拆分一个订单

    # S4.还有未拆分的金额

    # S5.订单已取消

    # S6.订单已拆分

    # S7.订单已收货

    # S8.拆分开关关闭

    # S9.拆分金额小于门槛

    # S10.拆单次数超过最大次数

    # S11.不支持货到付款

    def assertSepOrder(self, rsp, order, sepTime=2):
        self.assertEqual(rsp.model['success'], '0')
        self.assertEqual(rsp.model['orderNo'], order.orderNo)
        self.assertEqual(len(rsp.model['paymentList']), sepTime)



def suite():
    suite=unittest.TestSuite()
    suite.addTest(separateOrder('test_separateOrder_separat'))
    return suite