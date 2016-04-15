import MySQLdb
import time
import datetime
db=MySQLdb.connect("localhost","root","1234","bioskop")
cursor=db.cursor()

sql="ALTER TABLE MOVIE_DB ADD %s VARCHAR(20000)" % ("description")

cursor.execute(sql)

sql="ALTER TABLE MOVIE_DB ADD %s VARCHAR(1000)" % ("icon")

cursor.execute(sql)

sql="ALTER TABLE MOVIE_DB ADD %s INT(20)" % ("time")

cursor.execute(sql)

sql="ALTER TABLE MOVIE_DB ADD %s VARCHAR(50)" % ("trailer")

cursor.execute(sql)

sql="UPDATE MOVIE_DB SET description=%s, icon=%s, time=%s ,trailer=%s WHERE movie=%s"

txt=open('../dataset/desc.txt')

for line in txt.readlines():
	#print line
	movie=line.split('::')[1]
	desc=line.split('::')[2]
	icon=line.split('::')[4]
	time=line.split('::')[5]
	trailer=line.split('::')[6]
	trailer=trailer[0:11]

	ti=int(time)

	movie+=" ("+datetime.datetime.fromtimestamp(ti).strftime('%Y')+")"

	data=(desc,icon,time,trailer,movie)

	#print icon,time

	cursor.execute(sql,data)

db.commit()

db.close()