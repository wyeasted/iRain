#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
import unittest
import time as t
from page.init import *
from page.parklogin import *
from page.shanghu import *

class PackShangHuGL(PortalTest,ShangHuTest):

	def test_addcheck(self,error1='erroraccount',error2='errorpass',error3='errorphone'):
		'''验证创建商户：字符与长度校验'''
		self.shgl
		self.err_shanghuadd()
		account=self.erroraccount
		pass1=self.errorpass
		phone=self.errorphone
		self.assertEqual(account,self.getXmlData(error1))
		self.assertEqual(pass1,self.getXmlData(error2))
		self.assertEqual(phone,self.getXmlData(error3))

	def test_addsh(self):
		'''验证创建商户：创建用户时的商户名与成功后的用户名一致'''
		self.shgl
		t.sleep(3)
		name=self.isshanghu()
		self.shgl
		listname=self.shanghuname
		self.shanghudelete()
		self.assertEqual(listname,name)
	#
	def test_delsh(self,value='nulltext'):
		'''验证删除商户：删除后表格数据为空'''
		self.shgl
		self.isshanghu()
		self.shgl
		self.shanghudelete()
		self.assertEqual(self.nullshanghu,self.getXmlData(value))

	def test_editsh(self,parent='editfinish',value1='overnum',value2='overmoney',value3='overtime'):
		'''验证编辑商户：编辑时信息与编辑完信息一致'''
		self.shgl
		self.isshanghu()
		self.shgl
		self.editshanghu()
		self.shgl
		self.namelink
		self.assertEqual(self.getnum,self.getXmlUser(parent,value1))
		self.assertEqual(self.getmoney,self.getXmlUser(parent,value2))
		self.assertEqual(self.gettime,self.getXmlUser(parent,value3))
		self.shgl
		self.shanghudelete()


	def test_dongjie(self,value='freezetext'):
		'''验证冻结商户:冻结后状态变为冻结'''
		self.shgl
		self.isshanghu()
		self.shgl
		self.shanghudongjie()
		self.assertEqual(self.dongjiestatus,self.getXmlData(value))
		self.shanghudelete()

	def test_active(self, value='activetext'):
		'''验证激活商户:激活后状态变为激活'''
		self.shgl
		self.isshanghu()
		self.shgl
		self.shanghudongjie()
		self.shanghujihuo()
		self.assertEqual(self.jihuostatus,self.getXmlData(value))
		self.shanghudelete()

	def test_send(self,value='sumlimit'):
		'''验证发劵限制：总数限制数值与设置时一致'''
		self.shgl
		self.isshanghu()
		self.shgl
		self.fajuanlimit()
		self.fajuan
		self.assertEqual(self.getsumtext,self.getXmlData(value))
		self.fajuansave
		self.shanghudelete()

if __name__ == '__main__':
    unittest.main(verbosity=2)




