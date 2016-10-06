#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
0255.获取订单跟踪信息
http://127.0.0.1:8280/mallws/orders/getOrderLog.json
{
    "token": "57469529686440a88fedb0bed51ba5d0",        // 必须 token
    "orderNo":"123123123"                               // 必须 订单号
}

{
    "code": 200,
    "description": "执行成功!",
    "model": {
        "success": "0",                                 // 成功 0-成功 1-失败
        "orderLogList": [
			{
				"beforeStatus": "xx",                   // 订单之前的状态
				"dealDescrip": "xx",					// 订单操作说明
				"nowStatus": "xx",						// 订单当前状态
				"dealDate": "xx"						// 操作时间
			}
		]
    },
    "metadata": {
        "type": 0,
        "clazz": "cn.com.hd.mall.web.webservices.entity.response.order.OrderLogResponse"
    }
}

参数校验:
    只做必须验证
code说明:
    100-token失效 200-成功 300-错误的角色(无权限) 400-非法的参数 500-服务器异常 600-重新登陆
"""

import unittest
from www.common.webservice import *
from www.common.excel import eData
from www.operation.order import createOrder

class getOrderLog(unittest.TestCase):
    UserShop = eData('TmlShop')
    UserShopMin = eData('TmlShopMin')
    DealMgr = eData('DealMager')
    DealMgr2 = eData('DealMager2')
    DealSaler = eData('DealSaler')
    DealBuyer = eData('DealBuyer')
    Merch1 = eData('Merch1')


    #order = createOrder(UserShop, Merch1)

    # S1.货到付款提交订单获取订单跟踪消息
    def test_getOrderLog_createOrder(self):
        order = createOrder(self.UserShop, self.Merch1)
        ws = webservice()
        ws.login(self.UserShop.username, self.UserShop.password)
        orderLog = ws.getOrderLog(order.orderNo)
        self.assertEqual(orderLog['model']['success'], '0')
        self.assertEqual(orderLog['model']['orderLogList'][0]['beforeStatus'], '')
        self.assertIsNotNone(orderLog['model']['orderLogList'][0]['dealDate'])
        self.assertEqual(orderLog['model']['orderLogList'][0]['dealDescrip'], u'提交订单')
        self.assertEqual(orderLog['model']['orderLogList'][0]['nowStatus'], 'C020')

    # S2.货到付款取消订单获取订单跟踪消息
    def test_getOrderLog_cancelOrder(self):
        order = createOrder(self.UserShop, self.Merch1)
        order.ws.cancel(paymentNo=order.paymentNo)
        orderLog = order.ws.getOrderLog(order.orderNo)
        self.assertEqual(orderLog['model']['success'], '0')
        flag = 0
        for i in range(0,len(orderLog['model']['orderLogList'])):
            if orderLog['model']['orderLogList'][i]['beforeStatus'] == 'C020':
                self.assertIsNotNone(orderLog['model']['orderLogList'][i]['dealDate'])
                self.assertEqual(orderLog['model']['orderLogList'][i]['dealDescrip'], u'交易已取消')
                self.assertEqual(orderLog['model']['orderLogList'][i]['nowStatus'], 'C012')
                flag += 1
        self.assertEqual(flag, 1, 'cancel order log is not found or is found twice')


    # S3.货到付款订单发货获取订单跟踪消息
    def test_getOrderLog_deliverOrder(self):
        order = createOrder(self.UserShop, self.Merch1)
        ws = webservice()
        ws.login(self.DealMgr.username, self.DealMgr.password)
        ws.deliver(orderNo=order.orderNo)
        orderLog = order.ws.getOrderLog(order.orderNo)
        self.assertEqual(orderLog['model']['success'], '0')
        flag = 0
        for i in range(0,len(orderLog['model']['orderLogList'])):
            if orderLog['model']['orderLogList'][i]['beforeStatus'] == 'C020':
                self.assertIsNotNone(orderLog['model']['orderLogList'][i]['dealDate'])
                self.assertEqual(orderLog['model']['orderLogList'][i]['dealDescrip'], u'卖家发货')
                self.assertEqual(orderLog['model']['orderLogList'][i]['nowStatus'], 'C017')
                flag += 1
        self.assertEqual(flag, 1, 'cancel order log is not found or is found twice')

    # S4.货到付款订单交易完成订单跟踪消息

    # S5.订单改价获取订单跟踪消息——暂时不会记录订单跟踪
    def test_getOrderLog_changPrice(self):
        order = createOrder(self.UserShop, self.Merch1)
        ws = webservice()
        ws.login(self.DealMgr.username, self.DealMgr.password)
        ws.changeOrderPrice(orderNo=order.orderNo, orderDiscountAmount='100', orderChangeAmount='11900', orderStatus='C020')
        ws.deliver(orderNo=order.orderNo)
        orderLog = order.ws.getOrderLog(order.orderNo)
        self.assertEqual(orderLog['model']['success'], '0')
        flag = 0
        for i in range(0,len(orderLog['model']['orderLogList'])):
            if orderLog['model']['orderLogList'][i]['beforeStatus'] == 'C020':
                self.assertIsNotNone(orderLog['model']['orderLogList'][i]['dealDate'])
                self.assertEqual(orderLog['model']['orderLogList'][i]['dealDescrip'], u'卖家发货')
                self.assertEqual(orderLog['model']['orderLogList'][i]['nowStatus'], 'C017')
                flag += 1
        self.assertEqual(flag, 1, 'cancel order log is not found or is found twice')

    # S6.待收货订单取消后拒绝取消、同意取消订单跟踪
    def test_getOrderLog_cancelAudit(self):
        order = createOrder(self.UserShop, self.Merch1)
        ws = webservice()
        ws.login(self.DealMgr.username, self.DealMgr.password)
        ws.deliver(orderNo=order.orderNo)
        order.ws.cancel(paymentNo=order.paymentNo, cancelType='3')
        ws.auditCancel(paymentNo=order.paymentNo, orderNo=order.orderNo, auditStatus='1')
        order.ws.cancel(paymentNo=order.paymentNo, cancelType='3')
        ws.auditCancel(paymentNo=order.paymentNo, orderNo=order.orderNo, auditStatus='0')
        orderLog = order.ws.getOrderLog(order.orderNo)
        self.assertEqual(orderLog['model']['success'], '0')
        flagCancel = 0
        flagReject = 0
        flagAgree = 0
        for i in range(0,len(orderLog['model']['orderLogList'])):
            if orderLog['model']['orderLogList'][i]['dealDescrip'] == u'交易取消中':
                self.assertEqual(orderLog['model']['orderLogList'][i]['beforeStatus'], 'C017')
                self.assertIsNotNone(orderLog['model']['orderLogList'][i]['dealDate'])
                self.assertEqual(orderLog['model']['orderLogList'][i]['nowStatus'], 'C017')
                flagCancel += 1
                continue
            if orderLog['model']['orderLogList'][i]['dealDescrip'] == u'卖家拒绝取消':
                self.assertEqual(orderLog['model']['orderLogList'][i]['beforeStatus'], 'C017')
                self.assertIsNotNone(orderLog['model']['orderLogList'][i]['dealDate'])
                self.assertEqual(orderLog['model']['orderLogList'][i]['nowStatus'], 'C017')
                flagReject += 1
                continue
            if orderLog['model']['orderLogList'][i]['dealDescrip'] == u'交易已取消':
                self.assertEqual(orderLog['model']['orderLogList'][i]['beforeStatus'], 'C017')
                self.assertIsNotNone(orderLog['model']['orderLogList'][i]['dealDate'])
                self.assertEqual(orderLog['model']['orderLogList'][i]['nowStatus'], 'C012')
                flagAgree += 1
                continue
        self.assertEqual(flagCancel, 2, order.orderNo + 'cancel time is wrong!')
        self.assertEqual(flagReject, 1, order.orderNo + 'cancel reject time is wrong!')
        self.assertEqual(flagAgree, 1, order.orderNo + 'cancel agree time is wrong!')

    # S7.在线支付提交订单获取订单跟踪
    def test_getOrderLog_createOrderOnline(self):
        order = createOrder(self.UserShop, self.Merch1, payWay='1')
        orderLog = order.ws.getOrderLog(order.orderNo)
        self.assertEqual(orderLog['model']['success'], '0')
        self.assertEqual(orderLog['model']['orderLogList'][0]['beforeStatus'], '')
        self.assertIsNotNone(orderLog['model']['orderLogList'][0]['dealDate'])
        self.assertEqual(orderLog['model']['orderLogList'][0]['dealDescrip'], u'提交订单')
        self.assertEqual(orderLog['model']['orderLogList'][0]['nowStatus'], 'C011')

    # S8.在线支付取消订单订单获取订单跟踪
    def test_getOrderLog_cancelOrderOnline(self):
        order = createOrder(self.UserShop, self.Merch1, payWay='1')
        order.ws.cancel(paymentNo=order.paymentNo, payType='1', cancelType='1')
        orderLog = order.ws.getOrderLog(order.orderNo)
        flag = 0
        for i in range(0,len(orderLog['model']['orderLogList'])):
            if orderLog['model']['orderLogList'][i]['beforeStatus'] == 'C011':
                self.assertIsNotNone(orderLog['model']['orderLogList'][i]['dealDate'])
                self.assertEqual(orderLog['model']['orderLogList'][i]['dealDescrip'], u'交易已取消')
                self.assertEqual(orderLog['model']['orderLogList'][i]['nowStatus'], 'C012')
                flag += 1
        self.assertEqual(flag, 1, order.orderNo + 'cancel order log is not found or is found twice')

    # S9.在线支付付款获取订单跟踪

    # S10.在线支付发货获取订单跟踪

    # S11.在线支付确认收货获取订单跟踪


def suite():
    suite = unittest.TestSuite()
    suite.addTest(getOrderLog("test_getOrderLog_createOrder"))
    suite.addTest(getOrderLog("test_getOrderLog_cancelOrder"))
    suite.addTest(getOrderLog("test_getOrderLog_deliverOrder"))
    #suite.addTest(getOrderLog("test_getOrderLog_changPrice"))
    suite.addTest(getOrderLog("test_getOrderLog_cancelAudit"))
    suite.addTest(getOrderLog("test_getOrderLog_createOrderOnline"))
    suite.addTest(getOrderLog("test_getOrderLog_cancelOrderOnline"))
    return suite