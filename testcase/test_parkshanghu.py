#!/usr/bin/env python
# -*-coding:utf-8-*-

import unittest
import time as t
from page.init import *
from page.parklogin import *
from page.shanghu import *

class PackShangHuGL(PortalTest,ShangHuTest):

	def test_addcheckaccount(self,error1='erroraccount'):
		'''验证创建商户:账户长度错误的提示信息'''
		self.login()
		self.shgl
		self.err_shanghuadd1()
		account=self.erroraccount
		self.assertEqual(account,self.getXmlData(error1))

	def test_addcheckpass(self,error2='errorpass'):
		'''验证创建商户：密码长度错误的提示信息'''
		self.login()
		self.shgl
		self.err_shanghuadd2()
		pass1=self.errorpass
		self.assertEqual(pass1,self.getXmlData(error2))

	def test_addcheckphone(self,error3='errorphone'):
		'''验证创建商户：电话号码长度错误的提示信息'''
		self.login()
		self.shgl
		self.err_shanghuadd3()
		phone=self.errorphone
		self.assertEqual(phone,self.getXmlData(error3))

	def test_addsh(self):
		'''验证创建商户：创建用户时的商户名与成功后的用户名一致'''
		self.login()
		self.shgl
		name=self.isshanghu()
		self.shgl
		listname=self.shanghuname
		self.shanghudelete()
		self.assertEqual(listname,name)

	def test_delsh(self,value='nulltext'):
		'''验证删除商户：删除后表格数据为空'''
		self.login()
		self.shgl
		self.isshanghu()
		self.shgl
		self.shanghudelete()
		self.assertEqual(self.nullshanghu,self.getXmlData(value))

	def test_editsh(self,parent='editfinish',value1='overnum',value2='overmoney',value3='overtime'):
		'''验证编辑商户：编辑时信息与编辑完信息一致'''
		self.login()
		self.shgl
		self.isshanghu()
		self.shgl
		self.editshanghu()
		self.shgl
		self.namelink
		num=self.getnum
		money=self.getmoney
		time=self.gettime
		self.shgl
		self.shanghudelete()
		self.assertEqual(num,self.getXmlUser(parent,value1))
		self.assertEqual(money,self.getXmlUser(parent,value2))
		self.assertEqual(time,self.getXmlUser(parent,value3))

	def test_dongjie(self,value='freezetext'):
		'''验证冻结商户:冻结后状态变为冻结'''
		self.login()
		self.shgl
		self.isshanghu()
		self.shgl
		self.shanghudongjie()
		name=self.dongjiestatus
		self.shanghudelete()
		self.assertEqual(name,self.getXmlData(value))

	def test_active(self, value='activetext'):
		'''验证激活商户:激活后状态变为激活'''
		self.login()
		self.shgl
		self.isshanghu()
		self.shgl
		self.shanghudongjie()
		self.shanghujihuo()
		name=self.jihuostatus
		self.shanghudelete()
		self.assertEqual(name,self.getXmlData(value))

	def test_send(self,value='sumlimit'):
		'''验证发劵限制：总数限制数值与设置时一致'''
		self.login()
		self.shgl
		self.isshanghu()
		self.shgl
		self.fajuanlimit()
		self.fajuan
		self.fajuansave
		name=self.getsumtext
		self.shanghudelete()
		self.assertEqual(name,self.getXmlData(value))

if __name__ == '__main__':
    unittest.main(verbosity=2)




