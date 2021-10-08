# -*- coding: utf-8 -*-
# @Time    : 2021-3-5
# @Author  : huangjing
# @File    : test_company.py

import time
import json
import random
import unittest
from TestCase.initEnv import *
from ApiCommon.Company_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestCompany(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.company = Company_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()
        cls.g["comName"] = "python服务站" + str(random.randint(1, 1000))
        # print(cls.g["comName"])

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
    @logger("添加公司")
    def test_addcompany(self):
        """
            公司管理：添加公司
        """
        response = self.company.add_company(self.req_url, self.g["Cookie"], self.g["comName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询公司")
    def test_findcompany(self):
        """
            公司管理：查询公司
        """
        response = self.company.find_company(self.req_url, self.g["Cookie"])
        pythonorg = response["body"]["rows"][0]["children"][1]["children"]
        for i in range(0, len(pythonorg)):
            if pythonorg[i]["comName"] == self.g["comName"]:
                self.g["comId"] = pythonorg[i]["comId"]
        # print(self.g["comId"])
        assert self.initEvn.test.assert_in_text(response['body'], "python")

    @logger("编辑公司")
    def test_editcompany(self):
        """
            公司管理：编辑公司
        """
        self.g["comName"] = "编辑" + self.g["comName"]
        response = self.company.edit_company(self.req_url, self.g["Cookie"], self.g["comId"], self.g["comName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("禁用公司")
    def test_disablecompany(self):
        """
            公司管理：禁用公司
        """
        response = self.company.disable_company(self.req_url, self.g["Cookie"], self.g["comId"], self.g["comName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
