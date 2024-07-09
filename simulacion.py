import contagios
from enfermedad import Enfermedad
import matplotlib
matplotlib.use('GTK4Agg')
import matplotlib.pyplot as plt

#Crear ventana gtk
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
from grafico_gtk import MatplotlibGTKWindow


#aqui es donde debe estar la base del programa completo
#implementar modelo sir dentro de esta clase


class Simulador:
	def __init__(self):
		self.__comunidad = None

	def run(self, pasos):
		

		test = self.get_comunidad()

		lista_comunidad = test.return_lista()

		#Almacenamiento de infectados por Dia
		self.infectados = [test.num_infectados]
		#Almacenamiento de datos de inmunes por dia
		self.inmunes = [0]
		#Almacenamiento de personas sanas
		self.sanos = [test.get_num_personas()]

		#se ven el numero de pasos que va a tener la simulacion

		for numero in range(pasos):

			contador_inmunes = 0

			for habitante in lista_comunidad:
				if habitante.get_inmunidad():
					contador_inmunes += 1
			self.inmunes.append(contador_inmunes)

			for habitante in lista_comunidad:
				if habitante.get_estado():
					
					if habitante.pasos == habitante.enfermedad.get_prom_pasos():
						print(f"la persona {habitante.get_nombre()} se va a recuperar")
						habitante.se_recupero()
			

			for habitante in lista_comunidad:
				conexiones_habitante = habitante.get_conexiones()

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
			personas_sanas = 0
			for habitante in lista_comunidad:
				if habitante.estado:
					personas_enfermas += 1
				else:
					personas_sanas += 1
			self.infectados.append(personas_enfermas)
			self.sanos.append(personas_sanas)

			#Se recorre a la gente, y si esta enferma se activa el contador para que aumente
			#La cantidad de pasos (dias) para que en un punto ya se recupere
			print("Va a pasar el dia!!!\n\n")
			for habitante in lista_comunidad:
				if not habitante.get_inmunidad() and habitante.get_estado():
					habitante.pasa_el_dia()
					print(f"La persona {habitante.get_nombre()} lleva {habitante.pasos} dias enfermo")

			print(f"enfermos por dia {self.infectados}")


	#Se setea la comunidad
	def set_comunidad(self,comunidad):
		self.__comunidad = comunidad
	def get_comunidad(self):
		return self.__comunidad


	def main(self):

	    app = Gtk.Application()
	    
	    def on_activate(app):
	        win = MatplotlibGTKWindow(self.infectados, self.inmunes, self.sanos)
	        win.set_application(app)
	        win.show()
	    
	    app.connect('activate', on_activate)
	    app.run()
