#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
import xml.dom.minidom

class DataHelper(object):
	def getXmlData(self,value):
		dom = xml.dom.minidom.parse(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','login.xml'))
		db = dom.documentElement
		name = db.getElementsByTagName(value)
		nameValue = name[0]
		return nameValue.firstChild.data

	def getXmlUser(self,parent, child):
		dom = xml.dom.minidom.parse(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','login.xml'))
		db = dom.documentElement
		itemlist = db.getElementsByTagName(parent)
		item = itemlist[0]
		return item.getAttribute(child)

	def getXmlUser1(self,parent, child):
		dom = xml.dom.minidom.parse(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','meeting.xml'))
		db = dom.documentElement
		itemlist = db.getElementsByTagName(parent)
		item = itemlist[0]
		return item.getAttribute(child)
