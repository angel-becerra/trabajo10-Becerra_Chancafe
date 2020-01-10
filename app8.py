import libreria

def sumar_los_numeros():
    x=libreria.pedir_numero("ingrese 1numero:",0,999999999999999)
    y=libreria.pedir_numero("ingrese 2numero:",0,999999999999999)
    contenido="la suma  entre los numeros:" +str(x) +"-"+ str(y) + "es:"+ str(x+y)+"\n"
    libreria.guardar_datos("numeros.txt", contenido,"a")
    print("datos guardados con exito")

def restar_numeros():
    a=libreria.pedir_numero("ingrese 1numero:",0,999999999999999)
    b=libreria.pedir_numero("ingrese 2numero:",0,999999999999999)
    contenido="la resta   entre los numeros:" +str(a) +"-"+ str(b) + "es:"+ str(a-b)+"\n"
    libreria.guardar_datos("numeros.txt", contenido,"a")
    print("datos guardados con exito")


def mostrar_resultados():
    datos=libreria.obtener_datos("numeros.txt")
    if(datos!= ""):
        print(datos)
    else:
        print("archivo sin datos")





opc=0
max=4
while (opc!=max):
    print("############MENU################")
    print("#1.sumas                       #")
    print("#2.resta                       #")
    print("#3.mostar los resultados       #")
    print("#4.salir                       #")
    print("################################")

    opc=libreria.pedir_numero("ingrese la opcion donde esta la operazion que desea realizar:",1,4)

    if (opc==1):
        sumar_los_numeros()
    if (opc==2):
        restar_numeros()
    if (opc==3):
        mostrar_resultados()
#fin_menu
print("usted a terminado las operacioes que deso realizar ,garcias por su preferencia")

