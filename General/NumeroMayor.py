print ("\n","Vas a ingresar 3 numeros y te voy a decir cual es el mayor","\n")
num1 = int (input ("Ingrese primer numero:  "))
num2 = int (input ("Ingrese segundo numero:  "))
if (num1 != num2):
    num3 = int (input ("Ingrese tercer numero:  "))
    if (num3 != num1):
        if (num1 > num2) and (num1 > num3):
            print ("    El primer numero ingresado es el mayor")
        elif (num2 > num1) and (num2 > num3):
            print ("    El segundo numero ingresado es el mayor")    
        else:
            print ("    El tercer numero ingresado es el mayor")   
    else: print ("Deben ser Numeros diferentes")
else: print ("Deben ser Numeros diferentes")
print("\n")