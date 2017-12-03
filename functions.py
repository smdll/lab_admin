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
		set = self.cur.execute('SELECT DISTINCT Name,Model,Batch FROM Main WHERE id!=(SELECT id FROM Repair) ORDER BY %s %s'%(keyword, sort)).fetchall()
		repair_set = self.cur.execute('SELECT id,Name,Model,Batch FROM Main WHERE id IN (SELECT id FROM Repair) ORDER BY %s %s'%(keyword, sort)).fetchall()
		result = []
		for i in set:
			temp = list(self.cur.execute('SELECT Type,Name,Model,Spec,Cost,Count(Batch),Date,Manuf,Resp,Batch,Room FROM Main WHERE Name="%s" AND Model="%s" AND Batch=%s'%(i[0], i[1], i[2])).fetchone())
			temp.append(u'正常')
			result.append(temp)
		for i in repair_set:
			temp = list(self.cur.execute('SELECT Type,Name,Model,Spec,Cost,Count(Batch),Date,Manuf,Resp,Batch,Room FROM Main WHERE Name="%s" AND Model="%s" AND Batch=%s'%(i[1], i[2], i[3])).fetchone())
			temp.append(self.cur.execute('SELECT Status FROM Repair WHERE id=%d'%(i[0])).fetchone()[0])
			result.append(temp)
		return result

	def repair_query_id(self):
		data = self.cur.execute('SELECT id FROM Main WHERE id NOT IN (SELECT ID FROM Repair)').fetchall()
		result = []
		for i in data:
			result.append('%d'%i[0])
		return result

	def repair_query(self):
		data = self.cur.execute('SELECT * FROM Repair').fetchall()
		return data