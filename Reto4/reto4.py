import os
import time
import random
from math import asin,cos,sin,sqrt,radians,degrees

#region ENUNCIADO
#Tendremos la siguiente base de datos para trabajar.
# Lat1: 10,127
# Lon1: -74,950
# Numero de platos: 50
# Lat2: 10,196
# Lon2: -74,935
# Numero de platos: 15
# Lat3: 10,305
# Lon3: -75,040
# Numero de platos: 32
# Lat4: 10,196
# Lon4: -74,935
# Numero de platos: 17

#El usuario ingresará a la opción 3.
#en caso de que no existan restaurantes del sector (opción 2), mostrará un error y finalizará la ejecución.
#si ya están ingresadas el sistema nos mostrará sus 3 restaurantes favoritos (opción 2)
#y se le pedirá en qué restaurante se encuentra

#si se elige una opción inválida  mostrará error y volverá a la lista del menú.
#en caso de elegir una opción válida el programa calculará la distancia entre el restaurante actual
#y los de las bases de datos y mostrar los dos mas cercanos ordenados según la cantidad de platos.
#el usuario deberá elegir la opción 1 o la 2 para recibir indicaciones.

#el programa nos mostrará la dirección en la cual debe dirigirse (primero ir al sur, luego al occidente)
#y el tiempo aproximado que tardará en moto y en bicicleta
#endregion

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
ClaveGuardada="61225"
captcha1=216
captcha2=int((5*2)%(2**3)/(1+1))
captcha=captcha1+captcha2
radio=6372.795477598
listacoordenadas=[]
listadepuracion=[[10.103,-74.902],
                 [10.115,-75.085],
                 [10.108,-74.801]]
listadistancias=[]
restauranteactual=None
distanciaparatiempo=None
listacoordenadaspredet=[[6.124,-75.946,1035],
                        [6.125,-75.966,109],
                        [6.135,-75.976,31],
                        [6.144,-75.836,151]]
#endregion

def ImprimirLista(): 
    for x in range(len(listamenu)):
        print(f"{x+1} - {listamenu[x]}")

def ValidacionDatos(dato1,dato2):
    if dato1 == dato2:
        return True 
    else:
        return False 

def ReordenarFav(posicion): 
    mover=listamenu[posicion-1]
    listamenu.remove(mover)
    listamenu.insert(0,mover)

def ErrorConMensaje(mensaje):
    os.system("cls")
    print(mensaje)
    time.sleep(2)

def CambiarClave(claveactual):
    if ValidacionDatos(input("Por favor ingrese su contraseña actual: "), claveactual):
        nuevaclave=input("Por favor ingrese su nueva contraseña: ")
        if ValidacionDatos(nuevaclave,claveactual):
            ErrorConMensaje("La nueva contraseña no puede ser igual a la anterior.")
            return claveactual
        else:
            if ValidacionDatos(input("Por favor confirme su nueva contraseña: "), nuevaclave):
                return nuevaclave
                
            else:
                ErrorConMensaje("Las contraseñas no coinciden")
                return claveactual
    else:
        ErrorConMensaje("La contraseña es incorrecta")
        exit()
        
def IngresarCoordenadas(listaoriginal):
    listaduplicada=list(listaoriginal)
    for x in range (0,3):
        listaduplicada.append([])
        lat=input("Ingrese la latitud: ")
        while lat == "" or lat == " ":
            lat=input("La latitud no puede estar en blanco, por favor ingrésela de nuevo:")
        lat=float(lat)
        if lat >= 6.077 and lat <= 6.284:
            lon=input("Ingrese la longitud: ")
            while lon == "" or lon == " ":
                lon=input("La longitud no puede estar en blanco, por favor ingrésela de nuevo:")
            lon=float(lon)
            if lon >= -76.049 and lon <= -75.841:
                listaduplicada[x].insert(0,lat)
                listaduplicada[x].insert(1,lon)                
                
            else:
                ErrorConMensaje("Longitud fuera del rango")
                listaduplicada=[]
                return listaduplicada
        else:
            ErrorConMensaje("Latitud fuera del rango")
            listaduplicada=[]
            return listaduplicada
    print("Coordenadas Ingresadas correctamente")
    time.sleep(2)    
    return listaduplicada

def Ordenarlatitudes(listaoriginal):
    print(f"La coordenada que está mas al sur es: {min(listaoriginal, key=lambda posicion: posicion[0])}")

def OrdenarLongitudes(listaoriginal):
    print(f"La coordenada que está mas al oriente es: {max(listaoriginal, key=lambda posicion: posicion[1])}")
    
def PromedioCoordenadas(listaoriginal):
    print(f"EL promedio de las latitudes es: {(listaoriginal[0][0]+listaoriginal[1][0]+listaoriginal[2][0])/3}")

def ImprimirCoordenads(listaoriginal):
    
    listaduplicada=list(listaoriginal)
    print("Las coordenadas guardadas actualmente son: ")

    for x in range(0,len(listaduplicada)):
        print(f"{x+1}. Coordenada Latitud:'{listaduplicada[x][0]}' Longitud: '{listaduplicada[x][1]}'")
    Ordenarlatitudes(listaduplicada)
    OrdenarLongitudes(listaduplicada)
    PromedioCoordenadas(listaduplicada)
    choice=int(input("Por favor ingrese la opción que desea modificar:"))

    if choice !=1 and choice !=2 and choice !=3:
        ErrorConMensaje("Esa opción es inválida")
        return 
    else:
      
        ActualizarCoordenadas(choice,listaoriginal)

def ActualizarCoordenadas(choice,listaoriginal):

    listaduplicada=list(listaoriginal)
    choice=choice-1 
    lat=input("Ingrese la latitud: ")
    while lat == "" or lat == " ":
        lat=input("La latitud no puede estar en blanco, por favor ingrésela de nuevo:")
    lat=float(lat)
    if lat >= 10.103 and lat <= 10.362:
        lon=input("Ingrese la longitud: ")
        while lon == "" or lon == " ":
            lon=input("La longitud no puede estar en blanco, por favor ingrésela de nuevo:")
        lon=float(lon)
        if lon >= -75.088 and lon <= -74.319:

            listaduplicada[choice][0]=lat
            listaduplicada[choice][1]=lon
            
        else:
            ErrorConMensaje("Longitud fuera del rango")
            listaduplicada=[listaoriginal] 
            return listaduplicada
    else:
        ErrorConMensaje("Latitud fuera del rango")
        listaduplicada=[listaoriginal] 
        return listaduplicada
    
    return listaduplicada
    
def MostrarRestaurantesFav(listaoriginal):
    if listaoriginal==[]:
        ErrorConMensaje("Error sin registro de coordenadas")
        exit()
    else:

        ImprimirRestaurantesFav(listaoriginal)
        
def ImprimirRestaurantesFav(listaoriginal):
    listaduplicada=list(listaoriginal)
    print("Las coordenadas guardadas actualmente son: ")

    for x in range(0,len(listaduplicada)):
        print(f"{x+1}. Coordenada Latitud:'{listaduplicada[x][0]}' Longitud: '{listaduplicada[x][1]}'")
        
    opcion=int(input("Por favor seleccione su restaurante actual: "))
    if opcion == 1 or opcion ==2 or opcion ==3:
        global restauranteactual
        restauranteactual=listacoordenadas[opcion-1]
        PrepararDatos(opcion,listaduplicada,listacoordenadaspredet)
    else:
        ErrorConMensaje("Error ubicación")
        exit()

def PrepararDatos(IndRestauranteactual,listaoriginal,coordenadasfijas):
    listaduplicada=list(listaoriginal)
    listaduplicadafijas=list(coordenadasfijas)
    lat1=listaduplicada[IndRestauranteactual-1][0]
    lon1=listaduplicada[IndRestauranteactual-1][1]
    lat1=convertiraRadianes(lat1)
    lon1=convertiraRadianes(lon1)
    
    for x in range(0,len(listaduplicadafijas)):
        for y in range (0,2):
           
            listaduplicadafijas[x][y]=convertiraRadianes(listaduplicadafijas[x][y])
    
    AplicarFormulaDistancia(lat1,lon1,listaduplicadafijas)
    
    pass

def convertiraRadianes(valoraconvertir):
    return radians(valoraconvertir)
    pass

def AplicarFormulaDistancia(lat1, lon1, listaenradianes):

    
    for x in range(0,4):
        lat2=listaenradianes[x][0]
        lon2=listaenradianes[x][1]
        latdelta=lat2-lat1
        londelta=lon2-lon1

        auxiliarcalculo=sin(londelta/2)**2
        auxiliarcalculo=auxiliarcalculo*(cos(lat1)*cos(lat2))
        auxiliarcalculo=(sin(latdelta/2)**2)+auxiliarcalculo
        auxiliarcalculo=sqrt(auxiliarcalculo)
        auxiliarcalculo=asin(auxiliarcalculo)
        auxiliarcalculo=(2*radio)*auxiliarcalculo

        auxiliarcalculo=auxiliarcalculo*1000
        auxiliarcalculo=round(auxiliarcalculo)
       
        listadistancias.append(auxiliarcalculo)

    OrdenarDistancias(listadistancias)

def OrdenarDistancias(distancias):
    distanciasduplicadas=list(distancias)
    min1=distanciasduplicadas.index(min(distanciasduplicadas)) 
    distanciasduplicadas.pop(min1)
   
    min2=distancias.index(min(distanciasduplicadas))
               
    
    ImprimirMensajeCercanias(min1,min2,listacoordenadaspredet,distancias)

def ImprimirMensajeCercanias(min1,min2, basededatos,listadistancias ):
    for x in range (0,4):
        basededatos[x][0]=degrees(basededatos[x][0])
        basededatos[x][1]=degrees(basededatos[x][1])
    

    for x in range (0,len(listacoordenadaspredet)):
        if listacoordenadaspredet[min1][0]==listacoordenadaspredet[x][0] and listacoordenadaspredet[min1][1] == listacoordenadaspredet[x][1]:
            if listacoordenadaspredet[x][2]>listacoordenadaspredet[min1][2]:
                min1=listacoordenadaspredet.index(listacoordenadaspredet[x])
                

    global distanciaparatiempo 
    if basededatos[min1][2] > basededatos[min2][2]:
        
        print(f"1. El restaurante más cercano está en la latitud: '{basededatos[min1][0]}' longitud: '{basededatos[min1][1]}', está a {listadistancias[min1]} metros, y tiene {basededatos[min1][2]} platos.")
        print(f"2. El segundo restaurante más cercano está en la latitud: '{basededatos[min2][0]}' longitud: '{basededatos[min2][1]}', está a {listadistancias[min2]} metros, y tiene {basededatos[min2][2]} platos.")
        opcdestino=int(input("Por favor seleccione el restaurante al cual desea ir, para recibir indicaciones: "))
        if opcdestino==1: 
            distanciaparatiempo = listadistancias[min1] 
            DarIndicaciones(restauranteactual,basededatos[min1])
        elif opcdestino==2:
            distanciaparatiempo = listadistancias[min2]
            DarIndicaciones(restauranteactual,basededatos[min2])
        else:
            ErrorConMensaje("Restaurante destino inválido.")
        
    else:
        print(f"1. El restaurante más cercano está en la latitud: '{basededatos[min2][0]}' longitud: '{basededatos[min2][1]}', está a {listadistancias[min2]} metros, y tiene {basededatos[min2][2]} platos.")
        print(f"2. El segundo restaurante más cercano está en la latitud: '{basededatos[min1][0]}' longitud: '{basededatos[min1][1]}', está a {listadistancias[min1]} metros, y tiene {basededatos[min1][2]} platos.")
        opcdestino=int(input("Por favor seleccione el restaurante al cual desea ir, para recibir indicaciones: "))
        if opcdestino==1:
            distanciaparatiempo= listadistancias[min2]
            DarIndicaciones(restauranteactual,basededatos[min2])
        elif opcdestino==2:
            distanciaparatiempo= listadistancias[min1]
            DarIndicaciones(restauranteactual,basededatos[min1])
        else:
            ErrorConMensaje("Error zona wifi")
            exit ()

def DarIndicaciones(restactual,restdestino):

    latorigen=restactual[0]
    lonorigen=restactual[1]
    latdestino=restdestino[0]
    londestino=restdestino[1]

    if latorigen>latdestino:
        txt1="el sur"
    elif latorigen<latdestino:
        txt1="el norte"

    else:
        txt1=""
      
    if lonorigen>londestino:
        txt2="el occidente"
    elif lonorigen<londestino:
        txt2="el oriente"
    else:
        txt2=""
    

    if txt1=="" and txt2!="": 
        print(f"Debe ir hacia {txt2}")

    elif txt2=="" and txt1!="": 
        print(f"Debe ir hacia {txt1}")

    elif txt1=="" and txt2=="":
        print("Usted ya está en el destino")
        time.sleep(3)
        

    else:
        print(f"Debe dirigirse primero hacia {txt1} y luego hacia {txt2}")
        
        time.sleep(2)
        CalcularTiempoRecorrido()    
   
def CalcularTiempoRecorrido():
    tiempo1="segundos" 
    tiempo2="segundos"
    
    if distanciaparatiempo==0: 
        pass
        
    else:
        auto=distanciaparatiempo/20.83 
        moto=distanciaparatiempo/19.44
        
        if auto > 60: 
            auto=auto/60
            tiempo1="minutos"
        
        
        if moto > 60:
            moto=moto/60
            tiempo2="minutos"
        
        moto=round(moto,2) 
        auto=round(auto,2)
               
        print(f"Se tardará aproximadamente {auto} {tiempo1} en auto; y {moto} {tiempo2} en moto")
        time.sleep(3)
        input("Presione 0 para salir: ")
        
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
UsuarioIngresado=input("Ingrese su usuario: ")
if ValidacionDatos(UsuarioGuardado,UsuarioIngresado): 
    if ValidacionDatos(input("Ingrese su contraseña: "), ClaveGuardada): 
        verificacion=int(input(f"Por favor resuelva la siguiente operación {captcha1} + {captcha2}: "))
        if ValidacionDatos(captcha,verificacion): 
            os.system("cls") 
            print("Sesión Iniciada.")
            time.sleep(2)
            while contadorerrores<5:
                listadistancias=[] 
                os.system("cls")
                ImprimirLista()
                opcionelegida=int(input("Por favor selecciona una opción: ")) 
                if opcionelegida > 0 and opcionelegida < 8:
                    opcionelegidalista=listamenu[opcionelegida-1] 
                    
                    if opcionelegidalista==opc1:
                        print(opc1)
                        ClaveGuardada=CambiarClave(ClaveGuardada)
                    elif opcionelegidalista==opc2:
                        print(opc2)
                        if listacoordenadas==[]:
                            listacoordenadas=IngresarCoordenadas(listacoordenadas)
                        else:
                            ImprimirCoordenads(listacoordenadas)
                        
                    elif opcionelegidalista==opc3:

                        MostrarRestaurantesFav(listacoordenadas) 

                    elif opcionelegidalista==opc4:
                        print(opc4)
                        time.sleep(2)
                    elif opcionelegidalista==opc5:
                        print(opc5)
                        time.sleep(2)
                    elif opcionelegidalista==opc6:
                        print(opc6)
                        nuevofavorito=int(input("Ingrese el número de la opción que desea mover: ")) 
                        if nuevofavorito == 1 or nuevofavorito ==2 or nuevofavorito ==3 or nuevofavorito ==4 or nuevofavorito==5: 
                            if int(input(f"Por favor escriba el siguiente número: UNO ")) == 1:
                                if int(input("Por favor resuelva la siguiente operacion (6 + 6)/12:"))==1:                            
                                    ReordenarFav(nuevofavorito)
                                
                                else:
                                    ErrorConMensaje ("Error") # ("Error comprobación 2") 
                            else:
                                ErrorConMensaje ("Error") # ("Error comprobación 1")
                        else:
                            ErrorConMensaje ("Error") # ("Opción Inválida")
                            continue 
                    elif opcionelegidalista==opc7:
                        ErrorConMensaje ("Hasta pronto") # ("Sesión cerrada")
                        exit()
                else:
                    contadorerrores+=1 
                    ErrorConMensaje ("Error") # ("Opción no válida")
                    continue    
    
        else:
            ErrorConMensaje ("Error") #("Error captcha incorrecto")
    else:
        ErrorConMensaje("Error") # ("Error contraseña incorrecta")
else:
    ErrorConMensaje ("Error") #("Error usuario incorrecto")