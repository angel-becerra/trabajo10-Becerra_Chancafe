import libreria

def AgregarSubOpcionA():
    #1. pedir contraseña
    #2. Guardadr datos en contraseñas.txt
    curso=libreria.pedir_nombre("Ingrese curso: ")
    docente=libreria.pedir_nombre("Ingrese docente: ")
    contenido = curso + "-" + docente + "\n"
    libreria.guardar_datos("creditos.txt", contenido,"a")
    print("curso guardada")

def MostrarSubOpcionB():
    # 1. Abrir el archivo contraseñas.txt y mostrar sus datos
    datos=libreria.guardar_datos("creditos.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            curso, docente = item.split("-")
            msg="{} y el docente es {}"
            curso=curso.replace("\n","")
            docente=docente.replace("\n","")
            print(msg.format(curso, docente))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionC():
    #1. pedir nombre
    #2. Guardadr datos en datos.txt
    curso=libreria.pedir_nombre("Ingrese nombre: ")
    creditos=libreria.pedir_numero("Ingrese nro de de creditos: ",0,999999999)
    contenido = curso + "-" + str(creditos) + "\n"
    libreria.guardar_datos("creditos.txt", contenido,"a")
    print("cuenta creada y guardada")


def MostrarSubOpcionC():
     # 1. Abrir el archivo datos.txt y mostrar sus datos
    datos=libreria.obtener_datos("creditos.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            curso, creditos = item.split("-")
            msg="{} su numero de telefono es {}"
            curso=curso.replace("\n","")
            creditos=creditos.replace("\n","")
            print(msg.format(curso,creditos))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### curso ########")
    print("#1. Agregar  nombre     #")
    print("#2. mostrar nombre       #")
    print("#3. salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionA()
    if(opc==2):
        MostrarSubOpcionB()
    #fin if
#fin while

def OpcionB():
    print("##### nro de creditos ########")
    print("#1. agregar datos     #")
    print("#2. mostrar datos       #")
    print("#3. salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionC()
    if(opc==2):
        MostrarSubOpcionC()
    #fin if
#fin while

opc=""
max=3
while(opc!=max):
    print("############ MENU #############")
    print("#1. curso           #")
    print("#2. nro de creditos           #")
    print("#3. Salir                     #")
    print("###############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        OpcionA()
    if(opc==2):
        OpcionB()
    #fin if
#fin while
print("fin")

