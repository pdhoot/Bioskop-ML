from load_data import load_data
from numpy.random import standard_normal as randn
import numpy as np
from scipy import optimize

class algorithm():

	def __init__(self, num_movies, num_features, num_users):
		self.movies = num_movies
		self.users  = num_users
		self.features = num_features

	def init_data(self):
		self.theta = randn((self.users, self.features))
		self.X = randn((self.movies, self.features))

	def cost_function(self, param,Y, r, lamda):
		X=np.reshape(param[:self.movies*self.features], (self.movies, self.features))
		theta = np.reshape(param[self.movies*self.features:], (self.users, self.features))
		H = (X.dot(theta.T) - Y)*r
		J = (1.0/2)*np.sum(np.sum(H**2)) + (1.0/2)*lamda*np.sum(np.sum(theta**2)) + (1.0/2)*lamda*np.sum(np.sum(X**2))
		return J

	def gradient(self, param, Y, r , lamda):
		X=np.reshape(param[:self.movies*self.features], (self.movies, self.features))
		theta = np.reshape(param[self.movies*self.features:], (self.users, self.features))
		H = (X.dot(theta.T) - Y)*r
		X_grad = H.dot(theta) + lamda*X
		theta_grad = H.T.dot(X) + lamda*theta
		grad = np.append(X_grad.flatten(), theta_grad.flatten())
		return grad

	def normalize(self, Y, r):
		(m, n) = Y.shape
		Ymean = np.zeros((m,1))
		Ynorm = np.zeros(Y.shape)
		for i in xrange(m):
			idx = np.where(r[i]==1)
			t = Y[i][idx]
			Ymean[i] = np.sum(t)/len(t)
			Ynorm[i][idx] = Y[i][idx]-Ymean[i]
		return (Ynorm, Ymean)

	def predict(self,Y,r,lamda):
		print "[OK] Predict called!"
		param = np.append(self.X.flatten(), self.theta.flatten())
		res1 = optimize.fmin_cg(self.cost_function, param, fprime=self.gradient, args=(Y, r,lamda), maxiter=100, disp=True)

		X=np.reshape(res1[:self.movies*self.features], (self.movies, self.features))
		theta = np.reshape(res1[self.movies*self.features:], (self.users, self.features))

		pred=X.dot(theta.T)
		#predt=pred*(1-r);

		# np.savetxt("temp.txt", pred[:, -1])

		return (pred,X)

if __name__=="__main__":
	obj = algorithm(1800, 100, 2001)
	lamda=5
	L = load_data("../dataset/ratings.dat", 3953, 6041)

	(Y, r) = L.get_user_movie_mat()
	Y = Y[0:1800,0:2000]
	r = r[0:1800, 0:2000]

	t1 = np.zeros((1800, 1))
	t2 = np.zeros((1800, 1))

	t1[1] = 3
	t1[318] = 5
	t1[527] = 5 
	t1[1721] = 5 
	t1[1475] = 2 
	t1[1246] = 4.5
	t1[296] = 4.5 
	t1[356] = 4.5 
	t1[1203] = 3.5
	t1[858] = 5
	t1[1221] = 4.5
	t1[1377] = 2

	t2[1] = 1
	t2[318] = 1
	t2[527] = 1
	t2[1721] = 1
	t2[1475] = 1
	t2[1246] = 1
	t2[296] = 1
	t2[356] = 1
	t2[1203] = 1
	t2[858] = 1
	t2[1221] = 1
	t2[1377] = 1

	Y = np.concatenate((Y, t1), axis=1)
	r = np.concatenate((r, t2), axis=1)

	# r = r[0:100,0:100]
	# print obj.normalize(Y, r)
	print Y.shape
	print r.shape
	obj.init_data()
	l2 = load_data("../dataset/movies.dat")
	l2.get_movies_for_indexes(obj.predict(Y,r,lamda)[:, -1])