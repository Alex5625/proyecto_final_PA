
class Enfermedad(Comunidad):
	def __init__(self,apellido,edad,cantidad,promedio,probabilidad,infeccion,numero):
		super().__init__(cantidad,promedio,probabilidad)


		#Cual es la probabilidad que se contagie
		self.__prob_infeccion = infeccion

		#Cantidad maxima de de dias 
		self.__prom_pasos = numero

		#Contara la cantidad de pasos que se estan dando
		self.__num_pasos = int



	#Van pasando los dias
	def contador(self):
		self.__num_pasos += 1


	def get_numPasos(self):
		return str(self.__num_pasos)
