#despues definir que parametros 


class Persona:

	def __init__(self,apellido,nombre)
		self.__id = 	apellido
		self.__nombre = nombre
		
		#si __estado = True esta vivo, si = False esta muerto
		self.__enfermedad = False
		
		#si __estado = True esta vivo, si = False esta muerto
		self.__estado = True
		


	def set_taenfermo(self,booleano):

		if isinstance(booleano, bool):
			self.__enfermedad = booleano

	def set_tavivo(self,quesopadrino)

		if isinstance(quesopadrino, bool):

			self.__estado = quesopadrino
