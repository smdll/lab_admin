# -*- coding: utf-8 -*-

import sqlite3

class lab_db:
	def __init__(self):
		self.conn = sqlite3.connect('lab.db')
		self.cur = self.conn.cursor()

	def __del__(self):
		self.conn.close()

	def close(self):
		self.conn.commit()
		self.conn.close()

	def inst_add(self, type, name, model, spec, cost, date, manuf, resp, batch, room):
		self.cur.execute('INSERT INTO Main(Type,Name,Model,Spec,Cost,Date,Manuf,Resp,Batch,Room) VALUES("%s", "%s", "%s", "%s", %d, "%s", "%s", "%s", %d, "%s")'%(type, name, model, spec, cost, date, manuf, resp, batch, room))
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

	def inst_query(self, keyword, sort):
		list = self.cur.execute('SELECT distinct Name,Model,Batch FROM Main ORDER BY %s %s'%(keyword, sort)).fetchall()
		result = []
		for i in list:
			result.append(self.cur.execute('SELECT Type,Name,Model,Spec,Cost,Count(Batch),Date,Manuf,Resp,Batch,Room FROM Main WHERE Name="%s" AND Model="%s" AND Batch=%s ORDER BY %s %s'%(i[0], i[1], i[2], keyword, sort)).fetchone())
		return result