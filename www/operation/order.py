#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
对订单的相关操作
"""

from www.common.webservice import *
from www.common.model import Shoppingcart
from www.common.other import Dict

# 提交订单 payWay=1在线支付 payWay=2货到付款
def createOrder(buyer, merch, merchCount='1',payWay='2'):
        ws = webservice()
        ws.login(buyer.username, buyer.password)
        ws.addShoppingcar(merchId=merch.goodsId, merchCount=merchCount, sellerId=merch.seller_store_id, sellerName=merch.sellerName)
        shopcart = Shoppingcart.find_first('where user_id = ? and goods_id = ?', buyer.userId,  merch.goodsId)
        invoice = {"invoiceId":buyer.invoiceId, "invoiceType":"N011","needInvoice":"0","invoiceHeader":buyer.invoiceHeader}
        deliverAddress = {"deliverAddress":buyer.deliverAddress, "deliverMobile":buyer.deliverMobile, "deliverPerson":buyer.deliverPerson}
        sellerList = []
        sellerList.append({"sellerId":merch.shopcartSellerId,"sellerName":merch.sellerName,"isYijipayAccount":merch.isYijipayAccount,"codFlag":merch.codFlag,
                           "supportVatInvoice":merch.supportVatInvoice,"comment":"createOrderByShoppingcart comment.","merchList":
                               [{"id":shopcart.id,"merchId":merch.goodsId,"merchBarCode":merch.productBarCode}]})
        order = ws.createOrderByShoppingcartNew(payWay=payWay,invoice=invoice, deliverAddress=deliverAddress, sellerList=sellerList)
        #returnOrder.ws = ws
        if order.model['createOrderInfoModel']['onlinePaymentModelList'] is not None:
                names = ['paymentNo', 'payType', 'totalPrice', 'orderNo', 'ws']
                values = [order.model['createOrderInfoModel']['onlinePaymentModelList'][0]['paymentNo'], order.model['createOrderInfoModel']['onlinePaymentModelList'][0]['payType'],
                          order.model['createOrderInfoModel']['onlinePaymentModelList'][0]['totalPrice'], order.model['createOrderInfoModel']['onlinePaymentModelList'][0]['orderNo'], ws]
                # returnOrder.paymentNo = order.model['createOrderInfoModel']['onlinePaymentModelList'][0]['paymentNo']
                # returnOrder.payType = order.model['createOrderInfoModel']['onlinePaymentModelList'][0]['payType']
                # returnOrder.totalPrice = order.model['createOrderInfoModel']['onlinePaymentModelList'][0]['totalPrice']
                # returnOrder.orderNo = order.model['createOrderInfoModel']['onlinePaymentModelList'][0]['orderNo']
                #returnOrder = Dict(names, values)
        elif order.model['createOrderInfoModel']['cashOnDeliveryModelList'] is not None:
                names = ['paymentNo', 'orderNo', 'price', 'ws']
                values = [order.model['createOrderInfoModel']['cashOnDeliveryModelList'][0]['paymentNo'], order.model['createOrderInfoModel']['cashOnDeliveryModelList'][0]['orderNo'],
                          order.model['createOrderInfoModel']['cashOnDeliveryModelList'][0]['price'], ws]
                #
                # returnOrder.paymentNo = order.model['createOrderInfoModel']['cashOnDeliveryModelList'][0]['paymentNo']
                # returnOrder.orderNo = order.model['createOrderInfoModel']['cashOnDeliveryModelList'][0]['orderNo']
                # returnOrder.price = order.model['createOrderInfoModel']['cashOnDeliveryModelList'][0]['price']
        return Dict(names, values)

# 取消订单