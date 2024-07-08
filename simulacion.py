import contagios
from enfermedad import Enfermedad
import matplotlib.pyplot as plt
#Crear ventana gtk
#aqui es donde debe estar la base del programa completo


#implementar modelo sir dentro de esta clase


class Simulador:
	def __init__(self):
		self.__comunidad = None


	def run(self, pasos):

		test = self.get_comunidad()

		lista_comunidad = test.return_lista()

		#Almacenamiento de infectados por Dia
		adipd = [test.num_infectados]
		#Almacenamiento de datos de inmunes por dia
		adnpo = [0]

		#se ven el numero de pasos que va a tener la simulacion

		for numero in range(pasos):

			contador_inmunes = 0

			for habitante in lista_comunidad:
				if habitante.get_inmunidad():
					contador_inmunes += 1
			adnpo.append(contador_inmunes)

			for habitante in lista_comunidad:
				if habitante.get_estado():
					
					if habitante.pasos == habitante.enfermedad.get_prom_pasos():
						print(f"la persona {habitante.get_nombre()} se va a recuperar")
						habitante.se_recupero()
			

			for habitante in lista_comunidad:
				conexiones_habitante = habitante.get_conexiones()
				#Acordarse de que el atributo estado de la persona sera 0,1,2 !!!!
				#Si el ciudadano esta contagiado
				#print(f"EL habitante ~~{habitante.get_nombre()} ~~ esta contagiado? {habitante.get_estado()}")
			
				"""Aqui posteriormente puedes hacer esto:

				if habitante.get_estado() == 0:
					print("Es susceptible, entra a la probabilidad de infeccion")
				if habitante.get_estado() == 1 or habitante.get_estado() == 2:
					print("Esta infectado o ya se recupero, asiq dejemoslo pasar, ya no pueden contagiarse")
				"""
			

				if not habitante.get_inmunidad() and habitante.get_estado():
					self.enfermedad = habitante.get_enfermedad()
					for conexion_persona in conexiones_habitante:
						#print(f" la persona ~~{conexion_persona.get_nombre()} ~~ que tiene conexion con habitrante esta contagiado? {conexion_persona.get_estado()}")
			
						#Si la conexion de la persona anterior no esta contagiada (es susceptible)
						if not conexion_persona.get_estado():
							#Si esta enfermo la clase Enfermedad esta en el atributo enfermedad del contagiado
							#Retornara un booleano, si es True, se usa la funcion se_enfermo de la clase Persona
							infectado_o_no = contagios.contagios(habitante, conexion_persona)

							#Si es True
							if infectado_o_no:
								conexion_persona.se_enfermo(self.enfermedad)
			#Cantidad de gente enferma al final del dia
			personas_enfermas = 0

			for habitante in lista_comunidad:
				if habitante.estado:
					personas_enfermas += 1
			adipd.append(personas_enfermas)


			#Se recorre a la gente, y si esta enferma se activa el contador para que aumente
			#La cantidad de pasos (dias) para que en un punto ya se recupere
			print("Va a pasar el dia!!!\n\n")
			for habitante in lista_comunidad:
				if not habitante.get_inmunidad() and habitante.get_estado():
					habitante.pasa_el_dia()
					print(f"La persona {habitante.get_nombre()} lleva {habitante.pasos} dias enfermo")

			print(f"enfermos por dia {adipd}")


			#Esto imprime la cantidad de personas que tenga la comunidad
			# for x in lista_comunidad:
			# 	if x.get_estado():
			# 		x.se_enfermo(test.enfermedad)
			# 		print(x.print_estado())
			# 		print(f"La persona tiene estos amigos: {x.get_conexiones()}")

		#Grafico~~~~~~~~~

		longitud_x = len(adipd)
		arreglo_eje_x = list(range(1,longitud_x + 1))

		#ejes X e Y
		plt.plot(arreglo_eje_x, adipd)
		plt.plot(arreglo_eje_x, adnpo)

		#Titulo del grafico
		plt.title("Grafica de contagiados/inmunes")

		#Muestra el grafico
		plt.show()

	#Se setea la comunidad
	def set_comunidad(self,comunidad):
		self.__comunidad = comunidad
	def get_comunidad(self):
		return self.__comunidad


			
