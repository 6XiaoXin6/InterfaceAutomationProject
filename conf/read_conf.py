#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import configparser
from icecream import ic


def read_conf(confpath, env, url):
    conf = configparser.ConfigParser()
    conf.read(confpath)
    host = conf.get(env, url)
    return host

# ic()
# ic(read_conf('conf.ini', 'sit', 'url'))
# ic(read_conf('conf.ini', 'online', 'url'))
