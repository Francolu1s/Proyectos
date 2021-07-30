print ("\n","A continuacion ingrese los datos del empleado","\n")
nombreCompleto = input ("Ingrese nombre del empleado: ")
id = int (input ("# Documento: "))
salario = int (input ("Salario Devengado: $"))
valorxdiatrabajado = salario/30
print ("Valor por dia Laborado: $",f"{valorxdiatrabajado:.2f}")
valorHoraTrabajada= valorxdiatrabajado/8
valorHoraExtraNocturna = valorHoraTrabajada*1.75
horasExtrasNocturnas = int (input ("Ingrese # Horas Nocturnas laboradas:" ))
horasExtras = horasExtrasNocturnas * valorHoraExtraNocturna
print ("Total en horas Extras $",f"{horasExtras:.2f}")
valortotaldias = int (input ("Total dias trabajados: "))
print ("Total a Pagar: $",f"{valortotaldias * valorxdiatrabajado + horasExtras:.2f}","\n")

#print (valorHoraTrabajada)