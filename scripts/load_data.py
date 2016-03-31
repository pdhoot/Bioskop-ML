import numpy as np
import sys

class load_data():

	def __init__(self, file, movies, users):
		self.file = file
		self.movies = movies
		self.users = users

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

		# print Y.shape
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


if __name__=="__main__":
	obj = load_data("../dataset/ratings.dat", 4001, 6041)
	print obj.get_user_movie_mat()