# -*- coding: utf-8 -*-

import sqlite3,sys,md5

class lab_db:
	def __init__(self):
		self.conn = sqlite3.connect('lab.db')
		self.cur = self.conn.cursor()

	def __del__(self):
		self.conn.close()

	def close(self):
		self.conn.commit()
		self.conn.close()

	# incomplete
	def inst_add(self, type, name, model, spec, cost, count, date, manuf, resp):
		batch = self.cur.execute('SELECT Batch FROM Instrument WHERE Name="%s" AND Model="%s" ORDER BY Batch DESC'%(name, model)).fetchone()
		if batch == None:
			batch = 0
		else:
			batch = batch[0]
		self.cur.execute('INSERT INTO Instrument(Type, Name, Model, Spec, Cost, Count, Date, Manuf, Resp, Batch) VALUES("%s", "%s", "%s", "%s", %d, %d, "%s", "%s", %d, %d)'%(type, name, model, spec, cost, count, date, manuf, resp, batch + 1))
		self.conn.commit()

	# incomplete
	def inst_repair(self, id, count):
		list = self.cur.execute('SELECT Count FROM Instrument WHERE id=%d'%id).fetchall()

	# incomplete
	def inst_done_repair(self, Did, add):
		count = self.drug_query('Did', Did, 'Dcount').fetchone()[0]
		count += add
		self.cur.execute('UPDATE Drug SET Dcount=%d WHRER Did=%d'%(count, Did))
		self.commit()

	def inst_query(self, order, sort):
		list = []
		query = self.cur.execute('SELECT * FROM Instrument ORDER BY %s %s'%(order, sort)).fetchall()
		for i in query:
			temp = []
			for j in range(len(i)):
				if j == 9:
					name = self.cur.execute('SELECT Name FROM Admin where id=%d'%(i[9])).fetchone()
					temp.append(name)
				else:
					temp.append(i[j])
			list.append(temp)
		return list

	def admin_query(self, user, passw):
		md5_user = md5.new(user)
		md5_pass = md5.new(passw)
		id = self.cur.execute('SELECT ID FROM Admin WHERE User="%s" AND Pass="%s"'%(md5_user.hexdigest(), md5_pass.hexdigest())).fetchone()
		if id == None:
			return -1
		return id