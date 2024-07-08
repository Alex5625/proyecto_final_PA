#despues definir que parametros 


class Persona:

	def __init__(self,nombre,apellido,id_familia):

		self.nombre = nombre
		self.id = apellido
		self.id_familia = id_familia
		#si __estado = True esta contagiado, si = False esta libre
		#-puede ser de tipo Enfermedad
		self.enfermedad = None
		

		#si __estado = True esta enfermo, si = False no esta contagiado
		self.estado = False
		#Si inmunidad es falso es que aun no ha desarrollado la inmunidad
		self.inmunidad = False
		
		self.conexiones = []

		self.pasos = 0

	def pasa_el_dia(self):
		self.pasos += 1

		#si la lista esta rellena, es pq ta enfermo 
	def set_taenfermo(self,booleano):

		if isinstance(booleano, bool):
			self.enfermedad = booleano

	def se_enfermo(self, enfermedad_clase):
		self.estado = True
		self.enfermedad = enfermedad_clase

	def se_recupero(self):
		self.inmunidad = True
		self.estado = False

	def get_estado(self):
		return self.estado
	def get_inmunidad(self):
		return self.inmunidad

	def print_estado(self):
		if self.estado == True:
			print(f"{self.nombre} {self.id} está enfermo con {self.enfermedad.get_nombre()} ")
		if self.estado == False:
			print(f"{self.nombre} {self.id} no esta enfermo")

	def get_conexiones(self):
		return self.conexiones

	def get_nombre(self):
		return self.nombre + self.id

	def get_enfermedad(self):
		return self.enfermedad