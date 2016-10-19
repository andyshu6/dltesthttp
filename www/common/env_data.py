#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
初始化基础数据
"""

from www.operation.order import createOrder, codPay
from www.common.excel import eData, write_excel
from www.common.database import create_engine, update
from www.common.webservice import *

def initOrder():
    UserShop = eData('TmlShop')
    Merch = eData('Merch1')
    #Merch4 = eData('Merch4')
    DealMgr = eData('DealMager')

    ws = webservice()
    ws.login(DealMgr.username, DealMgr.password)

    #在线支付待付款订单(C011)
    orderOnlineWaitPay = createOrder(UserShop, Merch, payWay='1')
    orderOnlineWaitPay.pop('ws')
    write_excel(sheetname='TmlShop', rowkey='orderOnlineWaitPay', rowvalue=str(orderOnlineWaitPay))
    import datetime
    update('update dlorder.dl_order_orderinfo SET gmt_created = ? WHERE order_no = ?', datetime.datetime.strptime('2099-01-01 00:00:00', "%Y-%m-%d %H:%M:%S"), orderOnlineWaitPay.orderNo)

    #在线支付待发货订单
    #在线支付待收货订单
    #在线支付交易完成订单

    #在线支付已取消订单（C012）
    orderOnlienCancel = createOrder(UserShop, Merch, payWay='1')
    orderOnlienCancelWS = orderOnlienCancel.pop('ws')
    write_excel(sheetname='TmlShop', rowkey='orderOnlienCancel', rowvalue=str(orderOnlienCancel))
    orderOnlienCancelWS.cancel(paymentNo=orderOnlienCancel.paymentNo, payType='1', cancelType='1')

    #货到付款待发货订单（C020）
    orderCodWaitDeliver = createOrder(UserShop, Merch)
    orderCodWaitDeliver.pop('ws')
    write_excel(sheetname='TmlShop', rowkey='orderCodWaitDeliver', rowvalue=str(orderCodWaitDeliver))

    #货到付款待收货订单（C017）
    orderCodWaitReceive = createOrder(UserShop, Merch)
    orderCodWaitReceive.pop('ws')
    write_excel(sheetname='TmlShop', rowkey='orderCodWaitReceive', rowvalue=str(orderCodWaitReceive))
    ws.deliver(orderNo=orderCodWaitReceive.orderNo)

    #货到付款已完成订单(C019)
    orderCodComplete = createOrder(UserShop, Merch)
    orderCodComplete.pop('ws')
    write_excel(sheetname='TmlShop', rowkey='orderCodComplete', rowvalue=str(orderCodComplete))
    ws.deliver(orderNo=orderCodComplete.orderNo)
    codPay(orderNo=orderCodComplete.orderNo)

    #货到付款已取消订单（C012）
    orderCodCancel = createOrder(UserShop, Merch)
    orderCodCancelWS = orderCodCancel.pop('ws')
    write_excel(sheetname='TmlShop', rowkey='orderCodCancel', rowvalue=str(orderCodCancel))
    orderCodCancelWS.cancel(paymentNo=orderCodCancel.paymentNo)

    #经销商管理员下货到付款订单待发货
    # orderDealCodWaitDeliver = createOrder(DealMgr, Merch4, payWay='1')
    # write_excel(sheetname='DealMager', rowkey='orderCodWaitDeliver', rowvalue=str(orderDealCodWaitDeliver))



if __name__ == '__main__':
    create_engine()
    initOrder()