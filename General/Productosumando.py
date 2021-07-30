print ("\n","¡Vas a multiplicar DOS numeros enteros!","\n")

num1 = int ((input ("Ingrese primer numero:  ")))
num2 = int((input ("Ingrese segundo numero:  ")))

print ("\n","Primer opcion:")    
print (num1,"X",num2,"=",num1*num2)

print ("\n","Segunda opcion:")
for i in range (num2):
    print(num1,end="")
    if i < (num2-1):
        print ("+",end="")
print (" =",num1*num2)

if (num1 != num2):
    print ("\n","Tercera opcion:")
    for i in range (num1):
        print(num2,end="")
        if i < (num1-1):
            print ("+",end="")
    print (" =",num1*num2,"\n")