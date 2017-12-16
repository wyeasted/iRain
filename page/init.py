#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
from page.parklogin import *
from base.basepage import *
import unittest

class PortalTest(unittest.TestCase,LoginTest):

	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://eco.parkingwang.com/#/login')

	def tearDown(self):
		self.driver.quit()
