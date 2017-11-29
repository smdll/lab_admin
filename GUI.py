# -*- coding: utf-8 -*-
import wx
import wx.grid
import functions

class GridFrame(wx.Frame):
	colLabel = (u'类别', u'设备名', u'型号', u'规格', u'单价', u'数量', u'购置日期', u'生产厂家', u'购买人', u'批次', u'机房')
	colSize = (80, 200, 50, 50, 50, 30, 70, 80, 55, 30, 55)

	def __init__(self, parent):
		self.initUI(parent)
		self.drawTable()
		print type(self)
		self.bindEvents()

	def initUI(self, parent):
		width = 0
		for i in self.colSize:
			width += i + 1
		wx.Frame.__init__(self, parent, title = u'实验室设备管理系统', size = (width, 360), style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

		self.btn1 = wx.Button(self, -1, u'设备入库', (0, 0), (80, 40))
		self.btn2 = wx.Button(self, -1, u'维修管理', (90, 0), (80, 40))
		wx.StaticText(self, -1, u'关键字：', (180, 10), (50, 30))
		self.cb = wx.ComboBox(self, -1, pos = (230, 5), size = (100, 30), choices = ['123','234','345','456'])
		wx.StaticText(self, -1, u'排序：', (340, 10), (45, 30))
		self.rb = wx.RadioBox(self, -1, pos = (375, -10), size = (50, 40), choices = ['123', '234'])
		self.btn3 = wx.Button(self, -1, u'查询', (480, 0), (80, 40))

		self.grid = wx.grid.Grid(self, -1, pos = (0, 40), size = (width, 360))
		self.Show()

	def drawTable(self):
		self.db = functions.lab_db()

		self.grid.CreateGrid(0, len(self.colLabel))
		self.grid.SetRowLabelSize(0)

		for i in range(len(self.colLabel)):
			self.grid.SetColLabelValue(i, self.colLabel[i])
			self.grid.SetColSize(i, self.colSize[i])

		data = self.db.inst_query()
		self.refreshData(data)

	def bindEvents(self):
		self.Bind(wx.EVT_BUTTON, self.Warehouse, self.btn1)
		self.Bind(wx.EVT_BUTTON, self.Repair, self.btn2)
		self.Bind(wx.EVT_BUTTON, self.Query, self.btn3)
		self.Bind(wx.EVT_CLOSE, self.Exit)

	def refreshData(self, data):
		rows = self.grid.GetNumberRows()
		if rows > 0:
			self.grid.DeleteRows(numRows = rows)
		j = 0
		for line in data:
			self.grid.InsertRows(j)
			for i in range(len(self.colLabel)):
				if isinstance(line[i], int):
					val = '%d'%line[i]
				else:
					val = line[i]
				self.grid.SetCellValue(j, i, val)
				self.grid.SetReadOnly(j, i)
			j += 1

	def Warehouse(self, event):
		whf = wx.Frame(self, -1, u'', size = (400, 100), style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
		wx.Button(whf, -1, u'123')
		whf.Bind(wx.EVT_BUTTON, whf.Show(False), whf)
		whf.Show()
		while whf.IsShown():
			pass
		whf.Destroy()

	def Repair(self, event):
		pass

	def Query(self, event):
		pass

	def Exit(self, event):
		self.Destroy()
		exit()

if __name__ == '__main__':
	app = wx.App()
	frame = GridFrame(None)
	app.MainLoop()