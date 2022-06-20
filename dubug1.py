#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import jsonpath
import requests
from icecream import ic


# res=requests.post("https://scct.sf-express.com/api/metis/user/phone/login",json={"phone": "17612153057", "phoneCode": "5173"},cookies={"JSESSIONID":"5AA8FDD1C126D44369899D6471AA2D18"})
# print(res.status_code)
# print(res.text)

res={'requestId': 'REQ-daad9e7a-3247-4901-9c87-87099bdf5fc6', 'code': 'BS0002', 'message': '验证码错误'}
res1="{'requestId': 'REQ-daad9e7a-3247-4901-9c87-87099bdf5fc6', 'code': 'BS0002', 'message': '验证码错误'}"


def get_args(response, key):
    return jsonpath.jsonpath(response, f"$..{key}")

# print(get_args(res,"message"))
print(get_args(res,"message"))


