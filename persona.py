#despues definir que parametros 


class Persona:

	def __init__(self,nombre,apellido,id_familia):

		self.nombre = nombre
		self.id = apellido
		self.id_familia = id_familia
		#si __estado = True esta contagiado, si = False esta libre
		#-puede ser de tipo Enfermedad
		self.__enfermedad = False
		
		#si __estado = True esta vivo, si = False esta muerto
		#-si esta inmune o no
		#-segun el modelo sir son los 3 estados (numero 1, 2 ,3) 
		self.__estado = True
		#el valor de ese atributo puede ser mejor una constante por ejemplo (SANO,MUERTO) =range(2) ---> sano = 0 | muerto = 1 
		
		self.conexiones = []




		#si la lista esta rellena, es pq ta enfermo 
	def set_taenfermo(self,booleano):

		if isinstance(booleano, bool):
			self.__enfermedad = booleano

	def set_tavivo(self,parametro):	

		if isinstance(parametro, bool):

			self.__estado = parametro
