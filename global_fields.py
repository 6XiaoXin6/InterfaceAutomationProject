#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'


def _init_():
    global global_dict
    global_dict = {}


def set_value(key, value):
    global_dict[key] = value


def get_value(key):
    return getattr(global_dict, key, f"没有属性{key}")
