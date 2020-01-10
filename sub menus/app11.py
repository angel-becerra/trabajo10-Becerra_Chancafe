import libreria
def agregarsubopcionA():
    nombre=libreria.pedir_nombre("ingrese el nombre de la empresa:")
    contenido= nombre
    libreria.guardar_datos("menu1.txt",contenido, "a")
    print("nombre guardado")

def mostrarsubopcionA():
    datos=libreria.obtener_datos("menu1.txt")
    if (datos!=""):
        for item in datos:
            nombre=item.split("-")
            msg="su nombre es {}"
            print(msg.format(nombre))
        #fin_for
    else:
        print("no hay datos")


def agregarsubopcionB():
    nro_ruc=libreria.pedir_numero("ingrese el nro de ruc:",1,543654)
    contenido= str(nro_ruc)
    libreria.guardar_datos("menu1.txt",contenido, "a")
    print("nro de ruc guardado")

def mostrarsubopcionB():
    datos=libreria.obtener_datos("menu1.txt")
    if (datos!=""):
        for item in datos:
            nro_de_ruc=item.split("-")
            msg="su numero de ruc es {}"
            print(msg.format(nro_de_ruc))
        #fin_for
    else:
        print("no hay datos")



def opcionA():
    opc=0
    max=3
    while (opc!=max):

        print("############ EMPRESA ##########")
        print("#1.agregar nombre                #")
        print("#2.mostar datos              #")
        print("#3.salir                   #")
        print("############################")
        opc=libreria.pedir_nombre("ingrese opcion :",1,3)
        if (opc==1):
            agregarsubopcionA()
        if (opc==2):
            mostrarsubopcionA()


def opcionB():
    opc=0
    max=3
    while (opc!=max):

       print("############ NRO DE RUC ##########")
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
    print("#1.empresa                 #")
    print("#2.nro de ruc              #")
    print("#3.salir                   #")
    print("############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if(opc==1):
       opcionA()
    if(opc==2):
       opcionB()
#fin_while
print("fin del programa")
