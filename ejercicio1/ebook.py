import re

class EBook:
  """Representa un libro del EReader"""

  def __init__(self, titulo, autor, contenido):
    self.titulo = titulo
    self.autor = autor
    self.contenido = contenido


  def get_diccionario_palabras(self):
    """Retorna un dict() con todas la palabras del libro y la cantidad de veces
    que aparece cada una.

    Por ejemplo si el libro contiene un total de 7 palabras por ejemplo:
    "hola mundo Hola hola Hola mundo mundo"
     de las cuales 2 son
    la palabra 'hola', 2 son 'Hola' y 3 son la palabra 'mundo', retornará un
    diccionario, (no una cadena), cuya representación sería:

    {'hola': 2, 'Hola': 2, 'mundo': 3}

    Observe que se distiguen entre mayúsculas y minúsculas, los puntos y comas,
    no se cuentan como palabras.

    Como un segundo ejemplo, la representación del diccionario para el libro
    Blancanieves sería la siguiente:

    {'nieve': 4, 'el': 2, 'Le': 1, 'd\xc3\xada': 1, 'despist\xc3\xb3': 1, 'En': 1, 'tener': 1, 'dejando': 1, 'copos': 1, 'mientras': 1, 'en': 1, 'momento': 1, 'ca\xc3\xadan': 1, 'tal': 1, 'Un': 1, 'cabo': 1, 'm\xc3\xa1s': 1, 'forma': 1, 'le': 1, 'roja': 1, 'la': 8, 'blanca': 2, 'luz': 1, 'De': 1, 'dedo': 1, 'hija': 1, 'aunque': 1, 'as\xc3\xad': 1, 'los': 2, 'ese': 1, 'un': 2, 'c\xc3\xb3mo': 1, 'sobre': 1, 'ni\xc3\xb1a': 1, 'desear\xc3\xada': 1, 'muerte': 1, 'deseo': 1, 'cos\xc3\xada': 1, 'caer': 1, 'tiempo': 1, 'y': 4, 'de': 7, 'miraba': 1, 'cautivaron': 1, 'cabellos': 2, 'bell\xc3\xadsima': 1, 'negros': 1, 'Blancanieves': 1, 'como': 6, 'nombre': 1, 'gotas': 1, 'nacimiento': 1, 'a': 2, 'pinch\xc3\xb3': 1, 'dio': 1, 'sangre': 3, 'sonrosada': 2, 'invierno': 1, 'una': 2, 'Al': 1, 'su': 3, 'cumpli\xc3\xb3': 1, 'supuso': 1, 'pens\xc3\xb3:': 1, 'se': 3, 'madre': 1, '\xc3\xa9bano': 2, 'que': 1, 'tres': 1, 'con': 1, 'pusieron': 1, 'Reina': 1, 'C\xc3\xb3mo': 1}

    """
    contenido_limpio = re.split('[.,\s]', self.contenido)
    diccionario = {}
    for palabra in contenido_limpio:
      cantidad = contenido_limpio.count(palabra)
      diccionario[palabra] = cantidad
    del diccionario[''] #borra los '' que genera el split
    return diccionario

  def __str__(self):
    return self.contenido