archivo_externo = "E:\ServicioNacionaldeAprendizaje\MinTic2022\FundamentosProgramacion\Proyectos\ManejoDatos\personas.csv"
archivo_en_memoria = open(archivo_externo)
filecontents = archivo_en_memoria.read()

print ("\nEl contenido del archivo: " + archivo_externo + "es: \n")
print (filecontents)

archivo_en_memoria.close()