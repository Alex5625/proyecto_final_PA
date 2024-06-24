#despues definir que parametros 


class Persona:

	def __init__(self,apellido,nombre):

		self.id = 	apellido
		self.nombre = nombre
		
		#si __estado = True esta vivo, si = False esta muerto
		self.__enfermedad = False
		
		#si __estado = True esta vivo, si = False esta muerto
		self.__estado = True
		


	def set_taenfermo(self,booleano):

		if isinstance(booleano, bool):
			self.__enfermedad = booleano

	def set_tavivo(self,parametro):	

		if isinstance(parametro, bool):

			self.__estado = parametro
