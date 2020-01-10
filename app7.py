import libreria

def corredor_nro1():
    corredor=libreria.pedir_nombre("ingrese el nombre del corredor nro1:")
    distancia_total=libreria.pedir_numero("ingrese la distancia total:",1,1000)
    distancia_recorrida=libreria.pedir_numero("ingrese la distancia recorrida:",1,100)
    contenido= corredor + "y su distancia recorrida es" + " "   +str(distancia_recorrida)+ "\n"
    libreria.guardar_datos("carrera.txt", contenido,"a")
    print("datos guardados con exito")

def corredor_nro2():
    corredor=libreria.pedir_nombre("ingrese el nombre del corredor nro2:")
    distancia_total=libreria.pedir_numero("ingrese la distancia total:",1,1000)
    distancia_recorrida=libreria.pedir_numero("ingrese la distancia recorrida:",1,100)
    contenido= corredor + "y su distancia recorrida es" + " "   +str(distancia_recorrida)+ "\n"
    libreria.guardar_datos("carrera.txt", contenido,"a")
    print("datos guardados con exito")



def mostrar_las_distancias_recorridas():
    datos=libreria.obtener_datos("carrera.txt")
    if(datos!= ""):
        print(datos)
    else:
        print("archivo sin datos")


opc=0
max=4

while (opc != max):
    print("###################  MENU  #############")
    print("#1.corredor 1                          #")
    print("#2.corredor 2                          #")
    print("#3.mostrar las distancias recorridas   #")
    print("#4.salir                               #")

    opc=libreria.pedir_numero("ingese la opcion donde quiere ver la informacion:",1,4)
    if (opc==1):
        corredor_nro1()
    if (opc==2):
        corredor_nro2()
    if (opc==3):
        mostrar_las_distancias_recorridas()

#fin_menu
print("fin de las aperaciones realisadas")
