
class EReader:
  """Representa un lector de libros eléctronicos"""
  from ebook import EBook
  import glob
  cantLibros = len(glob.glob("libros/*"))
  listaLibros = list()
  def __init__(self):
    from ebook import EBook
    try:
      for i in range(self.cantLibros):
        ruta = 'libros\\'+str(i+1)+'.txt'
        bookCOD = open(ruta,'r', encoding = 'utf-8')
        book = str(bookCOD.read())#.encode('utf-8'))
        bookCOD.close()
        autor = str((book.split('autor: ')[1]).split('\n')[0])
        titulo = str((book.split('titulo: ')[1]).split('\n')[0])
        contenido = ''

        #Limpiando la lista del contenido
        listaContenido = (book.split('\n'))
        indice = 0
        for x in listaContenido:
          if indice<3: 
            listaContenido.pop(0)
            indice += 1

        #Haciendo cadena el contenido
        for y in listaContenido:
          contenido+=y
        toSplit = ((contenido.replace(':',': ')).replace(',',' ')).replace('.',' ')
        #Creando El objeto de Tipo EBook
        libroLeido = EBook(titulo, autor, contenido, toSplit)
        print('\nCreando Libro...\nAutor del libro: '+str(libroLeido.autor))

        print('Titulo del libro: '+str(libroLeido.titulo)+'')
        print('Se acaba de crear correctamente el libro: '+str(libroLeido.titulo)+' de '+str(libroLeido.autor)+'\n\n')
        
        #print(libroLeido.get_diccionario_palabras())
        self.listaLibros.append(libroLeido)

    except FileNotFoundError as error:
        print('\n\n')

    print('====================\nlibros Leidos: '+str(len(self.listaLibros))+'\n====================')
    """Se debe leer la lista de libros que están en el directorio 'libros'.

    Las dos primeras líneas de cada archivo contienen el autor y el título de
    cada libro, esta información no forma parte del contenido del libro. 

    Los nombres de los archivos terminan con la extensión .txt
    """
    


  def get_libros(self, filtro):
    r = list()
    for v in self.listaLibros:
      if filtro == str(v.autor):
        r.append(v)
      elif filtro == str(v.titulo):

        r.append(v)

    if len(r)==0:
      raise ValueError
   
    return r