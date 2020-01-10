import libreria

def AgregarSubOpcionA():
    #1. pedir contraseña
    #2. Guardadr datos en contraseñas.txt
    universidad=libreria.pedir_nombre("Ingrese universidad: ")
    ciudad=libreria.pedir_nombre("Ingrese ciudad de la universidad: ")
    contenido = universidad + "-" + ciudad + "\n"
    libreria.guardar_datos("universidad.txt", contenido,"a")
    print("universidad guardada")

def MostrarSubOpcionB():
    # 1. Abrir el archivo contraseñas.txt y mostrar sus datos
    datos=libreria.guardar_datos("universidad.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            universidad, ciudad = item.split("-")
            msg="{} y pertenece a la ciuda de  {}"
            universidad=universidad.replace("\n","")
            ciudad=ciudad.replace("\n","")
            print(msg.format(universidad, ciudad))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionC():
    #1. pedir nombre
    #2. Guardadr datos en datos.txt
    nombre=libreria.pedir_nombre("Ingrese nombre: ")
    nro_de_examenes=libreria.pedir_numero("Ingrese nro de examenes: ",0,999999999)
    contenido = nombre + "-" + str(nro_de_examenes) + "\n"
    libreria.guardar_datos("universidad.txt", contenido,"a")
    print("guardado con exito")


def MostrarSubOpcionC():
     # 1. Abrir el archivo datos.txt y mostrar sus datos
    datos=libreria.obtener_datos("universidad.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            nombre, nro_de_examenes = item.split("-")
            msg="{} su nuero de examnes al año es {}"
            nombre=nombre.replace("\n","")
            nro_de_examenes=creditos.replace("\n","")
            print(msg.format(nombre,nro_de_examenes))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### universidades ########")
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
    print("##### nro de examenes ########")
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
    print("#1. universidad          #")
    print("#2. nro de examnenes          #")
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

