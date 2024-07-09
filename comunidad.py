from persona import Persona
from crear_listas import NombresApellidos
from enfermedad import Enfermedad
import random
import numpy as np
		
class Comunidad(Persona) :
	#La cantidad de personas sera determinada con un get del largo de la lista 
	def __init__(self,cantidad,promedio,probabilidad,infectados,enfermedad):

		#cantidad maxima de habitantes o personas dentro de la comunidad
		self.largo_comunidad = cantidad

		self.__prom_conexion_fisica =  promedio
		self.__prob_conexion_fisica = 	probabilidad
		
		#cantidad inicial de infectados 
		self.num_infectados = infectados  
		self.enfermedad = enfermedad
		self.comunidad = self.set_comunidad()
	


	def numero_integrantes(self,media, desviacion_estandar):

		#la cantidad de integrantes de cada familia tiende a distribuir normal
		#USAR NUMPY (opcional)
		return round(random.gauss(media, desviacion_estandar))



	def set_comunidad(self):
		nombre_apellido_manager = NombresApellidos("nombres_apellidos.csv")
		self.lista = []
		id_familia = 0

		media = self.__prom_conexion_fisica
		desviacion_estandar = 1.2
		id_persona = 0
		
		#Combinatoria es para mezclar a la gente y no este ordenada
		#repartija aleatoria en un grupo de datos (numpy tiene algo con combinatoria) 
		#asi como podemos tener familias podemos tener amigos

		while id_persona != self.largo_comunidad:

			cantidad_personas = self.numero_integrantes(media,desviacion_estandar)
			for i in range(cantidad_personas):
				nombre, apellido = nombre_apellido_manager.obtener_nombre_apellido()
				persona = Persona(nombre,apellido,id_familia)
				#print(f"Creada {persona.nombre} {persona.id} con estado inicial: {persona.estado}\n")
				self.lista.append(persona)	
				id_persona += 1

				# print(f"persona n°{id_persona}")

				if id_persona == self.largo_comunidad:
					break

			id_familia += 1
		#self.get_lista()

		#Genera las interconexiones con la demas gente
		arreglo_comunidad_conexiones = self.conexiones_interpersonales(self.__prom_conexion_fisica,self.lista)

		#Se integran los ciudadanos inicialmente contagiados a la comunidad 
		arreglo_comunidad_w_infectados = self.sumar_infectados_inicio(self.largo_comunidad,self.num_infectados, self.lista)


		#Las conexiones que se realizan son unidireccionales, una persona puede tener X conexiones, pero esas X conexiones no tienen a la persona dentro de sus propias conexiones
	def conexiones_interpersonales(self,conexion_fisica, comunidad):

		largo_conexiones = conexion_fisica

		for persona in comunidad:
			conexiones = set()
			while len(conexiones) < largo_conexiones:
				candidato = np.random.choice(comunidad)
				if candidato != persona:
					conexiones.add(candidato)
			#Te genera la lista de internconexiones para una persona en comun

			persona.conexiones = list(conexiones)

		return comunidad

	def sumar_infectados_inicio(self, num_ciudadanos, num_infectados,arreglo_comunidad):
		contador = 0
		#########################################################
		#Se genera una lista con la API numpy para escoger las posiciones de las personas que seran inicialmente infectadas
		casilla_infectada = np.random.choice(range(num_ciudadanos), self.num_infectados, replace = False)
		casilla_infectada.sort()
		#########################################################
		#print(f"las personas n°{casilla_infectada} seran contagiadas inicialmente")

		#Recorre el arreglo tipo Personas
		for persona in arreglo_comunidad:
			contador += 1
	
			#La persona se enfermó
			if contador in casilla_infectada:
				#print(f"{persona.nombre} {persona.id} será infectada\n\n")
				#La persona al enfermarse, los atributos que se modifican es Estado (a True) y Enfermedad (tipo Enfermedad)
				persona.se_enfermo(self.enfermedad)
			#else: 
				#print(f"{persona.nombre} {persona.id} NO será infectada\n\n")

	def get_num_personas(self):
		return self.largo_comunidad
	def get_enfermedad(self):
		return enfermedad
	def return_lista(self):
		return self.lista

#Funcion que se utiliza para verificar que cada persona existe dentro de la comunidad
	def mostrar_lista(self):
		print("La lista contiene:")
		for persona in self.lista:
			print(f"Nombre: {persona.nombre}, Apellido: {persona.id}")
