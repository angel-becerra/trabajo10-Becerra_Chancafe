import libreria
def funcion_manzana():
    print("garcias por preferir la fruta y comer saludable")

def funcion_mandarina():
    print("gracias por preferir la frruta y comer saludable")

def funcion_aji_uva():
    print("gracias pór preferir fruta y comer saludable")


def funcion_brocoli():
    print("garcias por preferir veduras , coma saludable")


def funcion_apio():
     print("garcias por preferir veduras , coma saludable")

def funcion_zanahoria():
     print("garcias por preferir veduras , coma saludable")


def frutas():
    opc=0
    max=4

    while opc != max:
        print("###################")
        print(" 1. manzana    #")
        print(" 2. mandarina  #")
        print(" 3. uva        #")
        print(" 4. Salir      #")
        print("###################")

        opc=libreria.pedir_numero("Seleccione su opcion",1,4)
        if opc == 1:
            funcion_mazana()
        if opc == 2:
            funcion_mandarina()
        if opc == 3:
            funcion_uva()

def verduras():
    opc=0
    max=4

    while opc != max:
        print("###################")
        print(" 1. brocoli    #")
        print(" 2. apio        #")
        print(" 3. zanahoria     #")
        print(" 4. Salir      #")
        print("###################")

        opc=libreria.pedir_numero("Seleccione su opcion",1,4)
        if opc == 1:
            funcion_brocoli()
        if opc == 2:
            funcion_apio()
        if opc == 3:
            funcion_zanahoria()



opc=0
max=4

while opc != max:
    print("###################")
    print("#1. verduras   #")
    print("#2. frutas     #")
    print("#3.mostrar pedido")
    print("#4.salir           #")
    print("###################")

    opc=libreria.pedir_numero("Sellecione su opcion:",1,2)
    if (opc == 1):
        verduras()
    if (opc==2):
        frutas()
    if (opc==3):
        mostrar_pedido()
print("Usted selecciono salir, muchas gracias. ")
