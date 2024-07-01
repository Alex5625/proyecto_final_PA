#Crear ventana gtk
#aqui es donde debe estar la base del programa completo


#implementar modelo sir dentro de esta clase


class Simulador:
	def __init__(self):
		self.__comunidad = None

	#Se setea la comunidad
	def set_comunidad(self,comunidad):
		self.__comunidad = comunidad
	def get_comunidad(self):
		return self.__comunidad

	def run(self, pasos):

		#se ven el numero de pasos que va a tener la simulacion

		for numero in range(pasos):

			test = self.get_comunidad()

			lista_comunidad = test.return_lista()

			for x in lista_comunidad:
				if x.get_estado() == True:
					x.se_enfermo(test.enfermedad)
					print(x.print_estado())
						


			
