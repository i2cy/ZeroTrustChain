#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: i2cy(i2cy@outlook.com)
# Project: ZeroTrust
# Filename: block_loader
# Created on: 2022/2/10

from i2cylib.filesystem.icfat64 import IcFAT


class BlockProfile(object):

    def __init__(self, target_file):
        """
        BLK本地私有文件库

        :param target_file:
        """
