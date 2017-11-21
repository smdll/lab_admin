# -*- coding: utf-8 -*-

import sqlite3,sys
class lab_db:
	def __init__(self):
		self.conn = sqlite3.connect('lab.db')
		self.cur = self.conn.cursor()

	def __del__(self):
		self.conn.close()

	def close(self):
		self.conn.commit()
		self.conn.close()

	def inst_add(self, type, name, model, spec, cost, count, date, manuf, resp):
		# type = type.decode(sys.stdin.encoding).encode('UTF-8')
		# name = name.decode(sys.stdin.encoding).encode('UTF-8')
		# model = model.decode(sys.stdin.encoding).encode('UTF-8')
		# spec = spec.decode(sys.stdin.encoding).encode('UTF-8')
		# manuf = manuf.decode(sys.stdin.encoding).encode('UTF-8')
		batch = self.cur.execute('SELECT Batch FROM Instrument WHERE Name="%s" AND Model="%s" ORDER BY Batch DESC'%(name, model)).fetchone()
		if batch == None:
			batch = 0
		else:
			batch = batch[0]
		self.cur.execute('INSERT INTO Instrument(Type, Name, Model, Spec, Cost, Count, Date, Manuf, Resp, Batch) VALUES("%s", "%s", "%s", "%s", %d, %d, "%s", "%s", %d, %d)'%(type, name, model, spec, cost, count, date, manuf, resp, batch + 1))
		self.conn.commit()

	def inst_repair(self, id, count):
		list = self.cur.execute('SELECT Count FROM Instrument WHERE id=%d'%id).fetchall()
		print list
		# self.cur.execute('DELETE FROM Drug WHRER Did=%d'%Did)
		# self.conn.commit()

	def inst_done_repair(self, Did, add):
		count = self.drug_query('Did', Did, 'Dcount').fetchone()[0]
		count += add
		self.cur.execute('UPDATE Drug SET Dcount=%d WHRER Did=%d'%(count, Did))
		self.commit()

	def inst_query(self, arg):
		return self.cur.execute('SEKECT * FROM Insteument ORDER BY %s'%arg).fetchall()

	def inst_get_count():
		return 

d = lab_db()
d.inst_repair(1, 1)