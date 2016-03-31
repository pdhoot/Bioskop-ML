from load_data import load_data
from numpy.random import standard_normal as randn
import numpy as np

class algorithm():

	def __init__(self, num_movies, num_features, num_users):
		self.movies = num_movies
		self.users  = num_users
		self.features = num_features

	def init_data(self):
		self.theta = randn((self.users, self.features))
		self.X = randn((self.movies, self.features))

	def cost_function(self, Y, r, lamda):
		H = (self.X.dot(self.theta.T) - Y)*r
		J = (1.0/2)*np.sum(np.sum(H**2)) + (1.0/2)*lamda*np.sum(np.sum(self.theta**2)) + (1.0/2)*lamda*np.sum(np.sum(self.X**2))
		X_grad = H.dot(self.theta) + lamda*self.X
		theta_grad = self.X.T.dot(H) + lamda*self.theta

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


if __name__=="__main__":
	obj = algorithm(10, 10, 10)
	Y = np.array([[1,2,3],[4,5,6],[7,8,9]])
	r = np.array([[0, 1, 0], [1, 0, 1], [1, 1, 1]])
	print obj.normalize(Y, r)