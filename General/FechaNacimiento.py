AA = 2021 
MA = 7 
DA = 22 

AN = int(input("Digite su Año de Nacimiento: ")) 
MN = int(input("Digite su Mes de Nacimiento: ")) 
DN = int(input("Digite su Dia de Nacimiento: "))

if DA >= DN: 
    DA = DA - DN 
else: 
    DA = DA + 30 
    DA = DA - DN 
    MA = MA - 1 

if MA >= MN:
    MA = MA - MN
else:
    MA = MA + 12
    MA = MA - MN
    AA = AA - 1

print (f"usted tiene {AA - AN} años {MA} meses y {DA} dias")

