import numpy as np

class Red:
	def __init__(self):
		pass

	def model(self,X_train, Y_train, X_test, Y_test, num_iterations, learning_rate, print_cost):
		n = X_train.shape[0]										#tamanio del set de entrenamiento				
		print('in model n is: '+str(n))
		w, b = self.zeros(n)										#inicializacion de pesos[n,1] y bias en 0s
		parameters, grads, costs = self.opt(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost) #obtiene parametros(w,b) gradientes y costo
		w = parameters["w"]
		b = parameters["b"]	
		Y_prediction_test = self.predict(w, b, X_test)
		Y_prediction_train = self.predict(w, b, X_train)
		print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
		print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

		
		d = {"costs": costs,
			"Y_prediction_test": Y_prediction_test, 
			"Y_prediction_train" : Y_prediction_train, 
			"w" : w, 
			"b" : b,
			"learning_rate" : learning_rate,
			"num_iterations": num_iterations}
		
		return d

	def zeros(self,d):		
		w=np.zeros((d,1))
		b=0.0
		assert(w.shape==(d,1))
		assert(isinstance(b,float) or isinstance(b,int))
		return w,b

	def opt(self,w,b,X,Y,it,a,pc=False):
		costs=[]
	
		for i in range(it):

			grads, cost = self.prop(w, b, X, Y)

			dw = grads["dw"]
			db = grads["db"]
				
			w = w - a * dw
			b = b - a * db
				
			if i % 100 == 0:
				costs.append(cost)
			   
			if pc and i % 100 == 0:
				print ("Cost after iteration %i: %f" %(i, cost))
		
		params = {"w": w,
		          "b": b}
		
		grads = {"dw": dw,
		         "db": db}
		
		return params, grads, costs

	def sigmoid(self,z):
		s=1/(1+np.exp(-z))
		return s

	def prop(self,w,b,X,Y):
		m=X.shape[1]		#m tiene el tamanio de las columnas de X train
		Z=w.T.dot(X)+b
		A=self.sigmoid(Z)
		J=(-1/m)*np.sum((Y*np.log(A))+(1-Y)*np.log(1-A))
		dz=A-Y
		dw=(1/m)*np.dot(X,dz.T)
		db=(1/m)*np.sum(dz)

		J=np.squeeze(J)

		grads={"dw":dw, "db":db}

		return grads, J

	def predict(self,w, b, X):

		m = X.shape[1]
		Y_prediction = np.zeros((1,m))
		print("w: "+str(w.shape))
		w = w.reshape(X.shape[0], 4)

		A = self.sigmoid(w.T.dot(X) + b)
		
		for i in range(A.shape[1]):
		    Y_prediction[0,i] = 0 if (A[0,i] <= 0.5) else 1
		
		assert(Y_prediction.shape == (1, m))
		
		return Y_prediction

	

	###d = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations = 2000, learning_rate = 0.005, print_cost = True)
