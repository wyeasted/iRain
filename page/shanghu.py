#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
from base.basepage import *
from selenium.webdriver.common.by import By
from reader.helper import *
import time as t

class ShangHuTest(IrainPortal,DataHelper):
	'''查询元素页面属性'''
	select_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/div[2]/input')
	select_button=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/div[3]/button')

	def selectname(self,parent='shanghu',name='name'):
		self.findElement(*self.select_loc).send_keys(self.getXmlUser(parent,name))

	@property
	def selectbutton(self):
		self.findElement(*self.select_button).click()

	def select(self):
		self.selectname()
		self.selectbutton

	'''商户列表元素属性'''
	shgl_loc=(By.LINK_TEXT,u'商户管理')
	shanghuname_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[1]/div/a')
	null_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td/div')

	@property
	def shgl(self):
		t.sleep(3)
		self.findElement(*self.shgl_loc).click()

	@property
	def shanghuname(self):
		t.sleep(3)
		return self.findElement(*self.shanghuname_loc).text

	@property
	def nullshanghu(self):
		return self.findElement(*self.null_loc).text

	'''添加商户元素页面属性'''
	shanghuadd_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/a')
	account_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[1]/div/input')
	accountname_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[2]/div/input')
	accountpass_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[3]/div/input')
	usertype_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[4]/div/label[2]/input')
	touzhinum_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[5]/div[1]/div/div/input')
	touzhimoney_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[5]/div[2]/div/div/input')
	touzhitime_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[5]/div[3]/div/div/input')
	phone_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[8]/div/input')
	address_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[9]/div/input')
	des_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[10]/div/textarea')
	finishadd_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[11]/div/button')

	@property
	def shanghu11(self):
		self.wait()
		self.findElement(*self.shanghuadd_loc).click()

	def account(self,account):
		self.wait()
		self.findElement(*self.account_loc).send_keys(account)

	def accountname(self,accountname):
		self.wait()
		self.findElement(*self.accountname_loc).send_keys(accountname)

	def getaccountname(self):
		self.wait()
		return self.findElement(*self.accountname_loc).get_attribute('value')

	def accountpass(self,accountpass):
		self.wait()
		self.findElement(*self.accountpass_loc).send_keys(accountpass)

	@property
	def usertype(self):
		self.wait()
		self.findElement(*self.usertype_loc).click()

	def touzhinum(self,num):
		self.wait()
		self.findElement(*self.touzhinum_loc).clear()
		self.findElement(*self.touzhinum_loc).send_keys(num)

	def touzhimoney(self,money):
		t.sleep(4)
		self.findElement(*self.touzhimoney_loc).clear()
		self.findElement(*self.touzhimoney_loc).send_keys(money)

	def touzhitime(self,time):
		t.sleep(4)
		self.findElement(*self.touzhitime_loc).clear()
		self.findElement(*self.touzhitime_loc).send_keys(time)

	def phone(self,phone):
		self.wait()
		self.findElement(*self.phone_loc).send_keys(phone)

	def address(self,address):
		self.wait()
		self.findElement(*self.address_loc).send_keys(address)

	def description(self, dec):
		self.wait()
		self.findElement(*self.des_loc).send_keys(dec)

	@property
	def finish(self):
		self.findElement(*self.finishadd_loc).click()
		self.wait()

	'''正常创建商户'''
	def shanghuadd(self,parent='shanghu',account='acc',accountname='name',accountpass='password',
	               num='overnum',money='overmoney',time='overtime',phone='phone',address='address',dec='des'):

		self.shanghu11
		self.account(self.getXmlUser(parent,account))
		self.accountname(self.getXmlUser(parent,accountname))
		name=self.getaccountname()
		self.accountpass(self.getXmlUser(parent,accountpass))
		self.usertype
		self.touzhinum(self.getXmlUser(parent,num))
		self.phone(self.getXmlUser(parent,phone))
		self.address(self.getXmlUser(parent,address))
		self.description(self.getXmlUser(parent,dec))
		self.finish
		return name

	'''创建商户时字段校验'''
	error_account_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[1]/div/span')
	error_pass_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[3]/div/span')
	error_phone_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[8]/div/span')

	@property
	def erroraccount(self):
		account=self.findElement(*self.error_account_loc).text
		return account

	@property
	def errorpass(self):
		pass1=self.findElement(*self.error_pass_loc).text
		return pass1

	@property
	def errorphone(self):
		phone=self.findElement(*self.error_phone_loc).text
		return phone

	def err_shanghuadd(self,parent='errorshanghu',account='acc',accountname='name',accountpass='password',phone='phone'):
		self.shanghu11
		t.sleep(3)
		self.account(self.getXmlUser(parent, account))
		self.accountname(self.getXmlUser(parent,accountname))
		self.accountpass(self.getXmlUser(parent,accountpass))
		self.phone(self.getXmlUser(parent,phone))
		self.finish



	'''删除商户元素页面属性'''
	delsel_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[5]/div/i')
	def_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[5]/div/ul/li[2]')
	delsure_loc=(By.CSS_SELECTOR,'.layui-layer-btn0')

	@property
	def delsel(self):
		t.sleep(3)
		self.findElement(*self.delsel_loc).click()

	def shanghudel(self):
		t.sleep(2)
		self.findElement(*self.def_loc).click()
		self.delsure()

	def delsure(self):
		t.sleep(2)
		self.findElement(*self.delsure_loc).click()
		t.sleep(3)

	def shanghudelete(self):
		self.delsel
		self.shanghudel()

	'''冻结商户元素页面属性'''
	dongjie_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[5]/div/a')
	dongjiesure_loc = (By.CSS_SELECTOR, '.layui-layer-btn0')
	dongjie_status = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[3]/span')

	def shanghudongjie(self):
		t.sleep(2)
		self.findElement(*self.dongjie_loc).click()
		self.dongjiesure()
		t.sleep(3)

	def dongjiesure(self):
		t.sleep(2)
		self.findElement(*self.dongjiesure_loc).click()
		t.sleep(2)

	@property
	def dongjiestatus(self):
		name=self.findElement(*self.dongjie_status).text
		return name

	'''激活商户元素页面属性'''
	jihuo_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[5]/div/a')
	jihuosure_loc = (By.CSS_SELECTOR, '.layui-layer-btn0')
	jihuo_status = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[3]/span')

	def shanghujihuo(self):
		t.sleep(2)
		self.findElement(*self.jihuo_loc).click()
		self.jihuosure()
		t.sleep(3)

	def jihuosure(self):
		t.sleep(2)
		self.findElement(*self.jihuosure_loc).click()
		t.sleep(2)

	@property
	def jihuostatus(self):
		name=self.findElement(*self.jihuo_status).text
		return name

	'''编辑商户元素页面属性'''
	accnamelink_loc=(By.LINK_TEXT,'xian')
	edit_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div/div[2]/div/div[13]/div/button')
	editsave_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div/div[2]/div/div[12]/div[2]/button')
	inputnum_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div/div[2]/div/div[4]/div/div/input')
	inputmoney_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div/div/input')
	inputtime_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div/div/input')
	getnum_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div/div[2]/div/div[4]/div/p')
	getmoney_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div/p')
	gettime_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div/p')

	@property
	def namelink(self):
		self.findElement(*self.accnamelink_loc).click()
		t.sleep(3)

	@property
	def edit(self):
		self.findElement(*self.edit_loc).click()

	@property
	def editsave(self):
		self.findElement(*self.editsave_loc).click()

	def inputnum(self,num):
		t.sleep(3)
		self.findElement(*self.inputnum_loc).clear()
		self.findElement(*self.inputnum_loc).send_keys(num)
		t.sleep(3)

	# def gettouzhinum(self):
	# 	self.wait()
	# 	initnum=self.findElement(*self.inputnum_loc).get_attribute('value')
	# 	return initnum

	def inputmoney(self,money):
		t.sleep(3)
		self.findElement(*self.inputmoney_loc).click()
		self.findElement(*self.inputmoney_loc).clear()
		self.findElement(*self.inputmoney_loc).send_keys(money)
		t.sleep(3)

	# def gettouzhimoney(self):
	# 	self.wait()
	# 	initmoney=self.findElement(*self.inputmoney_loc).get_attribute('value')

	def inputtime(self,time):
		t.sleep(3)
		self.findElement(*self.inputtime_loc).click()
		self.findElement(*self.inputtime_loc).clear()
		self.findElement(*self.inputtime_loc).send_keys(time)

	# def gettouzhitime(self):
	# 	self.wait()
	# 	inittime=self.findElement(*self.inputtime_loc).get_attribute('value')
	# 	return inittime

	@property
	def getnum(self):
		return self.findElement(*self.getnum_loc).text

	@property
	def getmoney(self):
		return self.findElement(*self.getmoney_loc).text

	@property
	def gettime(self):
		return self.findElement(*self.gettime_loc).text


	def editshanghu(self,parent='editshanghu',num='overnum',money='overmoney',time='overtime'):
		self.namelink
		t.sleep(3)
		self.edit
		self.inputnum(self.getXmlUser(parent,num))
		self.inputmoney(self.getXmlUser(parent,money))
		self.inputtime(self.getXmlUser(parent,time))
		self.editsave


	'''发劵限制元素页面属性'''
	fajuan_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[5]/a[2]')
	sumlimit_loc=(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[2]/div/div[1]/div[1]/span')
	sumtext_loc=(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/input')
	sumselect_loc=(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/a/span')
	summonth_loc=(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/ul/li[3]')
	fajuansure_loc=(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[3]/button[1]')

	@property
	def fajuan(self):
		self.findElement(*self.fajuan_loc).click()
		t.sleep(3)

	@property
	def sumlimit(self):
		t.sleep(3)
		self.findElement(*self.sumlimit_loc).click()
		t.sleep(2)

	@property
	def sumselect(self):
		t.sleep(2)
		self.findElement(*self.sumselect_loc).click()


	def sumtext(self,value='sumlimit'):
		self.findElement(*self.sumtext_loc).send_keys(self.getXmlData(value))
		t.sleep(3)

	@property
	def getsumtext(self):
		return self.findElement(*self.sumtext_loc).get_attribute('value')

	@property
	def summonth(self):
		self.findElement(*self.summonth_loc).click()
		t.sleep(2)

	@property
	def fajuansave(self):
		self.findElement(*self.fajuansure_loc).click()
		t.sleep(3)

	def fajuanlimit(self):
		self.fajuan
		self.sumlimit
		self.sumselect
		self.summonth
		self.sumtext()
		self.fajuansave


	def isshanghu(self):
		try:
			self.select()
			assert self.shanghuname in u'xian'
			self.refresh()
			self.shanghudelete()
		except:
			name=self.shanghuadd()
			return name
		else:
			name=self.shanghuadd()
			return name
		finally:
			pass























