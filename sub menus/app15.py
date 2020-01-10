import libreria

def AgregarSubOpcionA():
    #1. pedir contraseña
    #2. Guardadr datos en contraseñas.txt
    contrasenia=libreria.pedir_numero("Ingrese contraseña: ",0,455445555)
    nro_contrasenia=libreria.pedir_numero("Ingrese nro: ",0,100000000)
    contenido = str(contrasenia) + "-" + str(nro_contrasenia) + "\n"
    libreria.guardar_datos("contraseñas.txt", contenido,"a")
    print("contraseña guardada")

def MostrarSubOpcionB():
    # 1. Abrir el archivo contraseñas.txt y mostrar sus datos
    datos=libreria.guardar_datos("contraseñas.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            contrasenia, nro_contrasenias = item.split("-")
            msg="{} es la contraseña {}"
            contrasenia=contrasenia.replace("\n","")
            nro_contrasenias=nro_contrasenias.replace("\n","")
            print(msg.format(contrasenia, nro_contrasenias))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionC():
    #1. pedir nombre
    #2. Guardadr datos en datos.txt
    nombre=libreria.pedir_nombre("Ingrese nombre: ")
    telefono=libreria.pedir_numero("Ingrese nro de telefono: ",0,999999999)
    contenido = nombre + "-" + str(telefono) + "\n"
    libreria.guardar_datos("datos.txt", contenido,"a")
    print("cuenta creada y guardada")


def MostrarSubOpcionC():
     # 1. Abrir el archivo datos.txt y mostrar sus datos
    datos=libreria.guardar_datos("datos.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            nombre, nro_telefono = item.split("-")
            msg="{} su numero de telefono es {}"
            nombre=nombre.replace("\n","")
            nro_telefono=nro_telefono.replace("\n","")
            print(msg.format(nombre, nro_telefono))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### INICIAR CESION ########")
    print("#1. Agregar  contraseña     #")
    print("#2. mostrar contraseña       #")
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
    print("##### CREAR CUENTA ########")
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
    print("#1. INICIAR CESION            #")
    print("#2. CREAR CUENTA              #")
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

