#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import jsonpath as jsonpath
import requests


class Keys:
    def do_get(self, url, headers=None, params=None):
        return requests.get(url, headers=headers, params=params)

    # def do_get(self, url, **kwargs):
    #     with sessions.Session() as session:
    #         return session.request(method="GET", url=url, kwargs=kwargs)

    def do_post(self, url, headers=None, json=None, data=None, cookies=None, params=None):
        return requests.post(url, headers=headers, data=data, json=json, cookies=cookies, params=params)

    # 获取响应的对应字段
    def get_args(self, response, key):
        token = jsonpath.jsonpath(response.json(), f"$..{key}")  # 第一个参数是json格式的Python对象
        if token:
            return token[0]
        else:
            print("未获取到token,登录失败")
            return token

    # 组装入参
    def register(self, kwargs):
        """

        :param kwargs:
        :return:
        """
        for k, v in kwargs.items():
            if isinstance(v, dict):
                self.register(v)
            else:
                if v == None:
                    kwargs[k] = getattr(self, k)
                else:
                    pass
        return kwargs
