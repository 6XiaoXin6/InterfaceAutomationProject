#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import unittest

from ddt2 import file_data, ddt
import jsonpath
from common.keywords import Keys
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
        url = Case.host + kwargs["path"]
        json = {"phone": kwargs["user"]["phone"], "phoneCode": kwargs["user"]["phoneCode"]}
        headers = {
            "cookie": kwargs['headers']["cookie"]
        }

        response = self.ik.do_post(url, json=json, headers=headers)

        # 获取token以便下面接口使用
        Case.ik.token = self.ik.get_args(response, "token")

        message = jsonpath.jsonpath(response.json(), "$.message")[0]
        assert message == kwargs["response"]["message"]

    @file_data("C:/Users/xiaoxin/PycharmProjects/InterfaceAutomationProject/data/query_order.yaml")
    def test_query_order(self, **kwargs):
        url = Case.host + kwargs["path"]
        kwargs = self.ik.register(kwargs)

        response = self.ik.do_get(url, headers=kwargs["headers"], params=kwargs["params"])

        assert response.json()["message"] == kwargs["response"]["message"]


if __name__ == '__main__':
    unittest.main()
