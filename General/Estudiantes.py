Estudiantes = []

def persona (nom, ape):
    Estudiantes.append([nom, ape])
    print(" ")

for i in range (2):
    nombre = input (f" Digite nombre " +str(i+1) + ": ")
    apellido = input ("Digite apellido: ")
    persona(nombre,apellido)

for i in range (len(Estudiantes)):
    print (Estudiantes [i])