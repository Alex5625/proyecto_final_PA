

#Crear ventana gtk
#aqui es donde debe estar la base del programa completo


#implementar modelo sir dentro de esta clase


class Simulador:
	def __init__(self):
		self.__comunidad = None


	def run(self, pasos):

		#se ven el numero de pasos que va a tener la simulacion

		for numero in range(pasos):

			test = self.get_comunidad()

			lista_comunidad = test.return_lista()

			for habitante in lista_comunidad:
				conexiones_habitante = habitante.get_conexiones()
				#Acordarse de que el atributo estado de la persona sera 0,1,2 !!!!
				#Si el ciudadano esta contagiado
				if habitante.get_estado():
					for conexion_persona in conexiones_habitante:
						#Si la conexion de la persona anterior no esta contagiada (es susceptible)
						if not conexion_persona.get_estado():
							self.contagiarse(habitante, conexion_persona)




			#Esto imprime la cantidad de personas que tenga la comunidad
			# for x in lista_comunidad:
			# 	if x.get_estado():
			# 		x.se_enfermo(test.enfermedad)
			# 		print(x.print_estado())
			# 		print(f"La persona tiene estos amigos: {x.get_conexiones()}")

	def contagiarse(self, persona_principal, conexion):
		
	#Se setea la comunidad
	def set_comunidad(self,comunidad):
		self.__comunidad = comunidad
	def get_comunidad(self):
		return self.__comunidad


			
