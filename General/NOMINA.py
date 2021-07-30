
#Inicializar Variables Proceso Nómina
Nombre = ""
Sueldo = 0
Dias_Trabajados = 0
Numero_Horas_Extras = 0
Valor_hora_HEN = 0
valor_total_Horas_Extras = 0
Total_Pagar = 0

#Ingreso Información
#Inicializar Variables Proceso Nómina
Nombre = ""
Sueldo = 0
Dias_Trabajados = 0
Numero_Horas_Extras = 0
Valor_hora_HEN = 0
valor_total_Horas_Extras = 0
Total_Pagar = 0

#Ingreso Información
Nombre = input("Digite su Nombre: ")
Sueldo = float(input("Digite el Valor Sueldo Mensual: "))
Dias_Trabajados = int(input("Digite días trabajados: "))
Numero_Horas_Extras = int(input("Digite el Número HEN Trabajadas: "))

#Proceso de Nómina
print("")
print("********************************************************")
print("")

valor_dia = Sueldo / 30
valor_hora = valor_dia / 8
valor_hora_HEN = valor_hora + ((valor_hora*75)/100)



# valor a pagar por dias trabajados
valor_pagar_dias = Dias_Trabajados * valor_dia 

# valor a pagar por horas Extras
valor_total_Horas_Extras = Numero_Horas_Extras * valor_hora_HEN

# valor total a pagar por Persona
Total_Pagar = valor_pagar_dias + valor_total_Horas_Extras

#Proceso de Nómina
print("")
print("*******************VALOR A PAGAR NOMINA ******************************")
print("")
print("Empleado: ", Nombre)
print("Sueldo Empleado por Mes: ", Sueldo)
print("Dias Trabajador: ", Dias_Trabajados)
print("Numero horas Extras Nocturnas: ", Numero_Horas_Extras)
print("")
print("*******************VALOR A PAGAR NOMINA ******************************")
print("")
print("VALOR DEL DIA: ", valor_dia)
print("VALOR DE LA HORA: ", valor_hora)
print("VALOR DE 1 HEN: ", valor_hora_HEN)
print("")
print("*******************VALOR A PAGAR NOMINA ******************************")
print("")
print("Valor a pagar Horas Extras: ", valor_total_Horas_Extras)
print("Valor a pagar Dias Trabajados: ", valor_pagar_dias)
print("Total a Pagar: ", Total_Pagar)