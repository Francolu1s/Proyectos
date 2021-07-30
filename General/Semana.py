
while (True):
    numeroIngresado = int(input("Ingrese un numero, y te dire a que dia de la semana pertenece: "))
    if numeroIngresado == 1:
        print ("Domingo")
    elif numeroIngresado == 2:
        print ("Lunes")
    elif numeroIngresado == 3:
        print ("Martes")
    elif numeroIngresado == 4:
        print ("Miercoles")            
    elif numeroIngresado == 5:
        print ("Jueves")
    elif numeroIngresado == 6:
        print ("Viernes")
    elif numeroIngresado == 7:
        print ("Sabado")        
    else:
        print ("El numero debe estar entre 1 y 7")    
