import numpy as np
import h5py
import scipy
from PIL import Image
from scipy import ndimage

class Red:

	def __init__(self):
		pass

	def sigmoide(self,z):
		s = 1 / (1 + (np.exp(-z)))
		return s

	def inicializa_con_ceros(self,dim):
		w=np.zeros((dim,1))
		b = 0
	
		assert(w.shape == (dim,1))
		assert(isinstance(b, float) or isinstance(b, int))
	
		return w,b

	def propagar(self, w, b, X, Y):

		m = X.shape[1]
	
		Z = np.dot(w.T,X)+b
		A = self.sigmoide(Z)
		costo = -1 / m * np.sum(Y*np.log(A)+(1-Y)*np.log(1-A), axis = 1, keepdims = True)
	
		dz = A - Y
		dw = 1 / m * np.dot(X,dz.T)
		db = 1 / m * np.sum(A-Y)
	
		costo = np.squeeze(costo)
		assert(costo.shape == ())
	
		gradientes = {"dw":dw, "db":db}
	
		return gradientes, costo

	def optimizar(self, w, b, X, Y, num_iteraciones, tasa_aprendizaje, imprimir_costo = False):

		costos = []
	
		for i in range(num_iteraciones):
		
			gradientes, costo = self.propagar(w, b, X, Y)
		
			dw = gradientes["dw"]
			db = gradientes["db"]
		
			w = w - tasa_aprendizaje * dw
			b = b - tasa_aprendizaje * db
		
			if i % 100 == 0:
				costos.append(costo)

			if imprimir_costo and i % 100 == 0:
				print ("Costo luego de la iteracion %i: %f" %(i, costo))
	
		parametros = {"w": w,
				  "b": b}
	
		gradientes = {"dw": dw,
				 "db": db}
	
		return parametros, gradientes, costos

	def predecir(self, w, b, X):
	
		m = X.shape[1]
		Y_prediccion = np.zeros((1,m))
		w = w.reshape(X.shape[0], 1)
	
		A = self.sigmoide(np.dot(w.T,X)+b)
	
		for i in range(A.shape[1]):
		
			Y_prediccion[0,i] = 0 if (A[0,i] <= 0.5) else 1
	
		assert(Y_prediccion.shape == (1, m))
	
		return Y_prediccion


	def modelo(self, X_train, Y_train, X_test, Y_test, num_iteraciones = 2000, tasa_aprendizaje = 0.5, imprimir_costo = False):

		learning_rate=tasa_aprendizaje
		num_iterations=num_iteraciones

		w, b = self.inicializa_con_ceros(X_train.shape[0])

		params, grads, costs = self.optimizar(w, b, X_train, Y_train, num_iteraciones, tasa_aprendizaje, imprimir_costo)
	
		w = params["w"]
		b = params["b"]
	
		Y_prediction_test = self.predecir(w, b, X_test)
		Y_prediction_train = self.predecir(w, b, X_train)

		print("exactitud de entrenamiento: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
		print("exactitud de prueba: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

		d = {"costs": costs,
			 "Y_prediction_test": Y_prediction_test, 
			 "Y_prediction_train" : Y_prediction_train, 
			 "w" : w, 
			 "b" : b,
			 "learning_rate" : learning_rate,
			 "num_iterations": num_iterations}
	
		return d

