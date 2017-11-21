# -*- coding: utf-8 -*-

import sqlite3,os

def init():
	if os.path.exists('lab.db'):
		os.remove('lab.db')

	conn = sqlite3.connect('lab.db')
	cur = conn.cursor()

	cur.execute('CREATE TABLE Instrument(id INTEGER PRIMARY KEY, Type TEXT, Name TEXT, Model TEXT, Spec TEXT, Cost INTEGER, Count INTEGER, Date TEXT, Manuf TEXT, Resp INTEGER, Batch INTEGER)')
	cur.execute('CREATE TABLE Admin(id INTEGER PRIMARY KEY, Name TEXT, Pass CHAR(32))');
	cur.execute('CREATE TABLE Repair(id INTEGER PRIMARY KEY, Date DATE, Name TEXT, Host TEXT, Cost INTEGER, Resp INTEGER)')
	cur.execute('CREATE TABLE DPC(Type TEXT, Name TEXT, Model TEXT, Spec TEXT, Count INTEGER, Date TEXT, Resp INTEGER)')

	file = open('pre_inst.txt', 'rt')
	for line in file.readlines():
		para = line[:-1].split(',')
		# print para
		cur.execute("INSERT INTO Instrument VALUES(%d, '%s', '%s', '%s', '%s', %d, %d, '%s', '%s', %d, %d)"%(int(para[0]), para[1], para[2], para[3], para[4], int(para[5]), int(para[6]), para[7], para[8], int(para[9]), int(para[10])))
	file.close()

	# file = open('pre_employee.txt', 'rt')
	# for line in file.readlines():
		# para = line[:-1].split(',')
		# cur.execute("INSERT INTO Employee VALUES(%d, '%s', '%s', '%s', %d, '%s')"%(int(para[0]), para[1], para[2], para[3], int(para[4]), para[5]))
	# file.close()

	# file = open('pre_client.txt', 'rt')
	# for line in file.readlines():
		# para = line[:-1].split(',')
		# cur.execute("INSERT INTO Client VALUES(%d, '%s', '%s', %d)"%(int(para[0]), para[1], para[2], int(para[3])))
	# file.close()
	conn.commit()
	conn.close()

if __name__ == "__main__":
	prompt = raw_input('Reset database?(y/n)')
	if prompt == 'y':
		init()
		print 'Database reset'