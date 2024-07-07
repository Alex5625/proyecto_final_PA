import contagios

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
				print(f"EL habitante ~~{habitante.get_nombre()} ~~ esta contagiado? {habitante.get_estado()}")
			
				"""Aqui posteriormente puedes hacer esto:

				if habitante.get_estado() == 0:
					print("Es susceptible, entra a la probabilidad de infeccion")
				if habitante.get_estado() == 1 or habitante.get_estado() == 2:
					print("Esta infectado o ya se recupero, asiq dejemoslo pasar, ya no pueden contagiarse")
				"""
			

				if habitante.get_estado():
					self.enfermedad = habitante.get_enfermedad()
					for conexion_persona in conexiones_habitante:
						print(f" la persona ~~{conexion_persona.get_nombre()} ~~ que tiene conexion con habitrante esta contagiado? {conexion_persona.get_estado()}")
			
						#Si la conexion de la persona anterior no esta contagiada (es susceptible)
						if not conexion_persona.get_estado():
							#Si esta enfermo la clase Enfermedad esta en el atributo enfermedad del contagiado
							#Retornara un booleano, si es True, se usa la funcion se_enfermo de la clase Persona
							infectado_o_no = contagios.contagios(habitante, conexion_persona)

							#Si es True
							if infectado_o_no:
								conexion_persona.se_enfermo(self.enfermedad)

			#Se recorre a la gente, y si esta enferma se activa el contador para que aumente
			#La cantidad de pasos (dias) para que en un punto ya se recupere
			for habitante in lista_comunidad:
				if isinstance(habitante.enfermedad, Enfermedad):
					habitante.enfermedad.contador()



			#Esto imprime la cantidad de personas que tenga la comunidad
			# for x in lista_comunidad:
			# 	if x.get_estado():
			# 		x.se_enfermo(test.enfermedad)
			# 		print(x.print_estado())
			# 		print(f"La persona tiene estos amigos: {x.get_conexiones()}")


	#Se setea la comunidad
	def set_comunidad(self,comunidad):
		self.__comunidad = comunidad
	def get_comunidad(self):
		return self.__comunidad


			
