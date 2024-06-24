from persona import Persona
from crear_listas import NombresApellidos




class Comunidad(Persona) :
	#La cantidad de personas sera determinada con un get del largo de la lista 
	def __init__(self,cantidad,promedio,probabilidad,infectados):

		#cantidad maxima de habitantes o personas dentro de la comunidad
		self.__largo_comunidad = cantidad

		self.__prom_conexion_fisica =  promedio
		self.__prob_conexion_fisica = 	probabilidad
		
		#cantidad inicial de infectados 
		self.__num_infectados = infectados  

		self.__comunidad = self.set_comunidad()
	


	def set_comunidad(self):
		self.lista = []
		nombre_apellido_manager = NombresApellidos("nombres_apellidos.csv")

		for i in range(self.__largo_comunidad):
			nombre, apellido = nombre_apellido_manager.obtener_nombre_apellido()
			persona = Persona(nombre,apellido)
			self.lista.append(persona)

		#self.get_lista()

	def get_lista(self):
		print("La lista contiene:")
		for persona in self.lista:
			print(f"Nombre: {persona.nombre}, Apellido: {persona.id}")

