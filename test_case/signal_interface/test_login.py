#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import unittest
import jsonpath
from ddt2 import file_data, ddt
from common.keywords import Keys
from conf.read_conf import read_conf


@ddt
class LoginTestCase(unittest.TestCase):

    @file_data('C:/Users/xiaoxin/PycharmProjects/InterfaceAutomation4SLProject/data/login.yaml')
    def test_login(self, **kwargs):  # 参数类型一致性

        host = read_conf("C:/Users/xiaoxin/PycharmProjects/InterfaceAutomation4SLProject/conf/conf.ini", "online", "host")
        url = host + kwargs["path"]
        json = {"phone": kwargs["user"]["phone"], "phoneCode": kwargs["user"]["phoneCode"]}
        headers = {
            "cookie": kwargs['headers']["cookie"]
        }

        k = Keys()
        response = k.do_post(url, headers=headers, json=json)

        message = jsonpath.jsonpath(response.json(), "$.message")[0]
        assert message == kwargs["response"]["message"]


# if __name__ == '__main__':
#     pytest.main()

if __name__ == '__main__':
    unittest.main(verbosity=2)
