#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import unittest

from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(
    start_dir="../signal_interface", pattern="test_*.py")
suite.addTests(tests)
with open("C:/Users/xiexinli/Documents/GitHub/InterfaceAutomation4SLProject/test_reports/reports_html/report.html",
          "w", encoding = "utf-8") as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="接口测试报告", description="苏格拉底接口测试报告")
    runner.run(suite)
