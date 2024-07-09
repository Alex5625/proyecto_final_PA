from enfermedad import Enfermedad
from comunidad import Comunidad
from simulacion import Simulador

"""Estos valores son los ideales para demostrar la distribucion normal de los infectados,
	las personas que deben estar dentro de la comunidad debe ser maximo 510 (hasta donde he probado)"""

covid = Enfermedad(infeccion = 0.1,
												numero = 20,
												nombre = "Covid")

talca = Comunidad(cantidad = 510,
											promedio= 5,
											probabilidad = 0.3,
											infectados = 5,
											enfermedad = covid
											)

sim = Simulador()

sim.set_comunidad(comunidad = talca)

sim.run(pasos = 42)

sim.main()


