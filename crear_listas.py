import csv
import random

class NombresApellidos:
    def __init__(self, file_path):
        self.file_path = file_path
        self.nombres_lista = []
        self.apellidos_lista = []
        self.combinaciones = set()
        
        # Si el archivo no existe, crearlo y luego leerlo
        try:
            self.leer_csv(file_path)
        except FileNotFoundError:
            self.crear_csv(file_path)
            self.leer_csv(file_path)
        
        self.generar_combinaciones()

    def crear_csv(self, file_path):
        # Listas de nombres y apellidos comunes
        nombres = [
            "Alejandro", "Beatriz", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Hilda", 
            "Ignacio", "Julia", "Karla", "Luis", "Mariana", "Nicolas", "Olga", "Pablo", "Queta", 
            "Roberto", "Sara", "Tomas", "Ulises", "Valeria", "William", "Ximena", "Yolanda", "Zoe"
        ]
        apellidos = [
            "Garcia", "Martinez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Rodriguez", "Sanchez", 
            "Ramirez", "Torres", "Flores", "Rivera", "Gomez", "Diaz", "Vasquez", "Cruz", "Morales", 
            "Ortiz", "Gutierrez", "Chavez", "Reyes", "Mendoza", "Jimenez", "Ruiz", "Alvarez", "Moreno"
        ]
        
        # Generar listas de 1000 nombres y apellidos
        lista_nombres = [random.choice(nombres) for _ in range(1000)]
        lista_apellidos = [random.choice(apellidos) for _ in range(1000)]
        
        # Escribir los datos en un archivo CSV
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nombre', 'Apellido'])  # Escribir la cabecera
            for nombre, apellido in zip(lista_nombres, lista_apellidos):
                writer.writerow([nombre, apellido])
    
    def leer_csv(self, file_path):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la cabecera
            for row in reader:
                self.nombres_lista.append(row[0])
                self.apellidos_lista.append(row[1])
    
    def generar_combinaciones(self):
        for nombre, apellido in zip(self.nombres_lista, self.apellidos_lista):
            self.combinaciones.add((nombre, apellido))
    
    def obtener_nombre_apellido(self):
        if not self.combinaciones:
            raise ValueError("No quedan más combinaciones de nombres y apellidos.")
        nombre_apellido = random.choice(list(self.combinaciones))
        self.combinaciones.remove(nombre_apellido)
        return nombre_apellido

   