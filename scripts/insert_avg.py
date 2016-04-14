from ConfigParser import ConfigParser
import MySQLdb

def insert_average_ratings(num_movies):
	cfg = ConfigParser()
	cfg.read("../config/config.cfg")

	host = cfg.get("creds", "host")
	user = cfg.get("creds", "user")
	passwd = cfg.get("creds", "passwd")
	dba = cfg.get("creds", "db")

	db = MySQLdb.connect(host,user,passwd,dba)
	cursor=db.cursor()
	sql="SELECT * FROM LOGS_DB"
	try:
		cursor.execute(sql);
		results=cursor.fetchall()
	except:
		print "Error: unable to fecth data"
		sys.exit(1)
	db.close()

	avg_ratings = [0]*(num_movies+1)
	count = [0]*(num_movies+1)

	for r in results:
		avg_ratings[r[1]]+=r[2]
		count[r[1]]+=1

	for i in xrange(len(avg_ratings)):
		if count[i]>10:
			avg_ratings[i] = (1.0*avg_ratings[i])/count[i]
		else:
			avg_ratings[i] = -1

	db = MySQLdb.connect(host,user,passwd,dba)
	cursor=db.cursor()

	sql = '''ALTER TABLE MOVIE_DB ADD rating DOUBLE'''
	cursor.execute(sql)
	db.commit()


	db = MySQLdb.connect(host,user,passwd,dba)
	cursor=db.cursor()

	sql=" UPDATE MOVIE_DB SET rating = %s WHERE id = %s"

	for i in range(1,num_movies+1):
		st = (avg_ratings[i], i)
		cursor.execute(sql,st)
	db.commit()

insert_average_ratings(3952)