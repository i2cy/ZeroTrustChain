#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: i2cy(i2cy@outlook.com)
# Project: ZeroTrust
# Filename: zerotrust_tcp
# Created on: 2022/2/1

import i2cylib.network.I2TCP.client as i2tc
import i2cylib.network.I2TCP.server as i2ts
import rsa


class ZTClient(i2tc.Client):

    def __init__(self, *args, **kwargs):
        """
        I2TCPclient 客户端通讯类

        :param hostname: str, server address 服务器地址
        :param port: int, server port 服务器端口
        :param key: str, dynamic key for authentication 对称动态密钥
        :param watchdog_timeout: int, watchdog timeout 守护线程超时时间
        :param logger: Logger, client log output object 日志器（来自于i2cylib.utils.logger.logger.Logger）
        :param max_buffer_size: int, max pakcage buffer size 最大包缓冲池大小（单位：个）
        """
        super(ZTClient, self).__init__(*args, **kwargs)

        self.session_key = b""

    def connect(self, timeout=10):
        """

        :param timeout:
        :return:
        """
        super(ZTClient, self).connect(timeout=timeout)

