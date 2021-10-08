# -*- coding: utf-8 -*-
# @Time    : 2021-9-28
# @Author  : 库婉君
# @File    : test_group.py

import time
import json
import random
import unittest
from TestCase.initEnv import *
from ApiCommon.Group_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestGroup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.group = Group_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()
        cls.g["groupName"] = "python用户组" + str(random.randint(1, 1000))

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @logger("添加用户组")
    def test_addgroup(self):
        """
            用户组管理：添加用户组
        """
        response = self.group.add_group(self.req_url, self.g["Cookie"], self.g["groupName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询用户组")
    def test_findgroup(self):
        """
            用户组管理：查询用户组
        """
        response = self.group.find_group(self.req_url, self.g["Cookie"], self.g["groupName"])
        pythongroup = response["body"]["rows"]
        for i in range(0, len(pythongroup)):
            if pythongroup[i]["groupName"] == self.g["groupName"]:
                self.g["groupId"] = pythongroup[i]["groupId"]
        print(self.g["groupId"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["groupName"])

    @logger("用户组授权")
    def test_editgroupMenu(self):
        """
            用户组管理：用户组授权
        """
        response = self.group.edit_groupMenu(self.req_url, self.g["Cookie"], self.g["groupId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)


    @logger("编辑用户组")
    def test_editgroup(self):
        """
            用户组管理：编辑用户组
        """
        self.g["groupName"] = "编辑" + self.g["groupName"]
        response = self.group.edit_group(self.req_url, self.g["Cookie"], self.g["groupId"], self.g["groupName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("禁用用户组")
    def test_disablegroup(self):
        """
            用户组管理：禁用用户组
        """
        response = self.group.disable_group(self.req_url, self.g["Cookie"], self.g["groupId"], self.g["groupName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
