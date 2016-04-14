from ConfigParser import ConfigParser
import MySQLdb
import md5
import sys

def add_user_pass(num_users):
	cfg = ConfigParser()
	cfg.read("../config/config.cfg")

	host = cfg.get("creds", "host")
	user = cfg.get("creds", "user")
	passwd = cfg.get("creds", "passwd")
	dba = cfg.get("creds", "db")

	m = md5.new()
	m.update("a")
	passhash = m.hexdigest()

	db = MySQLdb.connect(host,user,passwd,dba)
	cursor=db.cursor()
	sql='''ALTER TABLE USER_DB ADD username VARCHAR(100)'''
	cursor.execute(sql)
	db.commit()
	db.close()

	db = MySQLdb.connect(host,user,passwd,dba)
	cursor=db.cursor()
	sql='''ALTER TABLE USER_DB ADD password VARCHAR(100)'''
	cursor.execute(sql)
	db.commit()
	db.close()

	db = MySQLdb.connect(host,user,passwd,dba)
	cursor=db.cursor()
	sql='''UPDATE USER_DB SET username = %s , password = %s WHERE id = %s'''
	s = "random"
	for i in xrange(1, num_users+1):
		n = s + `i`
		st = (n, passhash, i)
		cursor.execute(sql, st)

	db.commit()
	db.close()

add_user_pass(6040)