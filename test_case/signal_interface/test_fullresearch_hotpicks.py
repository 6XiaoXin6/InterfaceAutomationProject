#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import unittest

from ddt2 import file_data, ddt
from my_log import my_Logger

from common.keywords import Keys
from conf.read_conf import read_conf


@ddt
class FullSearch_HotPicks(unittest.TestCase):

    @file_data('C:/Users/xiexinli/Documents/GitHub/InterfaceAutomation4SLProject/data/fullsearch_hotpicks.yaml')
    def test_status(self, **kwargs):  # 参数类型一致性

        host = read_conf("C:/Users/xiexinli/Documents/GitHub/InterfaceAutomation4SLProject/conf/conf.ini", "sit",
                         "host")
        url = host + kwargs["path"]
        params = kwargs["params"]
        print(params)
        headers = {
            "Authorization": kwargs['headers']["Authorization"]
        }

        k = Keys()
        response = k.do_get(url, headers=headers, params=params)
        # logger=my_Logger.MyLogger.getMyLogger()

        # logger(response.json())

        message = jsonpath.jsonpath(response.json(), "$.message")[0]

        assert response.status_code == 200

# if __name__ == '__main__':
#     pytest.main()

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
