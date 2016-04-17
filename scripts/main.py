from load_data import load_data
import MySQLdb
from ConfigParser import ConfigParser

cfg = ConfigParser()
cfg.read("../config/config.cfg")

host = cfg.get("creds", "host")
user = cfg.get("creds", "user")
passwd = cfg.get("creds", "passwd")
dba = cfg.get("creds", "db")
db = MySQLdb.connect(host,user,passwd,dba)
cursor=db.cursor()

sql="SELECT COUNT(*) FROM USER_DB"

cursor.execute(sql)
r = cursor.fetchall()
users = int(r[0][0])

sql="SELECT COUNT(*) FROM MOVIE_DB"

cursor.execute(sql)
r = cursor.fetchall()
movies = int(r[0][0])

f1 = "../dataset/ratings.dat"
f2 = "../dataset/users.dat"
f3 = "../dataset/movies.dat"
l1 = load_data(f1, f2, f3, movies+1, users+1)

l1.pred_update()
l1.find_similar_movies()
l1.make_recommendation()
l1.valid_count()