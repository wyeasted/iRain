#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
from page.parklogin import *
from base.basepage import *
import unittest

class PortalTest(unittest.TestCase,LoginTest):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('http://eco.parkingwang.com/#/login')

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def script(self,info):
		self.driver.execute_script(info)

