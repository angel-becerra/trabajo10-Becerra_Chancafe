import libreria

def jugar_futbol():
    futbol=libreria.pedir_nombre("ingrese el nombre del equipo:")
    nro_equipos=libreria.pedir_numero("ingrese el numero de equipos inscritos:",1,20)
    contenido= futbol + "el numero de equipo inscritos es es" + " "   +str(nro_equipos)+ "\n"
    libreria.guardar_datos("campeonato.txt", contenido,"a")
    print("datos guardados con exito")


def jugar_voley():
    voley=libreria.pedir_nombre("ingrese el nombre del equipo:")
    nro_equipos=libreria.pedir_numero("ingrese el numero de equipos inscritos:",1,20)
    contenido= voley + "el numero de equipo inscritos es es" + " "   +str(nro_equipos)+ "\n"
    libreria.guardar_datos("campeonato.txt", contenido,"a")
    print("datos guardados con exito")

def mostrar_datos():
    datos=libreria.obtener_datos("campeonato.txt")
    if(datos!= ""):
        print(datos)
    else:
        print("archivo sin datos")


opc=0
max=4

while (opc != max):
    print("###########MENU##########")
    print("#1.jugar fulbito    #")
    print("#2.jugar voley        #")
    print("#3.mostrar datos      #")
    print("#4.salir                #")

    opc=libreria.pedir_numero("ingese la opcion que desea realizar:",1,4)
    if (opc==1):
        jugar_futbol()
    if (opc==2):
        jugar_voley()
    if (opc==3):
        mostrar_datos()

#fin_menu
print("fin de las aperaciones realisadas")
