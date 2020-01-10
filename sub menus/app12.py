import libreria
def funcion_arroz_con_pato():
    print("garcias por preferir el arroz con pato")
    print("disfrute su comida")

def funcion_cabrito():
    print("gracias por preferir el plato cabrito")
    print("disfrute su comida")

def funcion_aji_de_gallina():
    print("gracias pór preferir aji de gallina")
    print("disfrutr su comida")


def funcion_arroz_con_lrche():
    print("garcias por preferir el arroz con leche")
    print("disfrute su postre")

def funcion_mazamorra():
    print("gracias por preferir la mazamorra")
    print("disfrute su postre")

def funcion_arroz_zambito():
    print("gracias pór preferir arroz zambito")
    print("disfrutr su postre")


def platos_tipicos():
    opc=0
    max=4

    while opc != max:
        print("###################")
        print(" 1. arroz con pato    #")
        print(" 2. cabrito  #")
        print(" 3. aji de gallina  #")
        print(" 4. Salir      #")
        print("###################")

        opc=libreria.pedir_numero("Seleccione su opcion",1,4)
        if opc == 1:
            funcion_arroz_con_pato()
        if opc == 2:
            funcion_cabrito()
        if opc == 3:
            funcion_aji_de_gallina()

def postres():
    opc=0
    max=4

    while opc != max:
        print("###################")
        print(" 1. arroz con leche    #")
        print(" 2. mazamorra        #")
        print(" 3. arroz zambito     #")
        print(" 4. Salir      #")
        print("###################")

        opc=libreria.pedir_numero("Seleccione su opcion",1,4)
        if opc == 1:
            funcion_arroz_con_leche()
        if opc == 2:
            funcion_mazamorra()
        if opc == 3:
            funcion_aji_de()



opc=0
max=4

while opc != max:
    print("###################")
    print("#1. Platos tipicos   #")
    print("#2. postres    #")
    print("#3.mostrar pedido")
    print("#4.salir           #")
    print("###################")

    opc=libreria.pedir_numero("Sellecione su opcion:",1,2)
    if (opc == 1):
        platos_tipicos()
    if (opc==2):
        postres()
    if (opc==3):
        mostrar_pedido
print("Usted selecciono salir, muchas gracias. ")
