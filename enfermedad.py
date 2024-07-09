
class Enfermedad():
	def __init__(self,infeccion,numero, nombre):
		
		#Cual es la probabilidad que se contagie
		self.prob_infeccion = infeccion

		#Cantidad maxima de de dias 
		self.prom_pasos = numero

		#Nombre de la Enfermedad
		self.nombre = nombre

		#Contara la cantidad de pasos que se estan dando
		self.num_pasos = 0

	#Van pasando los dias
	def contador(self):
		self.num_pasos += 1

	def get_prom_pasos(self):
		return self.prom_pasos

	def get_num_pasos(self):
		return int(self.num_pasos)

	def get_nombre(self):

		return self.nombre