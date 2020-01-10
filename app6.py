import libreria

def  ciudades_del_peru():
    ciudad=libreria.pedir_nombre("ingrese la ciudad domde desea ir :")
    dias_de_visita=libreria.pedir_numero("ingrese el numero de dias que piensa quedarse en dicho lugar:",0,40)
    contenido= (ciudad +"-"+  "-" + str(dias_de_visita) +  "\n")
    libreria.guardar_datos("destinos.txt", contenido,"a")
    print("datos guardados con exito")

def  paises_del_mundo():
    paises=libreria.pedir_nombre("ingrese el pais domde desea ir :")
    dias_de_visita=libreria.pedir_numero("ingrese el numero de dias que piensa quedarse en dicho lugar:",0,40)
    contenido= (paises +"-"+  "-" + str(dias_de_visita) +  "\n")
    libreria.guardar_datos("destinos.txt", contenido,"a")
    print("datos guardados con exito")

def mostrar_los_destinos_elejidos():
    datos=libreria.obtener_datos("destinos.txt")
    if(datos!= ""):
        print(datos)
    else:
        print("archivo sin datos")


opc=0
max=4

while (opc != max):
    print("###########    MENU     ##########")
    print("#1.ciudades                      #")
    print("#2.paises                        #")
    print("#3.mostrar los destinos elejidos #")
    print("#4.salir                #")
    print("##########################")

    opc=libreria.pedir_numero("Elija la opcion donde este el destino de su preferencia:",1,4)
    if (opc==1):
        ciudades_del_peru()
    if (opc==2):
        paises_del_mundo()
    if (opc==3):
        mostrar_los_destinos_elejidos()

