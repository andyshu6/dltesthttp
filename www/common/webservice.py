#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2016年4月19日

@author: Roy
'''
from www.common.httpbase import *
import hashlib
import logging


class webservice:
    # httpEngine

    def __init__(self):
        self.wrapHttpBase = httpbase()

    def doLogin(self, username, password, token = None):
        password = hashlib.md5(password).hexdigest()
        url = '/login/doLogin.json'
        data = {}
        data['username'] = username
        data['password'] = password
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    def login(self, username, password, token = 'null'):
        password = hashlib.md5(password).hexdigest()
        url = '/login/login.json'
        data = {}
        data['username'] = username
        data['password'] = password
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body



    # ——————————————————    共通  ————————————————————
    # 0233.比较应用版本信息（未登录也可检测）
    def compareAppVersion(self, clientVersion, osCode, equipmentCode, appType, token = None):
        url = '/common/version/compareAppVersion.json'
        data = {}
        data['clientVersion'] = clientVersion
        data['osCode'] = osCode
        data['equipmentCode'] = equipmentCode
        data['appType'] = appType
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0230.获取所有区域列表
    def getAllAreaList(self,token=None):
        url = '/common/area/getAllAreaList.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0231.选择获取区域列表
    def getAreaListByCondition(self, provinceCode=None, cityCode=None, token=None):
        url = '/common/area/getAreaListByCondition.json'
        data = {}
        if provinceCode is not None:
            data['provinceCode'] = provinceCode
        if cityCode is not None:
            data['cityCode'] = cityCode
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 获取指定区域列表
    def getAreaListStandAlone(self, provinceCode=None, cityCode=None, token=None):
        url = '/common/area/getAreaListStandAlone.json'
        data = {}
        if provinceCode is not None:
            data['provinceCode'] = provinceCode
        if cityCode is not None:
            data['cityCode'] = cityCode
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0254.获取用户协议URL
    def userAgreementUrl(self, token='null'):
        url = '/common/url/userAgreementUrl.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0281.获取平台参数
    def getCouponParam(self,token=None):
        url = '/common/param/getCouponParam.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0286.获取Banner图片地址
    def getBannerList(self,token=None):
        url = '/common/pic/getBannerList.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0287.获取主题列表（品类及其他）
    def getTopicList(self, token=None):
        url = '/common/pic/getTopicList.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body



    def getCategoryList(self, merchCategoryCode):
        url = '/merch/getCategoryList.json'
        data = {}
        data['merchCategoryCode'] = merchCategoryCode
        return self.wrapHttpBase.post(url, data)





    # ——————————————————    我的丹露  ————————————————————
    # 0010.修改密码
    def modiyfPassword(self, oldPassword=None, newPassword=None, token=None):
        oldPassword = hashlib.md5(oldPassword).hexdigest()
        newPassword = hashlib.md5(newPassword).hexdigest()
        url = '/mydl/password/modifyPassword.json'
        data = {}
        if oldPassword is not None:
            data['oldPassword'] = oldPassword
        if newPassword is not None:
            data['newPassword'] = newPassword
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body


    # ——————————————————    发票  ————————————————————
    # 0200.添加发票
    def addInvoice(self, invoiceType='N011', invoiceHeader=None, companyName=None, taxpayerRegistrationNumber=None, registerAddress=None, registerTel=None,
                   depositBank=None, accountBank=None, receiveManName=None, receiveManTel=None, receiveManProvince=None, receiveManAddress=None, token=None):
        url = '/mydl/invoice/addInvoice.json'
        data = {}
        data['invoice'] = {}
        if(invoiceType=='N011'):
            data['invoice']['invoiceType'] = 'N011'
            data['invoice']['invoiceHeader'] = invoiceHeader
        elif(invoiceType=='N012'):
            data['invoice']['invoiceType'] = 'N012'
            data['invoice']['companyName'] = companyName
            data['invoice']['taxpayerRegistrationNumber'] = taxpayerRegistrationNumber
            data['invoice']['registerAddress'] = registerAddress
            data['invoice']['registerTel'] = registerTel
            data['invoice']['depositBank'] = depositBank
            data['invoice']['accountBank'] = accountBank
            data['invoice']['receiveManName'] = receiveManName
            data['invoice']['receiveManTel'] = receiveManTel
            data['invoice']['receiveManProvince'] = receiveManProvince
            data['invoice']['receiveManAddress'] = receiveManAddress
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0201.删除发票
    def delInvoice(self, invoiceId, token=None):
        url = '/mydl/invoice/delInvoice.json'
        data = {}
        data['invoiceId'] = invoiceId
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0202.修改发票
    def modifyInvoice(self, invoiceId, invoiceType='N011', invoiceHeader=None, companyName=None, taxpayerRegistrationNumber=None, registerAddress=None, registerTel=None,
                   depositBank=None, accountBank=None, receiveManName=None, receiveManTel=None, receiveManProvince=None, receiveManAddress=None, token=None):
        url = '/mydl/invoice/modifyInvoice.json'
        data = {}
        data['invoice'] = {}
        data['invoice']['invoiceId'] = invoiceId
        if(invoiceType=='N011'):
            data['invoice']['invoiceType'] = 'N011'
            data['invoice']['invoiceHeader'] = invoiceHeader
        elif(invoiceType=='N012'):
            data['invoice']['invoiceType'] = 'N012'
            data['invoice']['companyName'] = companyName
            data['invoice']['taxpayerRegistrationNumber'] = taxpayerRegistrationNumber
            data['invoice']['registerAddress'] = registerAddress
            data['invoice']['registerTel'] = registerTel
            data['invoice']['depositBank'] = depositBank
            data['invoice']['accountBank'] = accountBank
            data['invoice']['receiveManName'] = receiveManName
            data['invoice']['receiveManTel'] = receiveManTel
            data['invoice']['receiveManProvince'] = receiveManProvince
            data['invoice']['receiveManAddress'] = receiveManAddress
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0203.设置默认发票
    def setDefaultInvoice(self, invoiceId, token=None):
        url = '/mydl/invoice/setDefaultInvoice.json'
        data = {}
        data['invoiceId'] = invoiceId
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0204.发票列表
    def getInvoiceList(self, token = None):
        url = '/mydl/invoice/getInvoiceList.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body


    # ——————————————————    商品接口  ————————————————————
    # 0036.获取品牌属性列表
    def getCategoryList(self, merchCategoryCode = 'C01L0101', token=None):
        url = '/merch/getCategoryList.json'
        data = {}
        if(merchCategoryCode is not None):
            data['merchCategoryCode'] = merchCategoryCode
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0037.获取商品列表
    def getMerchList(self, merchName=None, merchCategoryCode=None, merchPropertyValueCodeList=None, merchBrandId=None, sellerId=None, lowPrice=None, highPrice=None, sortField=0, sortType=0, page=1, rows=15, token=None):
        url = '/merch/getMerchList.json'
        data = {}
        if merchName is not None:
            data['merchName'] = merchName
        if merchCategoryCode is not None:
            data['merchCategoryCode'] = merchCategoryCode
        if merchPropertyValueCodeList is not None:
            data['merchPropertyValueCodeList'] = merchPropertyValueCodeList
        if merchBrandId is not None:
            data['merchBrandId'] = merchBrandId
        if sellerId is not None:
            data['sellerId'] = sellerId
        if lowPrice is not None:
            data['lowPrice'] = lowPrice
        if highPrice is not None:
            data['highPrice'] = highPrice
        if sortField is not None:
            data['sortField'] = sortField
        if sortType is not None:
            data['sortType'] = sortType
        if page is not None:
            data['page'] = page
        if rows is not None:
            data['rows'] = rows
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0038.获取商品详情
    def getMerchDetail(self, merchId, token=None):
        url = '/merch/getMerchDetail.json'
        data = {}
        data['merchId'] = merchId
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0037.获取商品列表(New)
    def getNewMerchList(self, merchName=None, merchCategoryCode=None, merchPropertyValueCodeList=None, merchBrandId=None, sellerId=None, lowPrice=None, highPrice=None, sortField=0, sortType=0, page=1, rows=15, token=None):
        url = '/merch/getNewMerchList.json'
        data = {}
        if merchName is not None:
            data['merchName'] = merchName
        if merchCategoryCode is not None:
            data['merchCategoryCode'] = merchCategoryCode
        if merchPropertyValueCodeList is not None:
            data['merchPropertyValueCodeList'] = merchPropertyValueCodeList
        if merchBrandId is not None:
            data['merchBrandId'] = merchBrandId
        if sellerId is not None:
            data['sellerId'] = sellerId
        if lowPrice is not None:
            data['lowPrice'] = lowPrice
        if highPrice is not None:
            data['highPrice'] = highPrice
        if sortField is not None:
            data['sortField'] = sortField
        if sortType is not None:
            data['sortType'] = sortType
        if page is not None:
            data['page'] = page
        if rows is not None:
            data['rows'] = rows
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body


    # 0038.获取商品详情
    def getNewMerchDetail(self, merchId, token=None):
        url = '/merch/getNewMerchDetail.json'
        data = {}
        data['merchId'] = merchId
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0039.获取丹露促销商品列表
    def getPromotionList(self, page=1, rows=4, token=None):
        url = '/merch/getPromotionList.json'
        data = {}
        data['page'] = page
        data['rows'] = rows
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0040.获取丹露推荐商品列表
    def getRecommendList(self, page=1, rows=4, token=None):
        url = '/merch/getRecommendList.json'
        data = {}
        data['page'] = page
        data['rows'] = rows
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0041.获取我的常购商品列表
    def getOftenBuyList(self, saleFlag=0, page=1, rows=4, token=None):
        url = '/merch/getOftenBuyList.json'
        data = {}
        data['saleFlag'] = saleFlag
        data['page'] = page
        data['rows'] = rows
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body


    # ——————————————————    购物车接口  ————————————————————
    # 0039.添加商品到购物车
    def addShoppingcar(self, merchId, merchCount, sellerId, sellerName, token=None):
        url = '/shoppingcart/addShoppingcart.json'
        data = {}
        if merchId is not None:
            data['merchId'] = merchId
        if merchCount is not None:
            data['merchCount'] = merchCount
        if sellerId is not None:
            data['sellerId'] = sellerId
        if sellerName is not None:
            data['sellerName'] = sellerName
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0040.修改指定商品在购物车中的数量
    def modifyShoppingcartCount(self, shoppingCartId, merchId, merchCount, sellerId, usePromotion, promotionId=None, promotionType=None, reductionType=None, ruleId=None, token=None):
        url = '/shoppingcart/modifyShoppingcartCount.json'
        data = {}
        if shoppingCartId is not None:
            data['shoppingCartId'] = shoppingCartId
        if merchId is not None:
            data['merchId'] = merchId
        if merchCount is not None:
            data['merchCount'] = merchCount
        if sellerId is not None:
            data['sellerId'] = sellerId
        if usePromotion is not None:
            data['usePromotion'] = usePromotion
        if promotionId is not None:
            data['promotionId'] = promotionId
        if promotionType is not None:
            data['promotionType'] = promotionType
        if reductionType is not None:
            data['reductionType'] = reductionType
        if ruleId is not None:
            data['ruleId'] = ruleId
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body


    # 0041.获取购物车中的商品信息
    def toShoppingcart(self, token=None):
        url = '/shoppingcart/toShoppingcart.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0042.删除购物车中的商品信息
    def delShoppingcartByProductIds(self, delList, token=None):
        url = '/shoppingcart/delShoppingcartByProductIds.json'
        data = {}
        data['delList'] = delList
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0045.获取购物车商品数量
    def getShoppingcartSize(self, token=None):
        url = '/shoppingcart/getShoppingcartSize.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0130.获取确认订单信息
    def getPreViewOrderByShoppingcart(self, toSettlementModel=None, token=None):
        url = '/shoppingcart/getPreViewOrderByShoppingcart.json'
        data = {}
        data['toSettlementModel'] = []
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0131.从购物车生成新订单
    def createOrderByShoppingcart(self,payWay=None, couponList=None, deliverAddress=None, invoice=None, sellerList=None, token=None):
        url = '/shoppingcart/createOrderByShoppingcart.json'
        data = {}
        data['payWay'] = payWay
        if couponList is not None:
            data['couponList'] = couponList
        data['deliverAddress'] = deliverAddress
        if invoice is not None:
            data['invoice'] = invoice
        data['sellerList'] = sellerList
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 检查是否需要弹出后续的验证信息
    def checkSwitch(self, token=None):
        url = '/shoppingcart/checkSwitch.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 发送短信验证码
    def sendMessage(self, tel=None, token=None):
        url = '/shoppingcart/sendMessage.json'
        data = {}
        if tel is not None:
            data['tel'] = tel
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 提交订单（新）
    def createOrderByShoppingcartNew(self,payWay=None, verfyCode=None, couponList=None, deliverAddress=None, invoice=None, sellerList=None, token=None):
        url = '/shoppingcart/createOrderByShoppingcart.json'
        data = {}
        if verfyCode is not None:
            data['verfyCode'] = verfyCode
        data['payWay'] = payWay
        if couponList is not None:
            data['couponList'] = couponList
        data['deliverAddress'] = deliverAddress
        if invoice is not None:
            data['invoice'] = invoice
        data['sellerList'] = sellerList
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # -----------------------------------订单接口-----------------------------------------------------
    # 0040.获取买家订单的数量
    def getBuyerOrderCount(self, token=None):
        url='/orders/getBuyerOrderCount.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0050.获取卖家订单的数量
    def getSellerOrderCount(self, token=None):
        url='/orders/getSellerOrderCount.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body


    # 0181.订单发货
    def deliver(self, orderNo=None, token=None):
        url='/orders/oper/deliver.json'
        data = {}
        data['orderNo']=orderNo
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0182.订单收货
    def receive(self, paymentNo=None, orderNo=None, payType=None, token=None):
        url='/orders/oper/receive.json'
        data = {}
        data['paymentNo']=paymentNo
        data['orderNo']=orderNo
        data['payType']=payType
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body


    # 0183.订单取消
    def cancel(self, paymentNo=None, payType='2', cancelType='2',token=None):
        url='/orders/oper/cancel.json'
        data = {}
        data['paymentNo']=paymentNo
        data['payType']=payType
        data['cancelType']=cancelType
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0184.订单取消审批
    def auditCancel(self, paymentNo=None, orderNo=None, auditStatus='0', token=None):
        url='/orders/oper/auditCancel.json'
        data = {}
        data['paymentNo']=paymentNo
        data['orderNo']=orderNo
        data['auditStatus']=auditStatus
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body


    # 0185.获取订单改价页面展示信息
    def getChangeOrderPricePage(self,orderNo=None,token=None):
         url='/orders/toChangeOrderPricePage.json'
         data={}
         data['orderNo']=orderNo
         self.wrapHttpBase.post(url, data, token)
         return self.wrapHttpBase.body

    # 0186.订单改价操作
    def changeOrderPrice(self,orderNo=None,orderDiscountAmount=None,orderChangeAmount=None,orderStatus=None,token=None):
        url='/orders/oper/changeOrderPrice.json'
        data = {}
        data['orderNo']=orderNo
        data['orderDiscountAmount']=orderDiscountAmount
        data['orderChangeAmount']=orderChangeAmount
        data['orderStatus']=orderStatus
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body


    # ——————————————————    注册接口  ————————————————————
    # 0242.获取店铺类型列表
    def getTerminalShopTypeList(self, token='null'):
        url = '/regist/getTerminalShopTypeList.json'
        data = {}
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0243.获取终端店地区列表
    def getArea(self, search, token='null'):
        url = '/regist/getArea.json';
        data = {}
        if search is not None:
            data['search'] = search
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body

    # 0245.获取短信验证码
    def getValidateCode(self, tel, token='null'):
        url = '/regist/getValidateCode.json';
        data = {}
        if tel is not None:
            data['tel'] = tel
        self.wrapHttpBase.post(url, data, token)
        return self.wrapHttpBase.body


    # ----------------------------------  收货地址接口  ----------------------------------------------
    #添加收货地址
    def addDeliverAddress(self,areaProvinceCode=None,areaCityCode=None,areaDistrictCode=None,addressDetail=None,zipCode=None,deliverPerson=None,deliverMobile=None,deliverTel=None,isDefault=None,token=None):
        url = '/mydl/deliverAddress/addDeliverAddress.json'
        data = {}
        data['deliverAddress'] = {}
        data['deliverAddress']['areaProvinceCode'] = areaProvinceCode
        data['deliverAddress']['areaCityCode'] = areaCityCode
        data['deliverAddress']['areaDistrictCode'] = areaDistrictCode
        data['deliverAddress']['addressDetail'] = addressDetail
        data['deliverAddress']['zipCode'] = zipCode
        data['deliverAddress']['deliverPerson'] = deliverPerson
        data['deliverAddress']['deliverMobile'] = deliverMobile
        data['deliverAddress']['deliverTel'] = deliverTel
        data['deliverAddress']['isDefault'] = isDefault
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #获取收货地址列表
    def getDeliverAddressList(self,token=None):
        url='/mydl/deliverAddress/getDeliverAddressList.json'
        data={}
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #删除收货地址
    def delDeliverAddress(self,token=None,deliverAddressId=None):
        url='/mydl/deliverAddress/delDeliverAddress.json'
        data={}
        data['deliverAddressId']=deliverAddressId
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #修改收货地址
    def modifyDeliverAddress(self,addressId=None,addressDetail=None,areaProvinceCode=None,areaCityCode=None,areaDistrictCode=None,zipCode=None,deliverPerson=None,deliverMobile=None,deliverTel=None,token=None):
        url='/mydl/deliverAddress/modifyDeliverAddress.json'
        data={}
        data['deliverAddress']={}
        data['deliverAddress']['addressId']=addressId
        data['deliverAddress']['addressDetail']=addressDetail
        data['deliverAddress']['areaProvinceCode']=areaProvinceCode
        data['deliverAddress']['areaCityCode']=areaCityCode
        data['deliverAddress']['areaDistrictCode']=areaDistrictCode
        data['deliverAddress']['zipCode']=zipCode
        data['deliverAddress']['deliverPerson']=deliverPerson
        data['deliverAddress']['deliverMobile']=deliverMobile
        data['deliverAddress']['deliverTel']=deliverTel
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #设置默认收货地址
    def setDefaultDeliverAddress(self,deliverAddressId=None,token=None):
        url='/mydl/deliverAddress/setDefaultDeliverAddress.json'
        data={}
        data['deliverAddressId']=deliverAddressId
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #获取终端店地址
    def getTerminalAddress(self,terminalCustomerId=None,token=None):
        url='/mydl/deliverAddress/getTerminalAddress.json'
        data={}
        data['terminalCustomerId']=terminalCustomerId
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body


    # -----------------------------------收藏接口-----------------------------------------------------
    #添加收藏
    def addFavorite(self,merchId=None,token=None):
        url='/mydl/favorites/addFavorite.json'
        data={}
        data['merchId']=merchId
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #删除收藏（支持批量删除）
    def delFavorite(self,merchId=None,token=None):
        url='/mydl/favorites/delFavorite.json'
        data={}
        data['merchId']=merchId
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #获取收藏列表
    def getFavoriteList(self,page=None,rows=None,token=None):
        url='/mydl/favorites/getFavoriteList.json'
        data={}
        data['page']=page
        data['rows']=rows
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #获取收藏列表数量
    def getFavoriteListSize(self,token=None):
        url='/mydl/favorites/getFavoriteListSize.json'
        data={}
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body


    #----------------------------------账号接口----------------------------------------------------------
    #获取企业信息
    def getCompanyInfo(self,companyId=None,token=None):
        url='/mydl/account/getCompanyInfo.json'
        data={}
        data['companyId']=companyId
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #获取账户信息
    def getAcctInfo(self,userId=None,userAcct=None,token=None):
        url='/mydl/account/getAcctInfo.json'
        data={}
        data['userId']=userId
        data['userAcct']=userAcct
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #获取激活验证码
    def getValCodeForActivate(self,tel=None,token=None):
        url='/mydl/account/getValCodeForActivate.json'
        data={}
        data['tel']=tel
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #激活手机
    def activatePhone(self,userAcct=None,userId=None,conditionInd=None,tel=None,token=None):
        url='/mydl/account/activatePhone.json'
        data={}
        data['userAcct']=userAcct
        data['userId']=userId
        data['conditionInd']=conditionInd
        data['tel']=tel
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #--------------------------------找回密码及更改手机号------------------------------------------------------
    # 0262.密码找回验证码短信发送
    def getValCodeForPsw(self,tel=None):
        url='/login/getValCodeForPsw.json'
        data={}
        data['tel']=tel
        self.wrapHttpBase.post(url,data)
        return self.wrapHttpBase.body

    # 0263.重置密码（前台已校验过验证码)
    def resetPsw(self,tel=None,password=None,passwordConfirm=None):
        url='/login/resetPsw.json'
        data={}
        data['tel']=tel
        data['password']=password
        data['passwordConfirm']=passwordConfirm
        self.wrapHttpBase.post(url,data)
        return self.wrapHttpBase.body

    # 0268.获取原手机号解绑短信验证码(4位验证码)
    def getValCodeForUnbindPhone(self,tel=None,token=None):
        url='/mydl/account/getValCodeForUnbindPhone.json'
        data={}
        data['tel']=tel
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    # 0269.获取新手机号激活验证码(4位验证码)
    def getValCodeForBindPhone(self,tel=None,token=None):
        url='/mydl/account/getValCodeForBindPhone.json'
        data={}
        data['tel']=tel
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    # 0270.激活新的手机号码
    def activateNewPhone(self,valCode=None,tel=None,token=None):
        url='/mydl/account/activateNewPhone.json.json'
        data={}
        data['valCode']=valCode
        data['tel']=tel
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    # 0271.获取图形验证码(4位纯数字)
    def getPicValCode(self,pictureWidth=None,pictureHeight=None,token=None):
        url='/common/pic/getPicValCode.json'
        data={}
        data['pictureWidth']=pictureWidth
        data['pictureHeight']=pictureHeight
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    # 0272.校验图形验证码(需要token)
    def validatePicValCode(self,picValCode=None,token=None):
        url='/common/pic/validatePicValCode.json'
        data={}
        data['picValCode']=picValCode
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    # 0273.校验图形验证码(不需要token)
    def validatePicValCode2(self,picValCode=None):
        url='/common/pic/validatePicValCode2.json'
        data={}
        data['picValCode']=picValCode
        self.wrapHttpBase.post(url,data)
        return self.wrapHttpBase.body

    # 0274.校验短信验证码
    def validateMsgValCode(self,valCode=None,token=None):
        url='/common/pic/validatePicValCode2.json'
        data={}
        data['valCode']=valCode
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    # 0275.校验短信验证码
    def validateMsgValCode2(self,valCode=None):
        url='/common/pic/validatePicValCode2.json'
        data={}
        data['valCode']=valCode
        self.wrapHttpBase.post(url,data)
        return self.wrapHttpBase.body

    # -----------------------------------红包项目-----------------------------------------------------
    #获取优惠券列表
    def getCouponList(self,companyId=None,merchList=None,token=None):
        url = '/coupon/getCouponList.json'
        data = {}
        data['companyId']=companyId
        data['merchList']=merchList
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #获取优惠劵列表（个人中心：未使用，已过期，已使用）
    def getMyCouponList(self,companyId=None,couponStatus=None,page=None,rows=None,token=None):
        url = '/coupon/getMyCouponList.json'
        data ={}
        data['companyId']=companyId
        data['couponStatus']=couponStatus
        data['page']=page
        data['rows']=rows
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body

    #获取优惠劵列表张数
    def getMyCouponCnt(self,companyId=None,token=None):
        url = '/coupon/getMyCouponCnt.json'
        data={}
        data['companyId']=companyId
        self.wrapHttpBase.post(url,data,token)
        return self.wrapHttpBase.body





