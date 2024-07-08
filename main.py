from enfermedad import Enfermedad
from comunidad import Comunidad
from simulacion import Simulador

covid = Enfermedad(infeccion = 0.1,
												numero = 10,
												nombre = "Covid")

talca = Comunidad(cantidad = 510,
											promedio= 5,
											probabilidad = 0.3,
											infectados = 5,
											enfermedad = covid
											)

sim = Simulador()

sim.set_comunidad(comunidad = talca)

sim.run(pasos = 40)

sim.main()


