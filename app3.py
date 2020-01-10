import libreria

def cosas_por_comprar():
    articulo_por_comprar=libreria.pedir_nombre("ingrese articulo qe desea obtener:")
    precio=libreria.pedir_numero("ingrese precio:",1,100)
    contenido= articulo_por_comprar + "el y el  precio  por este es" + " "   +str(precio)+ "\n"
    libreria.guardar_datos("lista.txt", contenido,"a")
    print("datos guardados con exito")

def mostrar_lista():
    datos=libreria.obtener_datos("lista.txt")
    if(datos!= ""):
        print(datos)
    else:
        print("archivo sin datos")


opc=0
max=3

while (opc != max):
    print("###########MENU##########")
    print("#1.cosas por comprar    #")
    print("#2.mostrar lista        #")
    print("#3.salir                #")

    opc=libreria.pedir_numero("ingese la opcion que desea realizar:",1,3)
    if (opc==1):
        cosas_por_comprar()
    if (opc==2):
        mostrar_lista()

#fin_menu
print("fin de las aperaciones realisadas")

