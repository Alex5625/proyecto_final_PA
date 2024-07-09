import numpy as np

def contagios(infectado, susceptible):

	infeccion_familia = 0.3
	#print(f"Id del infectado ~~{infectado.id_familia} ~~ Id del supuesto pariente ~~{susceptible.id_familia}~~")
	#primero ver si las personas son parientes o no, pq si lo son, significa que podrian habitar la misma casa y eso significa que 
	#la probabilidad de contagio sea mayor
	if infectado.id_familia == susceptible.id_familia: 
		#print("ERES DE LA FAMILIA TE vas a contagiar con la probabiliad de que eres familiar")
		if np.random.random() <= infeccion_familia:
			return True
		else:
			return False
	else:
		#print("no eres de la FAMILIA, la probabilidad con la que te van a contagiar sera menor")
		
		if np.random.random() <= infectado.enfermedad.prob_infeccion:
			return True
		else:
			return False
