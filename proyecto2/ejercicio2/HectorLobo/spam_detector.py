import os
import re
import numpy as np

class SpamDetector:

  def __init__(self):
    """El método init leerá todos los archivos con extensión ".txt" 
    de los directorios emails/train y emails/test y los usará para crear las matrices 
    de X_train, X_test, Y_train y Y_test.

    Cada archivo ".txt" corresponderá a una instancia de entrenamiento o prueba. 
    El formato de los archivos ".txt" es el siguiente:

    <0|1>
    <contenido>

    La primera línea contendrá la etiqueta 0 si el contenido no es spam y 1 si lo es. 
    A partir de la segunda línea todo el texto que se encuentre se considerará 
    parte del correo electrónico.

    El texto de un correo electrónico se convertirá en un vector de atributos de la 
    siguiente forma:

    Primero se detectarán todas las palabras distintas (sólo letras, ningún símbolo) 
    que aparezcan todos los archivos (train + test), 
    luego a cada palabra se le asignará un índice y finalmente se representará 
    cada correo a través de un vector cuyos elementos reprsentarán la cantidad de veces 
    que aparece cada palabra en su contenido de acuerdo al índice que se asignó.

    Ejemplo:

    Si tuviésemos solamente tres palabras distintas: no, si, spam, 
    le asignaríamos a cada un índice de 0 al 2 (esta longitud representa a n). 
    Y si el contenido de un correo fuese: "spam spam si si" 
    el vector que lo representaría sería: 
    [0 2 2]

    Recuerde que todos los vectores deben tener la misma longitud. 

    Las URL se considerarán como palabras, ej.: http://www.google.com sería cuatro palabras: 
    http, www, google y com.

    Por simplicidad se manejarán solamente correos en español. 
    """
    
    emails_train = os.listdir(path = "emails/train")
    emails_test = os.listdir(path = "emails/test")
    full_path_emails_train = []
    full_path_emails_test = []
    different_words = []
    max_size = 0
    self.X_train = []
    self.X_test = []
    self.Y_train = []
    self.Y_test = []
    dictionary = {}

    ''' se obtiene las rutas de los emails para train '''
    for email_train in emails_train:
      full_path_emails_train.append(os.path.join(os.getcwd() + "/emails/train/", email_train))

    ''' se obtiene las rutas de los emails para test '''
    for email_test in emails_test:
      full_path_emails_test.append(os.path.join(os.getcwd() + "/emails/test/", email_test))

    ''' se guardar las palabras distintas de los emails para train '''
    regex = re.compile("[A-Za-zÁÉÍÓÚáéíóúüñńνσ]+")
    for full_path_email_train in full_path_emails_train:
      if(".txt" in full_path_email_train):
        email = open(full_path_email_train, 'r', encoding = "utf-8")
        label = email.readline()
        content = ""
        for line_content in email.readlines():
          content += line_content
        if(regex.findall(content).__len__() > max_size):
          max_size = regex.findall(content).__len__()
        for different_word in regex.findall(content):
          if(not different_word.lower() in different_words):
            different_words.append(different_word.lower())
        email.close()

    ''' se guardar las palabras distintas de los emails para test '''
    for full_path_email_test in full_path_emails_test:
      if(".txt" in full_path_email_test):
        email = open(full_path_email_test, 'r', encoding = "utf-8")
        label = email.readline()
        content = ""
        for line_content in email.readlines():
          content += line_content
        if(regex.findall(content).__len__() > max_size):
              max_size = regex.findall(content).__len__()
        for different_word in regex.findall(content):
          if(not different_word.lower() in different_words):
            different_words.append(different_word.lower())
        email.close()
    ''' different_words.append("_") '''

    ''' dictionary '''
    for index in range(different_words.__len__()):
      dictionary[different_words[index]] = index

    ''' generar X_train '''
    for full_path_email_train in full_path_emails_train:
      if(".txt" in full_path_email_train):
        email = open(full_path_email_train, 'r', encoding = "utf-8")
        label = email.readline()
        content = ""
        for line_content in email.readlines():
          content += line_content
        vector_instace = []
        ''' counter = 0 '''
        for word in different_words:
          counter = regex.findall(content).count(word)
          vector_instace.append(counter)
        self.X_train.append(vector_instace)
        email.close()

    ''' generar X_test '''
    for full_path_email_test in full_path_emails_test:
      if(".txt" in full_path_email_test):
        email = open(full_path_email_test, 'r', encoding = "utf-8")
        label = email.readline()
        content = ""
        for line_content in email.readlines():
          content += line_content
        vector_instace = []
        for word in different_words:
          counter = regex.findall(content).count(word)
          vector_instace.append(counter)
        self.X_test.append(vector_instace)
        email.close()

    ''' generar Y_train '''
    vector_label = []
    for full_path_email_train in full_path_emails_train:
      if(".txt" in full_path_email_train):
        email = open(full_path_email_train, 'r', encoding = "utf-8")
        label = email.readline()
        vector_label.append(int(label))
        email.close()
    self.Y_train.append(vector_label)

    ''' generar Y_test '''
    vector_label = []
    for full_path_email_test in full_path_emails_test:
      if(".txt" in full_path_email_test):
        email = open(full_path_email_test, 'r', encoding = "utf-8")
        label = email.readline()
        vector_label.append(int(label))
        email.close()
    self.Y_test.append(vector_label)

    train_set_x_orig = np.array(self.X_train)
    test_set_x_orig = np.array(self.X_test)
    self.train_set_y = np.array(self.Y_train)
    self.test_set_y = np.array(self.Y_test)
    
    train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
    test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T

    train_set_x_flatten = (train_set_x_flatten - np.mean(train_set_x_flatten)) / np.std(train_set_x_flatten)
    test_set_x_flatten = (test_set_x_flatten - np.mean(test_set_x_flatten)) / np.std(test_set_x_flatten)

    self.train_set_x = train_set_x_flatten
    self.test_set_x = test_set_x_flatten


  def sigmoid(self, z):
    s = 1 / (1 + np.exp(-z))
    return s

  def initialize_with_zeros(self, dim):
    w = np.zeros((dim, 1))
    b = 0.0
    assert(w.shape == (dim, 1))
    assert(isinstance(b, float) or isinstance(b, int))
    return w, b
  
  def propagate(self, w, b, X, Y):
    m = X.shape[1]
    Z = w.T.dot(X) + b
    A = self.sigmoid(Z)
    cost = -1/m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))
    dZ = A - Y
    dw = 1/m * X.dot(dZ.T)
    db = 1/m * np.sum(dZ)
    assert(dw.shape == w.shape)
    assert(db.dtype == float)
    cost = np.squeeze(cost)
    assert(cost.shape == ())
    grads = {"dw": dw,
            "db": db}
  
    return (grads, cost)

  def optimize(self, w, b, X, Y, num_iterations, learning_rate, print_cost = False):
    costs = []
    for i in range(num_iterations):
      grads, cost = self.propagate(w, b, X, Y)
      dw = grads["dw"]
      db = grads["db"]
      w = w - learning_rate * dw
      b = b - learning_rate * db
      if i % 100 == 0:
        costs.append(cost)
      if print_cost and i % 100 == 0:
        print ("Cost after iteration %i: %f" %(i, cost))
    params = {"w": w,
            "b": b}
    grads = {"dw": dw,
            "db": db}
    return params, grads, costs
  
  def predict(self, w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1,m))
    w = w.reshape(X.shape[0], 1)
    A = self.sigmoid(w.T.dot(X) + b)
    for i in range(A.shape[1]):
      Y_prediction[0,i] = 0 if (A[0,i] <= 0.5) else 1
    assert(Y_prediction.shape == (1, m))
    return Y_prediction
  
  def model(self, X_train, Y_train, X_test, Y_test, num_iterations = 2000, learning_rate = 0.5, print_cost = False):
    n = X_train.shape[0]
    w, b = self.initialize_with_zeros(n)
    parameters, grads, costs = self.optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)
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

  def train_model(self):
    """Retorna un un diccionario con los siguientes datos:
    
    d = {"costs": costs,
    "Y_prediction_test": Y_prediction_test, 
    "Y_prediction_train" : Y_prediction_train, 
    "w" : w, 
    "b" : b,
    "learning_rate" : learning_rate,
    "num_iterations": num_iterations}

    Los parámetros learning_rate y num_iterations deben ser definidos por el programador 
    mediante un proceso de prueba y error con el fin de obtener la mejor precisión en los datos
    de prueba.
    """
    ''' train_set_x_orig = np.array(self.X_train)
    test_set_x_orig = np.array(self.X_test)
    train_set_y = np.array(self.Y_train)
    test_set_y = np.array(self.Y_test)
    
    train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
    test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T

    train_set_x_flatten = (train_set_x_flatten - np.mean(train_set_x_flatten)) / np.std(train_set_x_flatten)
    test_set_x_flatten = (test_set_x_flatten - np.mean(test_set_x_flatten)) / np.std(test_set_x_flatten)

    train_set_x = train_set_x_flatten
    test_set_x = test_set_x_flatten '''

    d = self.model(self.train_set_x, self.train_set_y, self.test_set_x, self.test_set_y, num_iterations = 7000, learning_rate = 0.0004, print_cost = True)
    return d

  def get_datasets(self):
    """Retorna un diccionario con los datasets preprocesados con los datos y 
    dimensiones que se usaron para el entrenamiento
    
    d = { "X_train": X_train,
    "X_test": X_test,
    "Y_train": Y_train,
    "Y_test": Y_test
    }
    """
    d = {
      "X_train": self.train_set_x,
      "X_test": self.test_set_x,
      "Y_train": self.train_set_y,
      "Y_test": self.test_set_y
    }

    return d

