#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""三步走 """

__author__ = 'List.Xie'

import logging
from datetime import datetime


class MyLogger():
    logger = logging.getLogger("我的日志记录器")

    def formatter(self):
        self.my_formatter = logging.Formatter("[%(asctime)s] %(pathname)s line:%(lineno)d %(message)s")
        return self.my_formatter

    def handler(self):
        self.log_file_name = datetime.now().strftime("%Y-%m-%d")
        self.my_handler = logging.FileHandler(
            f"C:/Users/xiexinli/Documents/GitHub/InterfaceAutomation4SLProject/my_log/log_files/{self.log_file_name}.log")
        self.my_handler.setFormatter(self.formatter())
        return self.my_handler

    def getMyLogger(self):
        self.logger.addHandler(self.handler())
        return self.logger
