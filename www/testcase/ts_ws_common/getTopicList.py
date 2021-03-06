#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
0287.获取主题列表（品类及其他）
http://127.0.0.1:8280/mallws/common/pic/getTopicList.json
{
	"token":"123"
}

{
    "code": 200,
    "description": "执行成功!",
    "model": {
        "success": "0"                                             // 0-成功 1-失败
		"topicList": [                                             // 主题列表
			{
				"topicType":"T01",                                 // 类型:T01-白酒，T02-葡萄酒，T03-啤酒，T04-其他饮品，T11-我的订单，T12-我的红包，T13-我的常购，T14-抽奖抢红包
				"topicTitle":"酒类",                               // 标题
				"topicDesc":"标题描述",                            // 描述-预留字段
				"picUrl":"123"                                     // 图片url
				"linkUrl":""                                       // 链接地址-预留字段
			}
        ]
    },
    "metadata": {
        "type": 0,
        "clazz": "cn.com.hd.mall.web.webservices.entity.response.common.GetTopicListResponse"
    }
}
"""

import unittest
from www.common.webservice import *
from www.common.excel import eData

class getTopicList(unittest.TestCase):

    UserShop = eData('TmlShop')
    Param = eData('Param')

    # S1.获取banner图片地址
    def test_getTopicList_get(self):
        ws = webservice()
        ws.login(self.UserShop.username,self.UserShop.password)
        TopicList = ws.getTopicList()
        self.assertEqual(TopicList.model['success'], '0')

    # S2.不带token获取banner图片地址
    def test_getTopicList_noToken(self):
        ws = webservice()
        ws.login(self.UserShop.username,self.UserShop.password)
        TopicList = ws.getTopicList(token='null')
        self.assertEqual(TopicList.code, 600)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(getTopicList("test_getTopicList_get"))
    suite.addTest(getTopicList("test_getTopicList_noToken"))
    return suite