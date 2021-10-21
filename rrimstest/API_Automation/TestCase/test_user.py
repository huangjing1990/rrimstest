# -*- coding: utf-8 -*-
# @Time    : 2021-9-29
# @Author  : 库婉君
# @File    : test_user.py

import time
import json
import random
import unittest
from TestCase.initEnv import *
from ApiCommon.User_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.user = User_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()
        cls.g["userId"] = "python用户" + str(random.randint(1, 1000))
        cls.g["userName"] = "python站长"

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @logger("添加用户")
    def test_adduser(self):
        """
            用户管理：添加用户
        """
        response = self.user.add_user(self.req_url, self.g["Cookie"], self.g["userId"], self.g["userName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询用户")
    def test_finduser(self):
        """
            用户管理：查询用户
        """
        response = self.user.find_user(self.req_url, self.g["Cookie"], self.g["userName"])
        pythongroup = response["body"]["rows"]
        for i in range(0, len(pythongroup)):
            if pythongroup[i]["userName"] == self.g["userName"]:
                self.g["userId"] = pythongroup[i]["userId"]
        print(self.g["userId"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["userName"])

    @logger("用户授权")
    def test_edituserHas(self):
        """
            用户管理：用户授权
        """
        response = self.user.edit_userHas(self.req_url, self.g["Cookie"], self.g["userId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)


    @logger("编辑用户")
    def test_edituser(self):
        """
            用户管理：编辑用户
        """
        self.g["userName"] = "编辑" + self.g["userName"]
        response = self.user.edit_user(self.req_url, self.g["Cookie"], self.g["userId"], self.g["userName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("用户重置密码")
    def test_resetPassworduser(self):
        """
            用户管理：用户重置密码
        """
        response = self.user.resetPassword_user(self.req_url, self.g["Cookie"], self.g["userId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("用户解锁")
    def test_unLockuser(self):
        """
            用户管理：用户解锁
        """
        response = self.user.unLock_user(self.req_url, self.g["Cookie"], self.g["userId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("禁用用户")
    def test_disableuser(self):
        """
            用户管理：禁用用户
        """
        response = self.user.disable_user(self.req_url, self.g["Cookie"], self.g["userId"], self.g["userName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
