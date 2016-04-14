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
		obj.init_data()
		lamda=5
		(pred,X)=obj.predict(Y,r,lamda)
		pred = pred*((1-r).T)
		print "Done!"

		#Inserting predictions and fetures in DB
		sql="DELETE FROM PRED_DB WHERE 1"
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
			sys.exit(1)

		sql=" INSERT INTO PRED_DB(id, prediction) VALUES(%s, %s)"

		for i in range(1,self.users):
			str1 = ','.join(["%.2f" % e for e in pred[i]])
			st = (i, str1)
			cursor.execute(sql,st)
		db.commit()


		sql="DELETE FROM FEAT_DB WHERE 1"
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
			sys.exit(1)

		sql=" INSERT INTO FEAT_DB(id, features) VALUES(%s, %s)"

		for i in range(1,self.movies):
			str1 = ','.join(["%.2f" % e for e in X[i]])
			st = (i, str1)
			cursor.execute(sql,st)
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

	def find_similar_movies(self):
		cfg = ConfigParser()
		cfg.read("../config/config.cfg")

		host = cfg.get("creds", "host")
		user = cfg.get("creds", "user")
		passwd = cfg.get("creds", "passwd")
		dba = cfg.get("creds", "db")

		db = MySQLdb.connect(host,user,passwd,dba)
		cursor=db.cursor()

		sql='''SELECT features FROM FEAT_DB ORDER BY id ASC'''

		cursor.execute(sql)
		results = cursor.fetchall()

		results=["0"] + list(results)

		l = len(results)
		T = 10
		X = np.zeros((l, T))

		print "[*] Finding Similar movies"

		for i in xrange(1, l):
			x = [(0, 0)]*(l)
			for j in xrange(1, l):
				if i==j:
					continue
				d = self.find_distance(results, i, j)
				x[j] = (d, j)
			x.sort()
			y = [j for k, j in x]
			y = y[2:T+2]
			X[i, :] = y

		sql="DELETE FROM SIM_DB WHERE 1"
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
			sys.exit(1)

		print "[*] Inserting into DB"
		sql='''INSERT INTO SIM_DB(id, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
		
		for i in xrange(1,l):
			t = list(X[i, :])
			t = [int(j) for j in t]
			t = [i]+t
			st = tuple(t)
			cursor.execute(sql, st)

		db.commit()
		db.close()

	def find_distance(self, results, i, j):
		r1 = results[i][0]
		r1 = r1.split(',')

		r2 = results[j][0]
		r2 = r2.split(',')

		d = [(float(x)-float(y))**2 for x, y in zip(r1, r2)]
		return sum(d)
	
	def make_recommendation(self):
		cfg = ConfigParser()
		cfg.read("../config/config.cfg")

		host = cfg.get("creds", "host")
		user = cfg.get("creds", "user")
		passwd = cfg.get("creds", "passwd")
		dba = cfg.get("creds", "db")

		db = MySQLdb.connect(host,user,passwd,dba)
		cursor=db.cursor()

		sql='''SELECT prediction FROM PRED_DB ORDER BY id ASC'''

		cursor.execute(sql)
		results = cursor.fetchall()
		results=["0"] + list(results)

		l = len(results)
		T = 10
		X = np.zeros((l, T))

		for i in xrange(1, l):
			x = results[i][0].split(',')
			x = [float(j) for j in x]
			y = [(x[j], j) for j in xrange(1, len(x))]
			y.sort(reverse=True)
			x = [j for k, j in y]
			X[i, :] = x[:T]

		sql="DELETE FROM RECO_DB WHERE 1"
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
			sys.exit(1)

		print "[*] Inserting into DB"
		sql='''INSERT INTO RECO_DB(id, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
		
		for i in xrange(1,l):
			t = list(X[i, :])
			t = [int(j) for j in t]
			t = [i]+t
			st = tuple(t)
			cursor.execute(sql, st)

		db.commit()
		db.close()	


if __name__=="__main__":
	obj = load_data("../dataset/ratings.dat", 4001, 6041)
	print obj.get_user_movie_mat()