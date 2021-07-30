dividendo = 0
divisor = 0
modulo = 0
cociente = 0
bandera = 1

dividendo = int (input ("ingrese Dividendo: "))
divisor = int (input ("ingrese divisor: "))
print("Vamos a dividir:",dividendo, "entre", divisor)

if dividendo >= divisor:
    while bandera == 1 and dividendo > 1:
        print (dividendo, "-", divisor,"= ",end="")
        dividendo = dividendo - divisor
        print (dividendo)    
        cociente = cociente + 1
        if dividendo < divisor: 
            modulo = dividendo
            bandera = 0
                      
    print ("El cociente de la operacion es igual a:",cociente)
    print ("El modulo de la operacion es igual a:", modulo)

else:
    print ("Dividendo debe ser mayor a Divisor")