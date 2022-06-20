#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import unittest

from ddt2 import file_data, ddt
from icecream import ic

from common.keys import Keys
from conf.read_conf import read_conf


@ddt
class Case(unittest.TestCase):
    @classmethod
    # 全局变量
    def setUpClass(cls) -> None:
        cls.ik = Keys()
        cls.host = read_conf("../../conf/conf.ini", "online", "host")
        cls.ik.token = None



    @file_data("C:/Users/xiaoxin/PycharmProjects/InterfaceAutomationProject/data/login.yaml")
    def test_login(self, **kwargs):
        # 数据准备
        # print('========', kwargs)
        json = {"phone": kwargs["user"]["phone"], "phoneCode": kwargs["user"]["phoneCode"]}
        url = Case.host + kwargs["path"]
        cookies = {"JSESSIONID": kwargs["user"]["cookies"]}

        # 接口调用
        response = self.ik.do_post(url, json=json, cookies=cookies)
        # Case.token = self.ik.get_args(response.json(), "token")#Case.token为flase

        #获取token
        Case.ik.token = self.ik.get_args(response, "token")
        # print("=======",Case.token )

        # ic(response.json())
        # ic(response.status_code)

        # 断言
        assert response.json()["message"] == kwargs["response"]["message"]

    @file_data("C:/Users/xiaoxin/PycharmProjects/InterfaceAutomationProject/data/query_order.yaml")
    def test_query_order(self, **kwargs):
        url = Case.host + kwargs["path"]
        kwargs = self.ik.register(kwargs)
        # print(kwargs)

        response = self.ik.do_get(url, headers=kwargs["headers"], params=kwargs["params"])
        # response = self.ik.do_get(url, kwargs=kwargs)
        # print(response.status_code)
        # print(response.json())

        assert response.json()["message"] == kwargs["response"]["message"]


if __name__ == '__main__':
    unittest.main()
