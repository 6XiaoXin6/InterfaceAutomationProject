#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

# from ddt import file_data, ddt
import unittest

# import pytest as pytest
from ddt2 import file_data, ddt
from common.keys import Keys
from conf.read_conf import read_conf
# @ddt
# class Ddt2TestCase(unittest.TestCase):                                    
#     @file_data('C:/Users/xiaoxin/PycharmProjects/InterfaceAutomationProject/data/login.yaml')
#     def test_ddt(self, **kwargs):
#         print(kwargs['path'])
#         print('======')
@ddt
class LoginTestCase(unittest.TestCase):

    # @file_data('test_data_dict.yaml')
    @file_data('C:/Users/xiaoxin/PycharmProjects/InterfaceAutomationProject/data/login.yaml')
    def test_login(self, **kwarg):  # 参数类型一致性
        # def test_file_data_yaml_dict(self, value):#参数类型一致性
        # self.assertTrue(has_three_elements(value))
        # host=read_conf("C:/Users/xiaoxin/PycharmProjects/InterfaceAutomationProject/conf/conf.ini","online","host")
        # url=host+kwarg["path"]
        # json={"phone":kwarg["user"]["phone"],}
        # #
        # k=Keys()
        # response=k.do_post(url,)
        # pass
        assert "成功状态码"==kwarg["response"]["message"]




# if __name__ == '__main__':
#     pytest.main()

if __name__ == '__main__':
    unittest.main(verbosity=2)

# test(1,2)
