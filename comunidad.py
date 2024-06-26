from persona import Persona
from crear_listas import NombresApellidos
from enfermedad import Enfermedad


		
class Comunidad(Persona) :
	#La cantidad de personas sera determinada con un get del largo de la lista 
	def __init__(self,cantidad,promedio,probabilidad,infectados,enfermedad):

		#cantidad maxima de habitantes o personas dentro de la comunidad
		self.__largo_comunidad = cantidad

		self.__prom_conexion_fisica =  promedio
		self.__prob_conexion_fisica = 	probabilidad
		
		#cantidad inicial de infectados 
		self.__num_infectados = infectados  
		self.__enfermedad = enfermedad
		self.__comunidad = self.set_comunidad()
	


	def numero_integrantes(self,media desviacion_estandar):

		#la cantidad de integrantes de cada familia tiende a distribuir normal
		return round(random.gauss(media, desviacion_estandar))



	def set_comunidad(self):
		nombre_apellido_manager = NombresApellidos("nombres_apellidos.csv")
		self.lista = []
		id_familia = 0
		media = 3.1
		desviacion_estandar = 1.2
		id_persona = 0


		while id_persona != self.__largo_comunidad:

			cantidad_personas = self.numero_integrantes(media,desviacion_estandar)
			for i in range(cantidad_personas):
				nombre, apellido = nombre_apellido_manager.obtener_nombre_apellido()
				persona = Persona(nombre,apellido,id_familia)
				self.lista.append(persona)	
				id_persona += 1

				print(f"persona n°{id_persona}")

				if id_persona == self.num_ciudadanos:
					break

			id_familia += 1


		arreglo_comunidad_hecha = self.agregar_infectados_iniciales(self.__largo_comunidad,self.__num_infectados, lista)
		#self.get_lista()


	def sumar_infectados_inicio(self, num_ciudadanos, num_infectados,arreglo_comunidad):
		contador = 0
		casilla_infectada = random.sample(range(num_ciudadanos), num_infectados)
		casilla_infectada.sort()

		print(f"las personas n°{casilla_infectada} seran contagiadas inicialmente")


		#Recorre el arreglo tipo Personas
		for persona in arreglo_comunidad:
	
			#La persona se enfermó
			if contador in casilla_infectada
				print(f"{persona.nombre} {persona.id} será infectada")
				persona.set_taenfermo(True)

			contador += 1
	


	def get_lista(self):
		print("La lista contiene:")
		for persona in self.lista:
			print(f"Nombre: {persona.nombre}, Apellido: {persona.id}")

