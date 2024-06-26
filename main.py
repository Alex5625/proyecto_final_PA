from enfermedad import Enfermedad
from comunidad import Comunidad
from simulacion import Simulador

covid = Enfermedad(infeccion = 0.3,
												numero = 10)

talca = Comunidad(cantidad = 10,
											promedio= 8,
											probabilidad = 0.8,
											infectados = 10,
											enfermedad = covid
											)

sim = Simulador()

sim.set_comunidad(comunidad = talca)

sim.run(pasos = 45)
