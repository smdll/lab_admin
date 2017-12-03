# -*- coding: utf-8 -*-
import wx
import wx.grid
import functions

class GridFrame(wx.Frame):
	def __init__(self, parent):
		self.initUI(parent)

	# Initialize the graphical interface
	def initUI(self, parent):
		colLabel = (u'类别', u'设备名', u'型号', u'规格', u'单价', u'数量', u'购置日期', u'生产厂家', u'购买人', u'批次', u'机房', u'状态')
		colSize = (80, 200, 50, 50, 50, 30, 70, 80, 55, 30, 55, 50)
		width = 0
		for i in colSize:
			width += i + 1
		wx.Frame.__init__(self, parent, title = u'实验室设备管理系统', size = (width, 360), style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

		self.btn1 = wx.Button(self, -1, u'设备入库', (0, 0), (80, 40))
		self.btn2 = wx.Button(self, -1, u'维修管理', (90, 0), (80, 40))
		wx.StaticText(self, -1, u'关键字：', (180, 10), (50, 30))
		self.cb = wx.ComboBox(self, -1, pos = (230, 5), size = (100, 30), choices = [i for i in colLabel[:-1] if i != colLabel[5]])
		wx.StaticText(self, -1, u'排序：', (340, 10), (45, 30))
		self.rb = wx.RadioBox(self, -1, pos = (375, -10), size = (50, 40), choices = [u'升序', u'降序'])
		self.btn3 = wx.Button(self, -1, u'查询', (480, 0), (80, 40))
		self.db = functions.lab_db()

		self.grid = wx.grid.Grid(self, -1, pos = (0, 40), size = (width, 360))
		self.grid.CreateGrid(0, len(colLabel))
		self.grid.SetRowLabelSize(0)
		for i in range(len(colLabel)):
			self.grid.SetColLabelValue(i, colLabel[i])
			self.grid.SetColSize(i, colSize[i])

		self.refreshData('id', 'ASC')

		self.Bind(wx.EVT_BUTTON, self.Warehouse, self.btn1)
		self.Bind(wx.EVT_BUTTON, self.Repair, self.btn2)
		self.Bind(wx.EVT_BUTTON, self.Query, self.btn3)
		self.Bind(wx.EVT_CLOSE, self.Exit)
		self.Show()

	# Clear table and append new data
	def refreshData(self, keyword, sort):
		data = self.db.inst_query(keyword, sort)

		rows = self.grid.GetNumberRows()
		if rows > 0:
			self.grid.DeleteRows(numRows = rows)
		j = 0
		for line in data:
			self.grid.InsertRows(j)
			for i in range(len(line)):
				if isinstance(line[i], int):
					val = '%d'%line[i]
				else:
					val = line[i]
				self.grid.SetCellValue(j, i, val)
				self.grid.SetReadOnly(j, i)
			j += 1

	# Instrument warehousing interface
	def Warehouse(self, event):
		self.whf = wx.Dialog(self, -1, u'入库', size = (190, 330), style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX) | wx.FRAME_FLOAT_ON_PARENT)

		wx.StaticText(self.whf, -1, u'类别：', pos = (0, 0), size = (70, 20))
		self.whtype = wx.TextCtrl(self.whf, -1, pos = (70, 0), size = (100, 20))
		wx.StaticText(self.whf, -1, u'设备名：', pos = (0, 25), size = (70, 20))
		self.whname = wx.TextCtrl(self.whf, -1, pos = (70, 25), size = (100, 20))
		wx.StaticText(self.whf, -1, u'型号：', pos = (0, 50), size = (70, 20))
		self.whmodel = wx.TextCtrl(self.whf, -1, pos = (70, 50), size = (100, 20))
		wx.StaticText(self.whf, -1, u'规格：', pos = (0, 75), size = (70, 20))
		self.whspec = wx.TextCtrl(self.whf, -1, pos = (70, 75), size = (100, 20))
		wx.StaticText(self.whf, -1, u'单价：', pos = (0, 100), size = (70, 20))
		self.whcost = wx.TextCtrl(self.whf, -1, pos = (70, 100), size = (100, 20))
		wx.StaticText(self.whf, -1, u'购置日期：', pos = (0, 125), size = (70, 20))
		self.whdate = wx.TextCtrl(self.whf, -1, pos = (70, 125), size = (100, 20))
		wx.StaticText(self.whf, -1, u'数量：', pos = (0, 150), size = (70, 20))
		self.whcount = wx.TextCtrl(self.whf, -1, pos = (70, 150), size = (100, 20))
		wx.StaticText(self.whf, -1, u'生产厂家：', pos = (0, 175), size = (70, 20))
		self.whmanuf = wx.TextCtrl(self.whf, -1, pos = (70, 175), size = (100, 20))
		wx.StaticText(self.whf, -1, u'责任人：', pos = (0, 200), size = (70, 20))
		self.whresp = wx.TextCtrl(self.whf, -1, pos = (70, 200), size = (100, 20))
		wx.StaticText(self.whf, -1, u'批次：', pos = (0, 225), size = (70, 20))
		self.whbatch = wx.TextCtrl(self.whf, -1, pos = (70, 225), size = (100, 20))
		wx.StaticText(self.whf, -1, u'机房名：', pos = (0, 250), size = (70, 20))
		self.whroom = wx.TextCtrl(self.whf, -1, pos = (70, 250), size = (100, 20))

		self.whpostbtn = wx.Button(self.whf, -1, u'添加', pos = (0,275), size = (40, 20))
		self.whf.Bind(wx.EVT_BUTTON, self.addHandle, self.whpostbtn)
		self.whf.Show()

	# incomplete
	def Repair(self, event):
		colLabel = (u'编号', u'费用', u'维修日期', u'修理厂家', u'负责人', u'状态')
		colSize = (30, 50, 70, 80, 55, 50)
		width = 0
		for i in colSize:
			width += i + 1

		self.rf = wx.Dialog(self, -1, u'维修', size = (width, 330), style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX) | wx.FRAME_FLOAT_ON_PARENT)

		wx.StaticText(self.rf, -1, u'损坏设备：', pos = (0, 5), size = (60, 20))
		self.rcb = wx.ComboBox(self.rf, -1, pos = (60, 5), size = (60, 20), choices = self.db.repair_query_id())
		wx.StaticText(self.rf, -1, u'费用：', pos = (130, 5), size = (50, 20))
		self.rcost = wx.TextCtrl(self.rf, -1, pos = (180, 5), size = (50, 20))

		wx.StaticText(self.rf, -1, u'维修日期：', pos = (0, 25), size = (60, 20))
		self.rdate = wx.TextCtrl(self.rf, -1, pos = (60, 25), size = (80, 20))
		wx.StaticText(self.rf, -1, u'修理厂家：', pos = (150, 25), size = (60, 20))
		self.rserv = wx.TextCtrl(self.rf, -1, pos = (210, 25), size = (100, 20))

		wx.StaticText(self.rf, -1, u'负责人：', pos = (0, 45), size = (50, 20))
		self.rresp = wx.TextCtrl(self.rf, -1, pos = (50, 45), size = (70, 20))
		self.rbtn = wx.Button(self.rf, -1, u'添加', pos = (130, 45), size = (50, 20))

		self.rgrid = wx.grid.Grid(self.rf, -1, pos = (0, 65), size = (400, 360))
		self.rgrid.CreateGrid(0, 6)
		self.rgrid.SetRowLabelSize(0)

		for i in range(len(colLabel)):
			self.rgrid.SetColLabelValue(i, colLabel[i])
			self.rgrid.SetColSize(i, colSize[i])

		data = self.db.repair_query()
		j = 0
		for line in data:
			self.rgrid.InsertRows(j)
			for i in range(len(line)):
				if isinstance(line[i], int):
					val = '%d'%line[i]
				else:
					val = line[i]
				self.rgrid.SetCellValue(j, i, val)
				self.rgrid.SetReadOnly(j, i)
			j += 1
			
		self.rf.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.fixHandle)
		self.rf.Show()

	# Sort and refresh data
	def Query(self, event):
		colName = ('Type', 'Name', 'Model', 'Spec', 'Cost', 'Date', 'Manuf', 'Resp', 'Batch', 'Room')
		keyword = colName[self.cb.GetSelection()]
		sort = ['ASC', 'DESC']
		self.refreshData(keyword, sort[self.rb.GetSelection()])

	# Handle the add event
	def addHandle(self, event):
		count = self.whcount.GetValue()
		if count == '0' or not count.isdigit():
			wx.MessageBox(u'数量错误', u'错误', wx.OK | wx.ICON_ERROR)
			return

		cost = self.whcost.GetValue()
		if cost == '0' or not cost.isdigit():
			wx.MessageBox(u'单价错误', u'错误', wx.OK | wx.ICON_ERROR)
			return

		batch = self.whbatch.GetValue()
		if batch == '0' or not batch.isdigit():
			wx.MessageBox(u'批次错误', u'错误', wx.OK | wx.ICON_ERROR)
			return

		for i in range(int(count)):
			self.db.inst_add(self.whtype.GetValue(), self.whname.GetValue(), self.whmodel.GetValue(), self.whspec.GetValue(), int(cost), self.whdate.GetValue(), self.whmanuf.GetValue(), self.whresp.GetValue(), int(batch), self.whroom.GetValue())

		wx.MessageBox(u'添加成功', u'成功')
		self.whf.Destroy()
		self.Query(None)

	def fixHandle(self, event):
		print 'fix'

	def Exit(self, event):
		self.Destroy()
		exit()

if __name__ == '__main__':
	app = wx.App()
	frame = GridFrame(None)
	app.MainLoop()