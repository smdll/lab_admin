# -*- coding: utf-8 -*-

import wx.grid as Grid

class GridTable(Grid.PyGridTableBase):
	def __init__(self, data):
		grid.PyGridTableBase.__init__(self)

		self.datas = data
		self.colLabels = [u'试卷名', u'制卷人', u'制卷人账号', u'考试成绩', u'测试开始时间', u'测试结束时间', u'测试时长']

		self.odd = grid.GridCellAttr()
		self.odd.SetReadOnly(True)
		self.odd.SetBackgroundColour('grey')
		self.even = grid.GridCellAttr()
		self.even.SetReadOnly(True)