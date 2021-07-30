print ("Registro de Personas")
personas = int (input ("Ingrese cantidad de personas a registrar: "))

genero = 0
hombres = 0
mujeres = 0

for i in range (personas):
    print (i+1,end=" ")
    input ("Ingrese Nombre:  ")
    genero = int (input("digite 1 si es femenino,\ndigite 2 si es masculino:\n"))
    if genero == 2:
        hombres = hombres + 1
    else:
        mujeres = mujeres + 1

print ("\n","Total Mujeres: ",mujeres)
print (" Total Hombres:  ",hombres)    