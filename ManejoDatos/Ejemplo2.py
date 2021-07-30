archivo_externo = "E:\ServicioNacionaldeAprendizaje\MinTic2022\FundamentosProgramacion\Proyectos\ManejoDatos\personas.csv" 
archivo_en_memoria = open(archivo_externo, 'a') 
cedula = input("Digite Documento: ") 
nombre = input("Digite Nombre: ") 
archivo_en_memoria.write("\n" + cedula + "," + nombre) 
archivo_en_memoria.close()