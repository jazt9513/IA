import os
import io
import re
from ebook import EBook

class EReader:
	"""Representa un lector de libros eléctronicos"""
	
	def __init__(self):
		"""Se debe leer la lista de libros que están en el directorio 'libros'.

		Las dos primeras líneas de cada archivo contienen el autor y el título de
		cada libro, esta información no forma parte del contenido del libro. 

		Los nombres de los archivos terminan con la extensión .txt"""
		
		dirs=os.listdir("./libros")
		libros=list()
		autores=list()
		titulos=list()
		self._diccio={}
		self._ebooks=list()
		self._cnt=''
		
		for l in dirs:
			nombres=l
			if os.path.isdir(nombres):
				pass
			else:
				res=re.match(r'\w*\.txt$',nombres)
				if res:
					libros.append(nombres)
				else:
					pass
					
		self._ebooks=list()
					
		for l in libros:
			fo=io.open("./libros/"+l,"r",encoding="utf-8")
			lineas=fo.readlines()
			fo.close()
			aut=lineas[0][7:]
			tlt=lineas[1][8:]
			
			c=2
			
			while c< len(lineas):	
				self._cnt+=(lineas[c])
				c+=1
			
			self._ebooks.append(EBook(titulo=tlt[:len(tlt)-1],autor=aut[:len(aut)-1],contenido=self._cnt))
						
			self._cnt=''

	def get_libros(self, filtro):
		"""Retorna un list() que contiene los libros según el 'filtro' indicado.

		'filtro' es una string que puede ser el titulo o autor que coincida con uno o varios libros. Cualquier otro valor recibido deberá lanzar 
		una excepción de tipo ValueError."""
		lista=list()
		
		i=0
		e=len(self._ebooks)
		
		while i<e:
			if (self._ebooks[i].getTitulo()==filtro or self._ebooks[i].getAutor()==filtro):
				lista.append(self._ebooks[i])
				return lista 
			else:
				i+=1
				
		if not lista:
			raise TypeError("Valor no valido!")
