# -*- coding: utf-8 -*-
import wx
import wx.grid
import functions

class LoginFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title = u"登陆", size = (100, 120), style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

		wx.StaticText(self, -1, u'用户名：', pos = (0, 0))
		self.uname = wx.TextCtrl(self, -1, pos = (50, 0))
		wx.StaticText(self, -1, u'密码：', pos = (0, 30))
		self.upass = wx.TextCtrl(self, -1, pos = (50, 30), style = wx.TE_PASSWORD)
		self.logbtn = wx.Button(self, -1, u'登录', pos = (0, 60), size = (75, 30))
		self.anobtn = wx.Button(self, -1, u'游客登录', pos = (80, 60), size = (75, 30))

		self.Bind(wx.EVT_BUTTON, self.Log, self.logbtn)
		self.Bind(wx.EVT_BUTTON, self.AnoLog, self.anobtn)
		self.Bind(wx.EVT_CLOSE, self.Exit)

		self.Show()

	def Log(self, event):
		db = functions.lab_db()
		uname = self.uname.GetValue()
		upass = self.upass.GetValue()
		id = db.admin_query(uname, upass)
		if id == -1:
			dialog = wx.MessageDialog(self, u'用户名或密码不正确', style = wx.OK|wx.STAY_ON_TOP|wx.CENTRE)
			dialog.ShowModal()
			dialog.Destroy()
		else:
			self.Show(False)
			print 'Logged in, id:',id
			exit()

	def AnoLog(self, event):
		self.Show(False)
		grid = GridFrame(None)

	def Exit(self, event):
		self.Show(False)
		exit()

class GridFrame(wx.Frame):
	colLabel = (u'编号', u'类别', u'设备名', u'型号', u'规格', u'单价', u'数量', u'购置日期', u'生产厂家', u'购买人', u'批次', u'状态')
	colSize = (30, 80, 200, 50, 50, 50, 30, 70, 80, 55, 30, 40)
	def __init__(self, parent):
		width = 0
		for i in self.colSize:
			width += i + 1
		wx.Frame.__init__(self, parent, size = (width, 360), style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

		grid = wx.grid.Grid(self, -1)

		db = functions.lab_db()
		data = db.inst_query('id', 'ASC')

		grid.CreateGrid(0, len(data[0]))
		grid.SetRowLabelSize(0)

		for i in range(len(self.colLabel)):
			grid.SetColLabelValue(i, self.colLabel[i])
			grid.SetColSize(i, self.colSize[i])

		j = 0
		for line in data:
			grid.InsertRows(j)
			for i in range(len(self.colLabel)):
				if isinstance(line[i], int):
					val = '%d'%line[i]
				else:
					val = line[i]
				grid.SetCellValue(j, i, val)
				grid.SetReadOnly(j, i)
			j += 1
		self.Bind(wx.EVT_CLOSE, self.Exit)
		self.Show()
	
	def Exit(self, event):
		self.Show(False)
		exit()

if __name__ == '__main__':
	app = wx.App()
	frame = LoginFrame(None)
	app.MainLoop()