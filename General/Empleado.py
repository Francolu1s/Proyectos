print ("A continuacion ingrese los datos del empleado")
nombreCompleto = input ("Ingrese nombre del empleado: ")
id = int (input ("# Documento: "))
salario = int (input ("Salario Devengado: $"))
valorxdiatrabajado = salario/30
print ("Valor por dia Laborado: $",f"{valorxdiatrabajado:.2f}")
Valortotaldias = int (input ("Total dias trabajados: "))
print ("Total a Pagar: $",f"{Valortotaldias * valorxdiatrabajado:.2f}","\n")