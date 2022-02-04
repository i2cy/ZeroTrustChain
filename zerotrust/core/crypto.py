#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: i2cy(i2cy@outlook.com)
# Project: ZeroTrust
# Filename: crypto
# Created on: 2022/2/4

import rsa


def generate_rsakey():
    """
    生成非对称加密公钥私钥

    :return: 公钥，私钥
    """
    return rsa.newkeys(1024)
