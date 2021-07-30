print ("Calcularemos el promedio de edad de las personas")
personas = int (input ("Ingrese cantidad de personas a promediar: "))
edades = 0
for i in range (personas):
    edad = int (input ("Ingrese edad:  "))
    edades = edades+edad
print ("Total sumatoria de edades: ",edades)    
print ("El promedio de edad es: ", (int(edades/personas)))