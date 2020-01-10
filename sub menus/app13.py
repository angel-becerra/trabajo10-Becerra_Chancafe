import libreria
def agregarsubopcionA():
    cliente=libreria.pedir_nombre("ingrese el nombre del cliente:")
    contenido= cliente + "\n"
    libreria.guardar_datos("menu2.txt",contenido, "a")
    print("nombre guardado")

def mostrarsubopcionA():
    datos=libreria.obtener_datos("menu2.txt")
    if (datos!=""):
        for item in datos:
            nombre=item.split("-")
            msg="su nombre es {}"
            print(msg.format(nombre))
        #fin_for
    else:
        print("no hay datos")


def agregarsubopcionB():
    telefono=libreria.pedir_numero("ingrese el nuro de telefono:",1,543654)
    contenido= str(telefono)+ "\n"
    libreria.guardar_datos("menu2.txt",contenido, "a")
    print("nro de ruc guardado")

def mostrarsubopcionB():
    datos=libreria.obtener_datos("menu2.txt")
    if (datos!=""):
        for item in datos:
            telefono=item.split("-")
            msg="su numero de telefono es {}"
            print(msg.format(telefono))
        #fin_for
    else:
        print("no hay datos")



def opcionA():
    opc=0
    max=3
    while (opc!=max):

        print("############ cliente ##########")
        print("#1.agregar nombre                #")
        print("#2.mostar datos              #")
        print("#3.salir                   #")
        print("############################")
        opc=libreria.pedir_numero("ingrese opcion :",1,3)
        if (opc==1):
            agregarsubopcionA()
        if (opc==2):
            mostrarsubopcionA()


def opcionB():
    opc=0
    max=3
    while (opc!=max):

       print("############ telefono ##########")
       print("#1.agragegar dato               #")
       print("#2.mostar dato              #")
       print("#3.salir                   #")
       print("############################")
       opc=libreria.pedir_numero("ingrese opciond :",1,3)
       if(opc ==1):
          agregarsubopcionB()
       if(opc ==2):
          mostrarsubopcionB()




opc=0
max=3
while (opc!=max):
    print("############ MENU ##########")
    print("#1.cliente                #")
    print("#2.telefono              #")
    print("#3.salir                   #")
    print("############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if(opc==1):
       opcionA()
    if(opc==2):
       opcionB()
#fin_while
print("fin del programa")
