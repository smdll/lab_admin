# -*- coding: utf-8 -*-

import sqlite3,os,md5

def init():
	if os.path.exists('lab.db'):
		os.remove('lab.db')

	conn = sqlite3.connect('lab.db')
	cur = conn.cursor()
	cur.execute('CREATE TABLE Main(id INTEGER PRIMARY KEY, Type TEXT, Name TEXT, Model TEXT, Spec TEXT, Cost INTEGER, Date TEXT, Manuf TEXT, Resp TEXT, Batch INTEGER, Room TEXT)')
	cur.execute('CREATE TABLE Repair(id INTEGER PRIMARY KEY, Cost INTEGER, Date TEXT, Manuf TEXT, Resp TEXT, Status TEXT)')

	file = open('pre_inst.txt', 'rt')
	for line in file.readlines():
		para = line[:-1].split(',')
		cur.execute("INSERT INTO Main(id, Type, Name, Model, Spec, Cost, Date, Manuf, Resp, Batch, Room) VALUES(%d, '%s', '%s', '%s', '%s', %d, '%s', '%s', '%s', %d, '%s')"%(int(para[0]), para[1], para[2], para[3], para[4], int(para[5]), para[6], para[7], para[8], int(para[9]), para[10]))
	file.close()

	conn.commit()
	conn.close()

if __name__ == "__main__":
	prompt = raw_input('Reset database?(y/n)')
	if prompt == 'y':
		init()
		print 'Database reset'