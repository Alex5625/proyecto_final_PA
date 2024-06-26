#Crear ventana gtk
#aqui es donde debe estar la base del programa completo


#implementar modelo sir dentro de esta clase


class Simulador:
	def __init__(self):
		self.__comunidad = None

	#Se setea la comunidad
	def set_comunidad(self,comunidad):
		self.__comunidad = comunidad

	def run(self, pasos):

		#se ven el numero de pasos que va a tener la simulacion
