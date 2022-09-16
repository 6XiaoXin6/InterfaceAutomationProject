#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import unittest

from ddt2 import file_data, ddt

from common.keywords import Keys
from conf.read_conf import read_conf


@ddt
class UnreadNotions(unittest.TestCase):

    @file_data('C:/Users/xiexinli/Documents/GitHub/InterfaceAutomation4SLProject/data/test _unread_notions.yaml')
    def test_unread(self, **kwargs):  # 参数类型一致性

        host = read_conf("C:/Users/xiexinli/Documents/GitHub/InterfaceAutomation4SLProject/conf/conf.ini", "sit",
                         "host")
        url = host + kwargs["path"]
        # json = {"phone": kwargs["user"]["phone"], "phoneCode": kwargs["user"]["phoneCode"]}
        headers = {
            "Authorization": kwargs['headers']["Authorization"]
        }

        k = Keys()
        response = k.do_get(url, headers=headers)
        # print(response.json())
        # message = jsonpath.jsonpath(response.json(), "$.message")[0]
        check = kwargs["response"]["check"]
        assert response.json() == check

# if __name__ == '__main__':
#     pytest.main()

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
