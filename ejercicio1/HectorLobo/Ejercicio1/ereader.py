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
    self.ebooks = []
    nameBooks = os.listdir(path = 'libros')
    fullPathBooks = []
    for nameBook in nameBooks:
      fullPathBooks.append( os.path.join(os.getcwd() + '/libros/', nameBook))

    for fullPathBook in fullPathBooks:
      if('.txt' in fullPathBook):
        book = open(fullPathBook, 'r')
        lineOne = book.readline()
        lineTwo = book.readline()
        author = lineOne[7:]
        title = lineTwo[8:]
        book.readline()
        content = ''
        for lineContent in book.readlines():
          content += lineContent
        self.ebooks.append(EBook(title, author, content))
        content = ''
        book.close()

  def get_libros(self, filtro):
    """Retorna un list() que contiene los libros según el 'filtro' indicado.

    'filtro' es una string que puede ser el titulo o autor que coincida con uno o varios libros. Cualquier otro valor recibido deberá lanzar una excepción de tipo ValueError."""
    ebooks = []
    for ebook in self.ebooks:
      if(filtro.upper() in ebook.author.upper() or filtro.upper() in ebook.title.upper()):
        ebooks.append(ebook)
    if(ebooks.__len__() == 0):
      raise ValueError('Error en el filtro')
    else:
      return ebooks