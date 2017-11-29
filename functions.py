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
		self.cur.execute('INSERT INTO Main(Type, Name, Model, Spec, Cost, Count, Date, Manuf, Resp, Batch) VALUES("%s", "%s", "%s", "%s", %d, %d, "%s", "%s", %d, %d)'%(type, name, model, spec, cost, count, date, manuf, resp, batch + 1))
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

	def inst_query(self):
		list = self.cur.execute('SELECT distinct Name,Model,Batch FROM Main').fetchall()
		result = []
		for i in list:
			result.append(self.cur.execute('SELECT Type,Name,Model,Spec,Cost,Count(Batch),Date,Manuf,Resp,Batch,Room FROM Main WHERE Name="%s" AND Model="%s" AND Batch=%s'%(i[0], i[1], i[2])).fetchone())
		return result