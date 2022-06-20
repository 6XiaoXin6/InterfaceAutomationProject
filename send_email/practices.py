#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

from send_email.send_email import MyEmail
args=["2585174552@qq.com", "xiexinli6@163.com"]
MyEmail(*args).send_email()
