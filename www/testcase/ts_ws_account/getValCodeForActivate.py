#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from www.common.database import *
from www.common.excel import *
from www.common.webservice import *

"""
0290.获取激活验证码(6位验证码)
http://127.0.0.1:8280/mallws/mydl/account/getValCodeForActivate.json
{
	"token":"123",
	"tel": "13800138000"        @NotNull，不为空字符串
}

{
    "code": 200,
    "description": "执行成功!",
    "model": {
        "success": "0",                //0-成功 1-手机号格式错误 4-发送间隔少于1分钟 9-验证码发送失败
		"valCode": "1234"              //验证码
    },
    "metadata": {
        "type": 0,
        "clazz": "cn.com.hd.mall.web.webservices.entity.response.mydl.account.GetValCodeForActivateResponse"
    }
}
"""

class getValCodeForActivate(unittest.TestCase):
    UserShop2=eData('TmlShop2')

