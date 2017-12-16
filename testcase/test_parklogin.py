#!/usr/bin/env python
# -*-coding:utf-8-*-

import unittest
from selenium import webdriver
from page.init import *
from page.parklogin import *

class PackLogin(PortalTest):

	def testpacklogin(self):
		"验证用户名密码登陆成功后的url"
		self.login()
		self.assertTrue(str(self.driver.current_url).endswith('/#/mall/list'))

if __name__ =='__main__':
	unittest.main(verbosity=2)

