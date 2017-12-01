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
		set = self.cur.execute('SELECT DISTINCT id,Name,Model,Batch FROM Main ORDER BY %s %s'%(keyword, sort)).fetchall()
		result = []
		for i in set:
			temp = list(self.cur.execute('SELECT Type,Name,Model,Spec,Cost,Count(Batch),Date,Manuf,Resp,Batch,Room FROM Main WHERE Name="%s" AND Model="%s" AND Batch=%s ORDER BY %s %s'%(i[1], i[2], i[3], keyword, sort)).fetchone())
			status = self.cur.execute('SELECT Status FROM Repair WHERE id=%s'%(i[0])).fetchone()
			if status == None:
				temp.append(u'正常')
			else:
				temp.append(status[0])
			result.append(temp)
		return result