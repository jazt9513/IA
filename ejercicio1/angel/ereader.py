from ebook import EBook
import os

class EReader:
  """Representa un lector de libros eléctronicos"""

  def __init__(self):
    """Se debe leer la lista de libros que están en el directorio 'libros'.

    Las dos primeras líneas de cada archivo contienen el autor y el título de
    cada libro, esta información no forma parte del contenido del libro. 

    Los nombres de los archivos terminan con la extensión .txt
    """
    self.libros = []
    archivos = os.listdir(path="libros")
    for n in archivos:
      if('.txt' in n):
        archivo = open('libros/'+n, 'r', encoding="utf-8")
        linea1 = archivo.readline() 
        linea2 = archivo.readline()
        autor = (linea1 if linea1.find('autor') != -1 else linea2).replace("autor: ", "")
        titulo = (linea2 if linea2.find('titulo') != -1 else linea1).replace("titulo: ", "")
        contenido = ''
        for fila in archivo.readlines():
          contenido += fila
        archivo.close()
        self.libros.append(EBook(titulo, autor, contenido))
        


  def get_libros(self, filtro):
    """Retorna un list() que contiene los libros según el 'filtro' indicado.

    'filtro' es una string que puede ser el titulo o autor que coincida con uno o varios libros. Cualquier otro valor recibido deberá lanzar una excepción de tipo ValueError."""
    resultado = []
    for libro in self.libros:
      titulo_autor = libro.titulo + " " + libro.autor
      if filtro in titulo_autor:
        resultado.append(libro)      
    if resultado:
      return resultado
    else:
      raise ValueError("El libro no se encontró")
