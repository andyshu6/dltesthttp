#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
0256.消息数量
接口名称：
	标准JSON接口 http://127.0.0.1:8181/message/count
	JSONP接口 http://127.0.0.1:8181/p/message/count
接口说明：查询用户的消息数量，包括全部数量和未读数量
接口参数：
{
    "channelId":"CH01",
    "receiverUserId":"e9ba06042b97458bb8cfdb6873c30e2a",
    "receiverCompanyId":"e9ba06042b97458bb8cfdb6873asdfd"
}
接口参数说明：
 	全部必传，channelId 参考常量 com.danlu.dlsms.constant.MsgCommonConst.MsgChannel
接口返回说明：
{
    "code": 200,
    "description": "执行成功!",
    "model": {
        "success": "0",
        "msgCount": {
            "unreadCount": {
                "T0201": 0,
                "T01": 0,
                "T03,T04": 0,
                "T0202": 0
            },
            "allCount": {
                "T0201": 0,
                "T01": 0,
                "T03,T04": 0,
                "T0202": 0
            },
            "extensionCount": {
                "iRisedCount": 0,
                "hasCheckedCount": 0
            }
        }
    },
    "metadata": {
        "type": 0,
        "clazz": "com.danlu.dlsms.model.pub.res.MsgCountResponse"
    }
}
	遵循WebService规则，外层code 200代表系统成功，其他代表系统异常，内层success 0代表业务执行成功。
	返回两个Map，Key为消息的类型，value为对应的数量，如果不存在相应的键值对则认为没有此类型的消息。消息类型参考常量 com.danlu.dlsms.constant.MsgTypeConst
"""

import unittest
from www.common.webservice import *
from www.common.excel import eData

class count(unittest.TestCase):

    UserShop = eData('TmlShop')


    # S1.获取终端店消息数量
    def test_count_shop(self):
        ws = webservice()
        msgCount = ws.messageCount(receiverUserId = self.UserShop.userId, receiverCompanyId=self.UserShop.companyId)
        self.assertEqual(msgCount.model['success'], '0')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(count("test_count_shop"))
    return suite