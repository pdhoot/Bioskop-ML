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
		X=reshape(param(1:self.movies*self.features), self.movies, self.features)
		theta = reshape(params(self.movies*self.features+1:end), self.users, self.features)		
		H = (X.dot(theta.T) - Y)*r
		J = (1.0/2)*np.sum(np.sum(H**2)) + (1.0/2)*lamda*np.sum(np.sum(theta**2)) + (1.0/2)*lamda*np.sum(np.sum(X**2))
		X_grad = H.dot(theta) + lamda*X
		theta_grad = X.T.dot(H) + lamda*theta

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
		param = np.append(self.X.flatten(), self.theta.flatten())
		res1 = optimize.fmin_cg(cost_function, param, args=(Y, r,lamda), maxiter=100, disp=True)

		X=reshape(res1(1:self.movies*self.features), self.movies, self.features)
		theta = reshape(res1(self.movies*self.features+1:end), self.users, self.features)

		pred=X.dot(theta.T);
		predt=pred*(1-r);

		return np.argsort(predt,0)[::-1][:20];

if __name__=="__main__":
	obj = algorithm(10, 10, 10)
	Y = np.array([[1,2,3],[4,5,6],[7,8,9]])
	r = np.array([[0, 1, 0], [1, 0, 1], [1, 1, 1]])
	lamda=10
	print obj.normalize(Y, r)
	print predict(Y,r,lamda)