#!/usr/bin/env python
# -*-coding:utf-8-*-

from page.init import *
from page.meeting import *
from page.parklogin import *
import unittest
import time as t

class MeetingTest(PortalTest,MeetingInfo):
    '''验证创建会议：创建会议时的标题与成功后的标题一致'''

    def test_addmt(self):
		self.login()
		titlename=self.meetadd()
		meetname=self.meetname
		self.meetdelete()
		self.assertEqual(titlename,meetname)

if __name__ == '__main__':
	unittest.main(verbosity=2)

