#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

from icecream import ic

from my_log.my_Logger import MyLogger

ml=MyLogger()
gl=ml.getMyLogger()
gl.warning("test")

try:
    1/0
except Exception as e:
    gl.exception(e)
