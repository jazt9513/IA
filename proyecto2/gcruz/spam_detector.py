import io
import re
import os
import numpy as np
import red2

class SpamDetector:
	def __init__(self):
		"""El método init leerá todos los archivos con extensión ".txt" de los directorios emails/train y emails/test y los usará para crear las matrices de X_train, X_test, Y_train y Y_test.

		Cada archivo ".txt" corresponderá a una instancia de entrenamiento o prueba. El formato de los archivos ".txt" es el siguiente:

		<0|1>
		<contenido>

		La primera línea contendrá la etiqueta 0 si el contenido no es spam y 1 si lo es. A partir de la segunda línea todo el texto que se encuentre se considerará parte del correo electrónico.

		El texto de un correo electrónico se convertirá en un vector de atributos de la siguiente forma:
		Primero se detectarán todas las palabras distintas (sólo letras, ningún símbolo) que aparezcan todos los archivos (train + test), luego a cada palabra se le asignará un índice y finalmente se representará cada correo a través de un vector cuyos elementos reprsentarán la cantidad de veces que aparece cada palabra en su contenido de acuerdo al índice que se asignó.

		Ejemplo:

		Si tuviésemos solamente tres palabras distintas: no, si, spam, hariamos un diccionario y le asignaríamos a cada un índice de 0 al 2 (esta longitud representa a n). Y si el contenido de un correo fuese: "spam spam si si" el vector que lo representaría sería: 
		[0 2 2]

		Recuerde que todos los vectores deben tener la misma longitud. 

		Las URL se considerarán como palabras, ej.: http://www.google.com sería cuatro palabras: http, www, google y com.

		Por simplicidad se manejarán solamente correos en español. """

	
		self.diccio={}
		self.oc=list()
		self.dr="./emails/test/"
		self.dr2="./emails/train/"

		self.crea_dicc(self.dr)
		t=len(self.diccio)
		print("diccion size "+str(t))

		self.X_train=np.array([0]*(t))
		self.X_test=np.array([0]*(t))
		self.Y_train=np.array([9])
		self.Y_test=np.array([9])

		em=self.crea_lista_ems(self.dr)
		
		for e in em:		
			email=self.lee_email(self.dr,e,p=0)
			eml=np.array(email[1:t])
			veml=np.array(self.proc_email(eml))
			eml2=np.array([int(email[0])])	
			self.X_test=np.vstack([self.X_test,veml])
			self.Y_test=np.vstack([self.Y_test,eml2])

		em=self.crea_lista_ems(self.dr2)

		for e in em:		
			email=self.lee_email(self.dr2,e,p=0)
			eml=np.array(email[1:t])
			veml=self.proc_email(eml)
			eml2=np.array([int(email[0])])
			self.X_train=np.vstack([self.X_train,veml])
			self.Y_train=np.vstack([self.Y_train,eml2])

		self.X_train=np.delete(self.X_train,0,axis=0)
		self.X_test=np.delete(self.X_test,0,axis=0)
		self.Y_train=np.delete(self.Y_train,0,axis=0)
		self.Y_test=np.delete(self.Y_test,0,axis=0)

		self.X_train=self.X_train.T
		self.Y_train=self.Y_train.T
		self.X_test=self.X_test.T
		self.Y_test=self.Y_test.T	

	def train_model(self):

		r = red2.Red()
		d = r.modelo(self.X_train, self.Y_train, self.X_test, self.Y_test, num_iteraciones =3500, tasa_aprendizaje = 0.07, imprimir_costo = True)
	
		return d	
		"""Retorna un un diccionario con los siguientes datos:
		
		d = {"costs": costs,
		"Y_prediction_test": Y_prediction_test, 
		"Y_prediction_train" : Y_prediction_train, 
		"w" : w, 
		"b" : b,
		"learning_rate" : learning_rate,
		"num_iterations": num_iterations}

		Los parámetros learning_rate y num_iterations deben ser definidos por el programador mediante un proceso de prueba y error con el fin de obtener la mejor precisión en los datos de prueba."""

	def lee_email(self,dr,e,p=1):
		f=io.open(dr+e, encoding="utf-8")
		t=f.read()
		f.close()
		txt=t[p:]

		tx=txt.replace('\n',' ')
		tx1=tx.replace('\t','')
		tx2=re.sub(r'[,.!?-]','',tx1)

		arr=tx2.split(' ')

		lst=[x for x in arr if x != '']

		return lst

	def crea_lista_ems(self,dr):
		dirs=os.listdir(dr)
		emails=list();

		for l in dirs:
			nombres=l
			if os.path.isdir(nombres):
				pass
			else:
				res=re.search(r'^[a-zA-z0-9\-\_]*\.txt$',nombres)
				if res:
					emails.append(nombres)
				else:
					pass

		return emails

	def crea_dicc(self,dr):
		emails=list()
		palabras=list()

		emails=self.crea_lista_ems(dr)
		
		for e in emails:
			palabras+=self.lee_email(dr,e)
	
		emails2=list()

		emails2=self.crea_lista_ems(self.dr2)

		for e in emails2:
			palabras+=self.lee_email(self.dr2,e)

		i=0

		for p in palabras:
			if p not in self.diccio:
				self.diccio[p]=i
				i+=1
			else:
				pass
	

	def proc_email(self, str):
		self.oc=[0]*len(self.diccio)
		
		for s in str:
			if s in self.diccio:
				self.oc[self.diccio[s]]+=1	

		return self.oc	
