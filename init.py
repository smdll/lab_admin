# -*- coding: utf-8 -*-
import sqlite3,os,md5

def init():
	if os.path.exists('lab.db'):
		os.remove('lab.db')

	conn = sqlite3.connect('lab.db')
	cur = conn.cursor()

	cur.execute('CREATE TABLE Instrument(id INTEGER PRIMARY KEY, Type TEXT, Name TEXT, Model TEXT, Spec TEXT, Cost INTEGER, Count INTEGER, Date TEXT, Manuf TEXT, Resp INTEGER, Batch INTEGER, Status TEXT)')
	cur.execute('CREATE TABLE Admin(id INTEGER PRIMARY KEY, Name TEXT, User TEXT, Pass TEXT)');

	file = open('pre_inst.txt', 'rt')
	for line in file.readlines():
		para = line[:-1].split(',')
		cur.execute("INSERT INTO Instrument(Type, Name, Model, Spec, Cost, Count, Date, Manuf, Resp, Batch, Status) VALUES('%s', '%s', '%s', '%s', %d, %d, '%s', '%s', %d, %d, '%s')"%(para[0], para[1], para[2], para[3], int(para[4]), int(para[5]), para[6], para[7], int(para[8]), int(para[9]), para[10]))
	file.close()

	file = open('pre_admin.txt', 'rt')
	for line in file.readlines():
		para = line[:-1].split(',')
		user = md5.new(para[1])
		passw = md5.new(para[2]) 
		cur.execute("INSERT INTO Admin(Name, User, Pass) VALUES('%s', '%s', '%s')"%(para[0], user.hexdigest(), passw.hexdigest()))
	file.close()

	conn.commit()
	conn.close()

if __name__ == "__main__":
	prompt = raw_input('Reset database?(y/n)')
	if prompt == 'y':
		init()
		print 'Database reset'