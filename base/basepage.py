#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
import time as t
from selenium.webdriver.support.expected_conditions import NoSuchElementException

class IrainPortal(object):
	def __init__(self,driver):
		self.driver=driver

	def findElement(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException as e:
			print 'Error Details is :%s' %(e.args[0])

	def findsElement(self,*loc):
		try:
			return self.driver.find_elements(*loc)
		except NoSuchElementException as e:
			print'Error Details is :%s' %(e.args[0])