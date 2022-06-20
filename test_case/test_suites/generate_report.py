#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import unittest

from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(
    start_dir="/test_case/", pattern="test*.py")
suite.addTests(tests)
with open("/test_reports/reports_html/report.html",
          "w", encoding = "utf-8") as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="接口测试报告", description="控制塔接口测试报告")
    runner.run(suite)
