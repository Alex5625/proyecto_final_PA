from persona import Persona


class Comunidad(Persona) 
	#La cantidad de personas sera determinada con un get del largo de la lista 
	def __init__(self,apellido,edad,cantidad,promedio,probabilidad):
		super().__init__(apellido,edad)

		#cantidad maxima de habitantes o personas dentro de la comunidad
		self.__largo_comunidad = cantidad

		self.__prom_conexion_fisica =  promedio
		self.__prob_conexion_fisica = 	probabilidad
		
		#cantidad inicial de infectados 
		self.__num_infectados = infectados  

