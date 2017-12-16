#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
from base.basepage import IrainPortal
from selenium.webdriver.common.by import By
from reader.helper import DataHelper
import time as t

class LoginTest(IrainPortal,DataHelper):
	username_loc=(By.NAME,'username')
	password_loc=(By.NAME,'password')
	login_button=(By.XPATH,'//*[@id="app"]/div/div/div[2]/form/div[4]/button')

	def typeusername(self,username):
		self.findElement(*self.username_loc).send_keys(username)

	def typepassword(self,password):
		self.findElement(*self.password_loc).send_keys(password)

	def loginbutton(self):
		self.findElement(*self.login_button).click()

	def login(self,parent='login',username='username',password='password'):
		self.typeusername(self.getXmlUser(parent,username))
		self.typepassword(self.getXmlUser(parent,password))
		self.loginbutton()
		t.sleep(3)