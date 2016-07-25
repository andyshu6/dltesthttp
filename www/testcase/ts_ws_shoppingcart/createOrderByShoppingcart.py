#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
0131.从购物车生成新订单
http://127.0.0.1:8280/mallws/shoppingcart/createOrderByShoppingcart.json
{
    "token": "e54d8c0d993543558062e52195c5c8d4",                        // 必须
    "couponList": [
		{                                                               // 可选优惠券
			"couponCode":"",                                            // 优惠券劵号
			"couponAmt":"",                                             // 优惠劵金额
			"couponUseAmt":"",                                          // 优惠券抵扣金额
		}
	],
    "deliverAddress": {                                                 // 收货地址模型
        "deliverAddress": "",                                           // 必须 收货地址
        "deliverMobile": "",                                            // 必须 电话
        "deliverPerson": ""                                             // 必须 收货人
    },
    "invoice": {                                                        // 发票模型
        "invoiceId": "",                                                // needInvoice-0 必须 needInvoice-1 不传
        "invoiceType": "",                                              // needInvoice-0 必须 needInvoice-1 不传 N011-普通发票 N012-增值税发票
        "needInvoice": ""                                               // 必须 0-需要发票 1-不要发票
		"invoiceHeader": ""                                             // 普通发票-必须 增值税发票-不需要
    },
    "payWay": "",                                                       // 必须 支付方式 1-在线支付 2-货到付款 12-混合支付 3-公司转帐
    "sellerList": [                                                     // 卖家模型
        {
            "sellerId": "7b632e29789d406595e93246fdb50fa4",             // 必须 卖家id
            "sellerName":"123",                                         // 必须 卖家名
			"isYijipayAccount": "0",                                    // 必须 卖家是否是易极付账户 0-是 1-不是
            "paymentFlag": "0",                                         // 必须 购物车接口的 paymentFlag
            "codFlag": "0",                                             // 必须 购物车接口的 codFlag
            "supportVatInvoice": "0",                                   // 必须 购物车接口的 supportVatInvoice
            "comment":"",                                               // 可选 留言
            "merchList": [                                              // 商品列表模型
                {
                    "id": "b8d8f93a5eae48b4a8918f741982d405",           // 必须 购物车主键
                    "merchId": "67d4cb03595348cdacd61000bc96ba03",      // 必须 商品id
                    "merchBarCode": "TM003",                            // 必须 商品条码
                    "promotionId": "",                                  // 可选 促销id
                    "promotionType":"",                                 // 可选 促销类型 0-满赠 1-满减
                    "reductionFlg":"",                                  // 可选 满减类型 0-减单价 1-减总额
                    "promotionDetail":""                                // 可选 促销详情
                    "ruleId":"123"                                      // 可选 规则
                }
            ]
        }
    ]
}

{
    "code": 200,
    "description": "执行成功!",
    "model": {
        "success":"0"                                       // 成功 0-成功 1-重复提交订单 2-校验失败 3-下单失败
        "failedReasons": {                                  // 去结算失败 返回的失败原因
            "lessThanMiniStartSaleQuantityList": [          // 商品数量小于最小起售量
                "商品名/店铺名"
            ],
            "delList": [                                    // 产品被删除 提示："以上商品不存在，无法购买"
                "商品名/店铺名"
            ],
            "invalidList": [                                // 无售卖权或无价格 提示："以上商品已失效，无法购买"
                "商品名/店铺名"
            ],
            "nameChangedList": [                            // 商品名称发生变化 提示："xx商品名称更改为xx商品    以上商品名称发生改变，请先查看最新信息"
                "商品名/店铺名"                             // 返回值为 : "xx商品名称更改为xx商品" 不用自己拼接 只用补最后一句
            ],
            "noInventoryList": [                            // 无库存 提示："以上商品暂时缺货，无法购买"
                "商品名/店铺名"
            ],
            "noOnHandInventoryList": [                      // 有库存但不足 提示："以上商品库存不足，请修改购买数量"
                "商品名/店铺名"
            ],
            "noSupplyInvoicList": [                         // 选择需要结算的商品对应的配送商如果由支持"开增值税发票"变为不支持 提示："以上配送商不再支持开增值税票，请查看最新信息"
                "商品名/店铺名"
            ],
            "priceChangedList": [                           // 价格变动 提示："以上商品价格变动，请先查看最新价格"
                "商品名/店铺名"
            ],
            "shelvesOffList": [                             // 平台或卖家操作下架（或锁定） 提示："以上商品已下架，无法购买"
                "商品名/店铺名"
            ],
            "specChangedList": [                            // 商品规格发生变化 提示："xx商品规格由x更改为x 以上商品规格发生改变，请先查看最新信息"
                "商品名/店铺名"                             // 返回值为："xx商品规格由x更改为x" 不用自己拼接 只用补最后一句
            ],
            "supplyCodPaymentChangedList": [                // 支付方式变化（增加或取消货到付款） 提示："以上配送商支付方式发生变动，请先查看最新信息"
                "商品名/店铺名"
            ],
			"couponCodeStateChangedList": [                 // 优惠劵发生变化（过期或不可用） 提示："xxx优惠券状态发生改变，已失效，请查看最新消息！"
                "优惠劵信息"
            ],
			"couponErrorMessage": "红包状态异常"

        },
        "createOrderInfoModel": {                               // 数据验证成功模型
            "leftShoppingcartSize":"0",                         // 购物车剩余商品类型数量
            "onlinePaymentModel": {                             // 在线支付订单模型
                "paymentNo":"123",                              // 大订单号
                "payType":"123",                                // 支付类型
                "totalPrice":"123",                             // 总价
                "orderNoList": [                                // 子订单号列表
                    "123"
                ]
            },
            "cashOnDeliveryModelList": [                        // 货到付款订单模型
                {
                    "paymentNo":"123",                          // 大订单号
                    "orderNo":"123",                            // 子订单号
                    "price":"123"                               // 总价
                }
            ]
        }
    },
    "metadata": {
        "type": 0,
        "clazz": "cn.com.hd.mall.web.webservices.entity.response.shoppingcart.CreateOrderResponse"
    }
}

参数校验:
    // 只做必须验证
code说明:
    100-token失效 200-成功 300-错误的角色(无权限) 400-非法的参数 500-服务器异常 600-重新登陆
param说明:
    发票模型中 如果开发票 则needInvoice为0 invoiceId/invoiceType必传 如果不开发票 needInvoice为1 invoiceId/invoiceType不传
result说明:
    当success字段为0时 createOrderInfoModel模型有值 当success字段为1时 两个大模型都没有值 当success为2时 failedReasons模型有值 当success为3时 下单失败
    onlinePaymentModel/cashOnDeliveryModelList如果无值 返回null
"""

import unittest
from www.common.webservice import *
from www.common.excel import eData
from www.common.database import update
from www.common.model import Shoppingcart

class createOrderByShoppingcart(unittest.TestCase):

    UserShop = eData('TmlShop')
    UserShop2 = eData('TmlShop2')
    Merch1 = eData('Merch1')
    Merch2 = eData('Merch2')
    Merch4 = eData('Merch4')

    # S1.提交活动付款订单
    def test_createOrderByShoppingcart_one(self):
        ws = webservice()
        ws.login(self.UserShop2.username, self.UserShop2.password)
        ws.addShoppingcar(merchId=self.Merch1.goodsId, merchCount='1', sellerId=self.Merch1.seller_store_id, sellerName=self.Merch1.sellerName)
        shopcart = Shoppingcart.find_first('where user_id = ? and goods_id = ?', self.UserShop2.userId, self.Merch1.goodsId)
        invoice = {"invoiceId":self.UserShop.invoiceId, "invoiceType":"N011","needInvoice":"0","invoiceHeader":self.UserShop.invoiceHeader}
        deliverAddress = {"deliverAddress":self.UserShop.deliverAddress, "deliverMobile":self.UserShop.deliverMobile, "deliverPerson":self.UserShop.deliverPerson}
        sellerList = []
        sellerList.append({"sellerId":self.Merch1.shopcartSellerId,"sellerName":self.Merch1.sellerName,"isYijipayAccount":self.Merch1.isYijipayAccount,"codFlag":self.Merch1.codFlag,
                           "supportVatInvoice":self.Merch1.supportVatInvoice,"comment":"createOrderByShoppingcart comment.","merchList":
                               [{"id":shopcart.id,"merchId":self.Merch1.goodsId,"merchBarCode":self.Merch1.productBarCode,
                                 }]})
        order = ws.createOrderByShoppingcart(payWay='2',invoice=invoice, deliverAddress=deliverAddress, sellerList=sellerList)
        self.assertEqual(order.model['success'], '0')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(createOrderByShoppingcart("test_createOrderByShoppingcart_one"))
    return suite