#Funcion que imprima lista
#Función que valide datos
#función que reordene el favorito
#función de error con mensaje personalizado

import os
import time
import random 

#Las regiones nos permiten colapsar ciertas partes del código

#region VARIABLES GLOBALES
opc1="Cambiar contraseña"
opc2="Ingresar coordenadas actuales"
opc3="Ubicar zona wifi más cercana"
opc4="Guardar archivo con ubicación cercana"
opc5="Actualizar registros de zonas wifi desde archivo"
opc6="Elegir opción de menú favorita"
opc7="Cerrar sesión"
listamenu=[opc1,opc2,opc3,opc4,opc5,opc6,opc7]
contadorerrores=0
UsuarioGuardado="52216"
ClaveGuardada=61225
captcha1=216
captcha2=int((5*2)%(2**3)/(1+1))
captcha=captcha1+captcha2 
#endregion

def ImprimirLista(): #Nos permite imprimir la lista
    for x in range(len(listamenu)):
        print(f"{x+1} - {listamenu[x]}")

def ValidacionDatos(dato1,dato2):#Toma como entrada dos parámetros a comparar, ej: UsuarioGuardado,UsuarioIngresado
    if dato1 == dato2:
        return True #Verdadero si son iguales
    else:
        return False #falso si son diferentes

def ReordenarFav(posicion): #Toma como entrada un parámetro que se usa para crear la variable mover
    mover=listamenu[posicion-1]
    listamenu.remove(mover)
    listamenu.insert(0,mover)

def ErrorConMensaje(mensaje):#Toma como entrada un mensaje personalizado que se imprimirá en pantalla
    os.system("cls")
    print(mensaje)
    time.sleep(1)

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
UsuarioIngresado=input("Ingrese su usuario: ")
if ValidacionDatos(UsuarioGuardado,UsuarioIngresado): #Se llama la función desde un condicinal por eso los dos puntos 
    if ValidacionDatos(int(input("Ingrese su contraseña: ")), ClaveGuardada): #El primer parámetro para la función, se toma desde un input
        verificacion=int(input(f"Por favor resuelva la siguiente operación {captcha1} + {captcha2}: "))
        if ValidacionDatos(captcha,verificacion): 
            os.system("cls")
            print("Sesión Iniciada.")
            time.sleep(2)
            while contadorerrores<=3:
                os.system("cls")
                ImprimirLista() #Llamamos a la función que nos imprime la lista
                opcionelegida=int(input("Elija una opción")) 
                #Recordar que ésta condición evita un error que corregí en el video
                #Debe revisarse si el número elegido está dentro del rango
                #Para evitar que sea buscado en la lista una posición que no existe.
                if opcionelegida > 0 and opcionelegida < 8:
                    opcionelegidalista=listamenu[opcionelegida-1]                     
                    if opcionelegidalista==opc1:
                        print("Usted ha elegido la opción número 1") 
                        time.sleep(2)
                    elif opcionelegidalista==opc2:
                        print("Usted ha elegido la opción número 2")
                        time.sleep(2)
                    elif opcionelegidalista==opc3:
                        print("Usted ha elegido la opción 3 ")
                        time.sleep(2)
                        exit()
                    elif opcionelegidalista==opc4:
                        print("Usted ha elegido la opción número 4")
                        time.sleep(2)
                    elif opcionelegidalista==opc5:
                        print("Usted ha elegido la opción número 5")
                        time.sleep(2)
                    elif opcionelegidalista==opc6:
                        print("Usted ha elegido la opción número 6")
                        nuevofavorito=int(input("Seleccione opción favorita")) 
                        if nuevofavorito == 1 or nuevofavorito ==2 or nuevofavorito ==3 or nuevofavorito ==4 or nuevofavorito==5:                         
                            if int(input(f"Por favor escriba el siguiente número: UNO ")) == 1:
                                if int(input("Por favor resuelva la siguiente operacion (6 + 6)/12:"))==1:
                                    ReordenarFav(nuevofavorito)#Se llama la función reordenar fav, el parámetro es en número ingresado por el usuario                                
                                else:
                                    ErrorConMensaje("Error") #Se llama la función de error con mensaje, y se manda el error a mostrar.
                            else:
                                ErrorConMensaje("Error")
                        else:
                            ErrorConMensaje("Error")
                            exit()
                            #continue #Recordar que continues, breaks y exit no están dentro de la función.
                    elif opcionelegidalista==opc7:
                        ErrorConMensaje("Hasta pronto")
                        exit()
                else:
                    contadorerrores+=1 
                    ErrorConMensaje("Error")
                    continue        
        else:
            ErrorConMensaje("Error")
    else:
        ErrorConMensaje("Error")
else:
    ErrorConMensaje("Error")