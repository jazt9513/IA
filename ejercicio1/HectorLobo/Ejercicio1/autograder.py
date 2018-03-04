#-*- coding: utf-8 -*-
from ereader import EReader

ans1 = {'ébano': 2, 'Un': 1, 'cautivaron': 1, 'nombre': 1, 'así': 1, 'el': 2, 'De': 1, 'tal': 1, 'tiempo': 1, 'roja': 1, 'copos': 1, 'un': 2, 'de': 7, 'niña': 1, 'caer': 1, 'y': 4, 'pinchó': 1, 'blanca': 2, 'miraba': 1, 'mientras': 1, 'Blancanieves': 1, 'caían': 1, 'Le': 1, 'dejando': 1, 'despistó': 1, 'dio': 1, 'bellísima': 1, 'sangre': 3, 'su': 3, 'con': 1, 'le': 1, 'desearía': 1, 'madre': 1, 'dedo': 1, 'los': 2, 'hija': 1, 'cosía': 1, 'tener': 1, 'Cómo': 1, 'cómo': 1, 'sobre': 1, 'cabellos': 2, 'se': 3, 'pusieron': 1, 'a': 2, 'sonrosada': 2, 'nieve': 4, 'ese': 1, 'en': 1, 'Reina': 1, 'invierno': 1, 'como': 6, 'momento': 1, 'tres': 1, 'más': 1, 'Al': 1, 'una': 2, 'forma': 1, 'pensó:': 1, 'deseo': 1, 'cabo': 1, 'gotas': 1, 'día': 1, 'En': 1, 'negros': 1, 'la': 8, 'muerte': 1, 'luz': 1, 'nacimiento': 1, 'aunque': 1, 'cumplió': 1, 'que': 1, 'supuso': 1}

# ans1 = {'nieve': 4, 'el': 2, 'Le': 1, 'd\xc3\xada': 1, 'despist\xc3\xb3': 1, 'En': 1, 'tener': 1, 'dejando': 1, 'copos': 1, 'mientras': 1, 'en': 1, 'momento': 1, 'ca\xc3\xadan': 1, 'tal': 1, 'Un': 1, 'cabo': 1, 'm\xc3\xa1s': 1, 'forma': 1, 'le': 1, 'roja': 1, 'la': 8, 'blanca': 2, 'luz': 1, 'De': 1, 'dedo': 1, 'hija': 1, 'aunque': 1, 'as\xc3\xad': 1, 'los': 2, 'ese': 1, 'un': 2, 'c\xc3\xb3mo': 1, 'sobre': 1, 'ni\xc3\xb1a': 1, 'desear\xc3\xada': 1, 'muerte': 1, 'deseo': 1, 'cos\xc3\xada': 1, 'caer': 1, 'tiempo': 1, 'y': 4, 'de': 7, 'miraba': 1, 'cautivaron': 1, 'cabellos': 2, 'bell\xc3\xadsima': 1, 'negros': 1, 'Blancanieves': 1, 'como': 6, 'nombre': 1, 'gotas': 1, 'nacimiento': 1, 'a': 2, 'pinch\xc3\xb3': 1, 'dio': 1, 'sangre': 3, 'sonrosada': 2, 'invierno': 1, 'una': 2, 'Al': 1, 'su': 3, 'cumpli\xc3\xb3': 1, 'supuso': 1, 'pens\xc3\xb3:': 1, 'se': 3, 'madre': 1, '\xc3\xa9bano': 2, 'que': 1, 'tres': 1, 'con': 1, 'pusieron': 1, 'Reina': 1, 'C\xc3\xb3mo': 1}

ans2 = {'cuanto': 1, 'de': 1, 'era': 1, 'suerte': 1, 'lamentó': 1, 'supo': 1, 'el': 8, 'una': 1, 'vez': 1, 'herencia': 1, 'se': 1, 'murió': 1, 'reparto': 1, 'sus': 1, 'que': 1, 'último': 1, 'pequeño': 1, 'a': 1, 'gato': 2, 'cuando': 1, 'segundo': 1, 'más': 1, 'asno': 2, 'para': 3, 'y': 2, 'molinero': 1, 'cuál': 1, 'Había': 1, 'un': 3, 'fue': 1, 'pobre': 1, 'En': 1, 'molino': 2, 'su': 2, 'Éste': 1, 'sólo': 1, 'pudo': 1, 'por': 1, 'en': 1, 'hijos': 1, 'dejar': 1, 'mayor': 1, 'parte': 1}

# ans2 = {'el': 8, 'en': 1, 'cu\xc3\xa1l': 1, 'Hab\xc3\xada': 1, 'cuando': 1, 'muri\xc3\xb3': 1, '\xc3\xbaltimo': 1, 'hijos': 1, 'mayor': 1, 'dejar': 1, 'para': 3, 'asno': 2, 'vez': 1, 'gato': 2, 'sus': 1, 'herencia': 1, 'un': 3, 'molino': 2, 'segundo': 1, 'por': 1, 'pudo': 1, 'de': 1, 'que': 1, 'peque\xc3\xb1o': 1, 'lament\xc3\xb3': 1, 'cuanto': 1, 'parte': 1, 'a': 1, 'En': 1, '\xc3\x89ste': 1, 'reparto': 1, 'pobre': 1, 'su': 2, 'm\xc3\xa1s': 1, 'una': 1, 'fue': 1, 'era': 1, 'suerte': 1, 'molinero': 1, 'y': 2, 'supo': 1, 's\xc3\xb3lo': 1, 'se': 1}

ans3 = {'era': 2, 'casa': 2, 'cerditos': 1, 'hacerla': 1, 'el': 6, 'aquí': 1, 'después': 1, 'un': 1, 'de': 5, 'mayor:': 1, 'mucho': 2, 'madera': 1, 'idea': 1, 'vivían': 1, 'jugar': 1, 'día': 1, 'muy': 1, 'chimenea': 1, 'mejor': 1, 'qué': 1, 'por': 2, 'estaba': 1, 'Así': 1, 'Además': 1, 'Como': 1, 'le': 1, 'tardara': 1, 'les': 1, 'los': 2, 'otros': 1, 'no': 3, 'tampoco': 1, 'utilizar': 2, 'se': 1, 'protegernos': 1, 'persiguiendo': 1, 'calentarme': 1, 'fuerte': 1, 'lo': 2, 'tres': 1, 'sus': 1, 'final': 1, 'irse': 1, 'Había': 1, 'pero': 1, 'poder': 1, 'y': 4, 'invierno': 1, 'prefirió': 1, 'en': 2, 'escondernos': 1, 'cerdito': 1, 'dos': 1, 'hacer': 3, 'bosque': 1, 'así': 1, 'vez': 2, 'tiempo': 1, 'ponían': 1, 'pequeño': 1, 'comérselos': 1, 'Pero': 1, 'discutir': 1, 'ella': 1, 'Tenemos': 1, 'construirla': 1, 'quisiese': 1, 'dentro': 1, 'paja': 2, 'malvado': 1, 'lobo': 3, 'tardar': 1, 'dijo': 1, 'hiciera': 1, 'podré': 1, 'aunque': 1, 'con': 2, 'optó': 1, 'mediano': 1, 'cada': 2, 'resistente': 2, 'ladrillos': 1, 'podremos': 1, 'siempre': 1, 'A': 1, 'material': 1, 'una': 4, 'buena': 1, 'hermanos': 2, 'pareció': 1, 'pensó': 2, 'a': 2, 'llevaría': 1, 'más': 3, 'Al': 1, 'aparezca': 1, 'para': 4, 'respecto': 1, 'uno': 1, 'la': 3, 'El': 2, 'mayor': 1, 'acuerdo': 1, 'decidieron': 1, 'que': 10}

# ans3 = {'dijo': 1, 'd\xc3\xada': 1, 'pon\xc3\xadan': 1, 'Tenemos': 1, 'podr\xc3\xa9': 1, 'pens\xc3\xb3': 2, 'mayor': 1, 'le': 1, 'la': 3, 'lo': 2, 'vez': 2, 'jugar': 1, 'hacerla': 1, 'madera': 1, 'escondernos': 1, 'hermanos': 2, 'lobo': 3, 'estaba': 1, 'cerdito': 1, 'material': 1, 'hiciera': 1, 'tardara': 1, 'fuerte': 1, 'peque\xc3\xb1o': 1, 'quisiese': 1, 'ladrillos': 1, 'm\xc3\xa1s': 3, 'mayor:': 1, 'el': 6, 'en': 2, 'buena': 1, 'Pero': 1, 'idea': 1, 'tardar': 1, 'protegernos': 1, 'muy': 1, 'calentarme': 1, 'as\xc3\xad': 1, 'chimenea': 1, 'sus': 1, 'cerditos': 1, 'respecto': 1, 'decidieron': 1, 'construirla': 1, 'com\xc3\xa9rselos': 1, 'les': 1, 'despu\xc3\xa9s': 1, 'aunque': 1, 'El': 2, 'Adem\xc3\xa1s': 1, 'opt\xc3\xb3': 1, 'invierno': 1, 'utilizar': 2, 'una': 4, 'bosque': 1, 'llevar\xc3\xada': 1, 'persiguiendo': 1, 'uno': 1, 'Hab\xc3\xada': 1, 'por': 2, 'paja': 2, 'mucho': 2, 'cada': 2, 'otros': 1, 'siempre': 1, 'pero': 1, 'los': 2, 'discutir': 1, 'Como': 1, 'pareci\xc3\xb3': 1, 'final': 1, 'qu\xc3\xa9': 1, 'resistente': 2, 'a': 2, 'para': 4, 'malvado': 1, 'As\xc3\xad': 1, 'casa': 2, 'poder': 1, 'un': 1, 'prefiri\xc3\xb3': 1, 'era': 2, 'acuerdo': 1, 'tres': 1, 'tampoco': 1, 'viv\xc3\xadan': 1, 'aparezca': 1, 'mejor': 1, 'irse': 1, 'no': 3, 'que': 10, 'A': 1, 'tiempo': 1, 'de': 5, 'ella': 1, 'podremos': 1, 'mediano': 1, 'hacer': 3, 'Al': 1, 'dentro': 1, 'aqu\xc3\xad': 1, 'y': 4, 'dos': 1, 'con': 2, 'se': 1}

e = EReader()
grade = 100

# Read books
try:
  book1 = e.get_libros('Hermanos Grimm')
except:
  print('No se pudo leer el libro con autor: Hermanos Grimm (-10%)')
  grade -= 10

try:
  book2 = e.get_libros('Charles Perrault')
except:
  print('No se pudo leer el libro con autor: Charles Perrault (-10%)')
  grade -= 10

try:
  book3 = e.get_libros('Los Tres Cerditos')
except:
  print('No se pudo leer el libro con titulo: Los Tres Cerditos (-10%)')
  grade -= 10

try:
  book4 = e.get_libros('No existe')
  book4[0]
except ValueError:
  pass
except:
  print('No se lanza una excepcion de tipo ValueError al buscar un libro inexistente (-5%)')
  grade -= 5

# Obtain maps
try:
  dict1 = book1[0].get_diccionario_palabras()
except:
  print('No se pudo obtener el diccionario para el libro: Blancanieves (-40%)')
  grade -= 40
else:
  # Test map
  setKeys1 = set(dict1.keys()) - set(ans1.keys())
  if len(setKeys1) > 0:
    print('El diccionario del libro: Blancanieves, tiene las siguientes palabras de más (-3 c/u):')
    print(setKeys1)
    grade -= 15

  setKeys1 = set(ans1.keys()) - set(dict1.keys())
  if len(setKeys1) > 0:
    print('El diccionario del libro: Blancanieves, tiene las siguientes palabras faltantes (-3 c/u):')
    print(setKeys1)
    grade -= 15

  for k in dict1.keys():
    if k in ans1.keys() and dict1[k] != ans1[k]:
        print('La cantidad de ocurrencias de la palabra: {0} es incorrecta (-3%)'.format(k))
        grade -= 3



try:
  dict2 = book2[0].get_diccionario_palabras()
except:
  print('No se pudo obtener el diccionario para el libro: El Gato con Botas (-30%)')
  grade -= 30
else:
  setKeys2 = set(dict2.keys()) - set(ans2.keys())
  if len(setKeys2) > 0:
    print('El diccionario del libro: El Gato con botas, tiene las siguientes palabras de más (-3 c/u):')
    print(setKeys2)
    grade -= 15

  setKeys2 = set(ans2.keys()) - set(dict2.keys())
  if len(setKeys2) > 0:
    print('El diccionario del libro: El Gato con botas, tiene las siguientes palabras faltantes (-3 c/u):')
    print(setKeys2)
    grade -= 15

  for k in dict2.keys():
    if k in ans2.keys() and dict2[k] != ans2[k]:
        print('La cantidad de ocurrencias de la palabra: {0} es incorrecta (-3%)'.format(k))
        grade -= 3


try:
  dict3 = book3[0].get_diccionario_palabras()
except:
  print('No se pudo obtener el diccionario para el libro: Los Tres Cerditos (-30%)')
  grade -= 30
else:
  setKeys3 = set(dict3.keys()) - set(ans3.keys())
  if len(setKeys3) > 0:
    print('El diccionario del libro: Los tres cerditos, tiene las siguientes palabras de más (-3 c/u):')
    print(setKeys3)
    grade -= 15

  setKeys3 = set(ans3.keys()) - set(dict3.keys())
  if len(setKeys3) > 0:
    print('El diccionario del libro: Los tres cerditos, tiene las siguientes palabras faltantes (-3 c/u):')
    print(setKeys3)
    grade -= 15

  for k in dict3.keys():
    if k in ans3.keys() and dict3[k] != ans3[k]:
        print('La cantidad de ocurrencias de la palabra: {0} es incorrecta (-3%)'.format(k))
        grade -= 3

print('='*79)
if grade == 100:
  print('¡Felicidades no se detectó ningún error!')
print('Su nota asignada es: NOTA<<{0}>>'.format(grade if grade >= 0 else 0))