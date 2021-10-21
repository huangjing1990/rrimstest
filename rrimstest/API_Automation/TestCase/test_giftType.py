# -*- coding: utf-8 -*-
# @Time    : 2021-10-20
# @Author  : kuwanjun
# @File    : test_giftType.py

import time
import json
import random
import unittest
from TestCase.initEnv import *
from ApiCommon.GiftType_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestGiftType(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.giftType = GiftType_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()
        cls.g["giftTypeName"] = "python礼品类型" + str(random.randint(1, 1000))
        # print(cls.g["giftTypeName"])

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    # @logger("登录")
    # def test_login(self):
    #     """
    #         用例描述：登录
    #     """
    #     response = self.login.login(self.req_url, userName="cqhj", password="DB1A8BD798EEA81B0BE3DCA1D0E2C309")
    #     print(response["headers"])
    #     self.g["Cookie"] = {"JSESSIONID": response["headers"]["Set-Cookie"][11:43]}
    #     print(self.g["Cookie"])
    #     print("cqhj")
    #     assert self.initEvn.test.assert_code(response["code"], 302)
    #
    @logger("添加礼品类型")
    def test_addgiftType(self):
        """
            礼品类型设置：添加礼品类型
        """
        response = self.giftType.add_giftType(self.req_url, self.g["Cookie"], self.g["giftTypeName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询礼品类型")
    def test_findgiftType(self):
        """
            礼品类型设置：查询礼品类型
        """
        response = self.giftType.find_giftType(self.req_url, self.g["Cookie"], self.g["giftTypeName"])
        pythongiftType = response["body"]["rows"]
        for i in range(0, len(pythongiftType)):
            if pythongiftType[i]["giftTypeName"] == self.g["giftTypeName"]:
                self.g["giftTypeId"] = pythongiftType[i]["giftTypeId"]
        # print(self.g["giftTypeId"])
        assert self.initEvn.test.assert_in_text(response['body'], "python")

    @logger("编辑礼品类型")
    def test_editgiftType(self):
        """
            礼品类型设置：编辑礼品类型
        """
        self.g["giftTypeName1"] = "编" + self.g["giftTypeName"]
        response = self.giftType.edit_giftType(self.req_url, self.g["Cookie"], self.g["giftTypeId"], self.g["giftTypeName"],self.g["giftTypeName1"] )
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)


    @logger("禁用礼品类型")
    def test_disablegiftType(self):
        """
            礼品类型设置：禁用礼品类型
        """
        response = self.giftType.disable_giftType(self.req_url, self.g["Cookie"], self.g["giftTypeId"], self.g["giftTypeName1"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
