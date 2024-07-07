#despues definir que parametros 


class Persona:

	def __init__(self,nombre,apellido,id_familia):

		self.nombre = nombre
		self.id = apellido
		self.id_familia = id_familia
		#si __estado = True esta contagiado, si = False esta libre
		#-puede ser de tipo Enfermedad
		self.enfermedad = None
		
		#si __estado = True esta vivo, si = False esta muerto
		#-si esta inmune o no
		#-segun el modelo sir son los 3 estados (numero 1, 2 ,3) 
		self.estado = False
		#el valor de ese atributo puede ser mejor una constante por ejemplo (SANO,MUERTO) =range(2) ---> sano = 0 | muerto = 1 
		
		self.conexiones = []




		#si la lista esta rellena, es pq ta enfermo 
	def set_taenfermo(self,booleano):

		if isinstance(booleano, bool):
			self.enfermedad = booleano

	def se_enfermo(self, enfermedad_clase):
		self.estado = True
		self.enfermedad = enfermedad_clase

	def get_estado(self):
		return	 self.estado

	def print_estado(self):
		if self.estado == True:
			print(f"{self.nombre} {self.id} está enfermo con {self.enfermedad.get_nombre()} ")
		if self.estado == False:
			print(f"{self.nombre} {self.id} no esta enfermo")

	def get_conexiones(self):
		return self.conexiones

	def get_nombre(self):
		return self.nombre + self.id

	def get_enfermedad:
		return self.enfermedad