#despues definir que parametros 


class Persona:

	def __init__(self,nombre,apellido,id_familia):

		self.nombre = nombre
		self.id = 	apellido
		self.id_familia = id_familia
		#si __estado = True esta contagiado, si = False esta libre
		self.__enfermedad = False
		
		#si __estado = True esta vivo, si = False esta muerto
		self.__estado = True 
		


	def set_taenfermo(self,booleano):

		if isinstance(booleano, bool):
			self.__enfermedad = booleano

	def set_tavivo(self,parametro):	

		if isinstance(parametro, bool):

			self.__estado = parametro
