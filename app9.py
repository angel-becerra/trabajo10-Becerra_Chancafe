import libreria

def cursos_llevados():
    cursos=libreria.pedir_nombre("ingrese el curso donde quiere la informacion :")
    creditos=libreria.pedir_numero("ingrese el numero de  creditos del curso:",0,40)
    contenido= (cursos +"-"+  "-" + str(creditos) +  "\n")
    libreria.guardar_datos("universidad.txt", contenido,"a")
    print("datos guardados con exito")

def docentes():
    docente=libreria.pedir_nombre("ingrese el docente donde quiere la informacion :")
    edad=libreria.pedir_numero("ingrese la edad del docente:",0,100)
    contenido= (docente +"-"+  "-" + str(edad) +  "\n")
    libreria.guardar_datos("universidad.txt", contenido,"a")
    print("datos guardados con exito")

def mostrar_datos_brindados():
    datos=libreria.obtener_datos("universidad.txt")
    if(datos!= ""):
        print(datos)
    else:
        print("archivo sin datos")


opc=0
max=4

while (opc != max):
    print("###########    MENU     ##########")
    print("#1.cursos a cargo                    #")
    print("#2.docentes de la universidad        #")
    print("#3.mostrar los datos brindados       #")
    print("#4.salir                #")
    print("##########################")

    opc=libreria.pedir_numero("elija la opcion de donde este lo que deseas saber:",1,4)
    if (opc==1):
        cursos_llevados()
    if (opc==2):
        docentes()
    if (opc==3):
        mostrar_datos_brindados()
