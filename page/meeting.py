#!/usr/bin/env python
# -*-coding:utf-8-*-

from base.basepage import *
from reader.helper import *
from init import *
from selenium.webdriver.common.by import By
import time as t

class MeetingInfo(IrainPortal,DataHelper):

	'''创建会议页面属性'''
	meetmanage_loc=(By.LINK_TEXT,u'会议管理')
	meetcreate_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/a')
	title_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[1]/div/input')
	address_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div/input')
	totlenum_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[6]/div/input')
	content_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[7]/div/textarea')
	addmeet_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[10]/div/button')

	@property
	def meetmanage(self):
		self.findElement(*self.meetmanage_loc).click()
		t.sleep(2)

	@property
	def meetcreate(self):
		self.findElement(*self.meetcreate_loc).click()

	def title(self,titlename):
		self.findElement(*self.title_loc).send_keys(titlename)

	def gettitle(self):
		return self.findElement(*self.title_loc).get_attribute('value')

	def address(self,address):
		self.findElement(*self.address_loc).send_keys(address)

	def activefirstime(self,firstime):
		startTime = "$(\"input[placeholder='请选择时间']\").removeAttr('readonly');$(\"input[placeholder='请选择时间']\").attr('value','firstime')"
		info=PortalTest()
		info.script(startTime)

	def activesectime(self,secondtime):
		secTime="$(\"input[placeholder='请选择时间']\").removeAttr('readonly');$(\"input[placeholder='请选择时间']\").attr('value','secondtime')"


	def countfirstime(self,firstcount):
		startTime = "$(\"input[placeholder='请选择时间']\").removeAttr('readonly');$(\"input[placeholder='请选择时间']\").attr('value','firstcount')"

	def countsectime(self,secondcount):
		secTime="$(\"input[placeholder='请选择时间']\").removeAttr('readonly');$(\"input[placeholder='请选择时间']\").attr('value','secondcount')"

	def totlenum(self,num):
		self.findElement(*self.totlenum_loc).send_keys(num)

	def content(self,content):
		self.findElement(*self.content_loc).send_keys(content)

	@property
	def addmeet(self):
		self.findElement(*self.addmeet_loc).click()

	'''创建会议'''
	def meetadd(self,parent='meetmanage',titlename='title',address='address',firstime='time1',secondtime='time2',firstcount='time3',secondcount='time4',num='num',content='des'):

		self.meetmanage
		self.meetcreate
		self.title(self.getXmlUser1(parent,titlename))
		titlename=self.gettitle()
		self.address(self.getXmlUser1(parent,address))
		self.activefirstime(self.getXmlUser1(parent,firstime))
		self.activesectime(self.getXmlUser1(parent,secondtime))
		self.countfirstime(self.getXmlUser1(parent,firstcount))
		self.countsectime(self.getXmlUser1(parent,secondcount))
		self.totlenum(self.getXmlUser1(parent,num))
		self.content(self.getXmlUser1(parent,content))
		self.addmeet
		return titlename

	'''会议列表页面属性'''
	meetname_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/a')
	nullmeet_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div/table/tbody/tr/td/div')

	@property
	def meetname(self):
		meetname=self.findElement(*self.meetname_loc).text
		return meetname

	@property
	def nullmeet(self):
		return self.findElement(*self.nullmeet_loc).text

	'''会议删除页面属性'''
	delmeet_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/div/table/tbody/tr/td[7]/span[2]')
	delsure_loc=(By.XPATH,'//*[@id="layui-layer13"]/div[3]/a[1]')

	@property
	def meetdel(self):
		self.findElement(*self.delmeet_loc).click()

	@property
	def delsure(self):
		self.findElement(*self.delsure_loc).click()

	def meetdelete(self):
		self.meetdel
		self.delsure




