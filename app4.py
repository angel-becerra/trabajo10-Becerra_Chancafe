import libreria

def paciente():
    nombre=libreria.pedir_nombre("ingrese el nombre del paciente que desea ver :")
    habitacion=libreria.pedir_numero("ingrese en numero de habitacion en donde se encuentra:",0,40)
    contenido= (nombre +"-"+  "-" + str(habitacion) +  "\n")
    libreria.guardar_datos("enfermeria.txt", contenido,"a")
    print("datos guardados con exito")

def mostrar_datos_guardados():
    datos=libreria.obtener_datos("enfermeria.txt")
    if(datos!= ""):
        print(datos)
    else:
        print("archivo sin datos")


opc=0
max=4

while (opc != max):
    print("###########MENU##########")
    print("#1.paciente    #")
    print("#2.numero de habitacion")
    print("#3.mostrar datos guardados")
    print("#4.salir                #")
    print("##########################")

    opc=libreria.pedir_numero("Elija la opcion de la cual requiere la informacion:",1,4)
    if (opc==1):
        paciente()
    if (opc==2):
        numero_de_habitacion()
    if (opc==3):
        mostrar_datos_guardados()


#fin_menu
print("fin de las aperaciones realisadas")

