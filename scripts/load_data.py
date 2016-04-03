import numpy as np
import sys
import MySQLdb
from ConfigParser import ConfigParser
from algorithm import algorithm

class load_data():

	def __init__(self, file,ufile,mfile ,movies=0, users=0):
		self.file = file
		self.movies = movies
		self.users = users
		self.ufile=ufile
		self.mfile=mfile

	def get_movies_for_indexes(self,idx):
		try:
			f = open(self.file, "r")
		except:
			print >> sys.stderr, "[ERR] Failed to open file"
			sys.exit(1)
		else:
			data = f.read()
			f.close()

		logs = data.split('\n')
		if not logs[-1]:
			logs = logs[0:-1]
		logs = [(int(c.split("::")[0]), c.split("::")[1]) for c in logs]
		logs = dict(logs)

		for i in idx:
			print logs[i]
		

	def get_user_movie_mat(self):
		try:
			f = open(self.file, "r")
		except:
			print >> sys.stderr, "[ERR] Failed to open file"
			sys.exit(1)
		else:
			data = f.read()
			f.close()

		return self.parse_data(data)

	def parse_data(self, data):
		Y = np.zeros((self.movies, self.users))
		r = np.zeros((self.movies, self.users))

		# This code uses indexing from 1, not 0
		logs = data.split('\n')
		if not logs[-1]:
			logs = logs[0:-1]
		logs = [(int(c.split("::")[0]), int(c.split("::")[1]), int(c.split("::")[2])) for c in logs]
		for x in logs:
			try:
				Y[x[1]][x[0]] = x[2]
				r[x[1]][x[0]] = 1
			except:
				print >> sys.stderr,"[ERR]", x[0], x[1], x[2]
				print >> sys.stderr , Y
				sys.exit(1)
		return (Y, r)


	def pred_update(self):
		#load Y and r from Logs database 
		Y = np.zeros((self.movies, self.users))
		r = np.zeros((self.movies, self.users))

		cfg = ConfigParser()
		cfg.read("../config/config.cfg")

		host = cfg.get("creds", "host")
		user = cfg.get("creds", "user")
		passwd = cfg.get("creds", "passwd")
		db = cfg.get("creds", "db")

		db = MySQLdb.connect(host,user,passwd,db)
		cursor=db.cursor()
		sql="SELECT * FROM LOGS_DB"
		try:
			cursor.execute(sql);
			results=cursor.fetchall()

			for row in results:
				u=row[0]
				m=row[1]
				rate=row[2]
				r[m][u]=1
				Y[m][u]=rate

		except:
			print "Error: unable to fecth data"
			sys.exit(1)

		#Predicting
		obj =algorithm(self.movies,100,self.users)
		lamda=5
		(pred,X)=obj.predict(Y,r,lamda)


		#Inserting predictions and fetures in DB
		sql="DELETE * FROM PRED_DB"
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
			sys.exit(1)

		sql=" INSERT INTO PRED_DB(predi) VALUES(%s)"

		for i in range(1,self.movies+1):
			str1 = ','.join([str(e) for e in pred[i]])
			cursor.execute(sql,str1)
			db.commit()


		sql="DELETE * FROM FEAT_DB"
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
			sys.exit(1)

		sql=" INSERT INTO FEAT_DB(feati) VALUES(%s)"

		for i in range(1,self.movies+1):
			str1 = ','.join(["%.2f" % e for e in X[i]])
			cursor.execute(sql,str1)
			db.commit()

		db.close()


	def initialize_rdb(self):
		try:
			f = open(self.file, "r")
		except:
			print >> sys.stderr, "[ERR] Failed to open file"
			sys.exit(1)
		else:
			data = f.read()
			f.close()

		# This code uses indexing from 1, not 0
		logs = data.split('\n')
		if not logs[-1]:
			logs = logs[0:-1]
		logs = [(int(c.split("::")[0]), int(c.split("::")[1]), int(c.split("::")[2])) for c in logs]

		cfg = ConfigParser()
		cfg.read("../config/config.cfg")

		host = cfg.get("creds", "host")
		user = cfg.get("creds", "user")
		passwd = cfg.get("creds", "passwd")
		db = cfg.get("creds", "db")

		db = MySQLdb.connect(host,user,passwd,db)
		cursor=db.cursor()

		sql='''INSERT INTO LOGS_DB(user,movie,rating) VALUES(%s,%s,%s)'''
		cursor.executemany(sql, logs)
		db.commit()
		db.close()


	def initialize_udb(self):
		try:
			f = open(self.ufile, "r")
		except:
			print >> sys.stderr, "[ERR] Failed to open file"
			sys.exit(1)
		else:
			data = f.read()
			f.close()

		logs = data.split('\n')
		if not logs[-1]:
			logs = logs[0:-1]
		logs = [(int(c.split("::")[0]), c.split("::")[1], int(c.split("::")[2]) ,int(c.split("::")[3])) for c in logs]

		cfg = ConfigParser()
		cfg.read("../config/config.cfg")

		host = cfg.get("creds", "host")
		user = cfg.get("creds", "user")
		passwd = cfg.get("creds", "passwd")
		db = cfg.get("creds", "db")

		db = MySQLdb.connect(host,user,passwd,db)
		cursor=db.cursor()

		sql=" INSERT INTO USER_DB(id,gender,age,occu) VALUES(%s,%s,%s,%s)"

		i = 0
		l = len(logs)

		cursor.executemany(sql, logs)
		db.commit()
		db.close()


	def initialize_mdb(self):
		try:
			f = open(self.mfile, "r")
		except:
			print >> sys.stderr, "[ERR] Failed to open file"
			sys.exit(1)
		else:
			data = f.read()
			f.close()

		logs = data.split('\n')
		if not logs[-1]:
			logs = logs[0:-1]
		logs = [(int(c.split("::")[0]), c.split("::")[1], c.split("::")[2])  for c in logs]

		cfg = ConfigParser()
		cfg.read("../config/config.cfg")

		host = cfg.get("creds", "host")
		user = cfg.get("creds", "user")
		passwd = cfg.get("creds", "passwd")
		db = cfg.get("creds", "db")

		db = MySQLdb.connect(host,user,passwd,db)
		cursor=db.cursor()

		sql='''INSERT INTO MOVIE_DB(id,movie,genre) VALUES(%s,%s,%s)'''

		cursor.executemany(sql, logs)
		db.commit()
		db.close()


if __name__=="__main__":
	obj = load_data("../dataset/ratings.dat", 4001, 6041)
	print obj.get_user_movie_mat()