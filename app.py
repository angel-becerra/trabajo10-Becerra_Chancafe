import libreria

def agregar_cliente():
    # 1. Pedir la IP
    nombre=libreria.pedir_nombre("Ingrese el nombre del cliente:")
    serie=libreria.pedir_numero("Ingrese la serie:",-1000000000,101000)
    # 2. Guardar la IP en el archivo ip.txt
    contenido=nombre + "-" + str(serie) + "\n"
    libreria.guardar_datos("nombres.txt", contenido, "a")
    print("Datos guardados")

def mostrar_datos():
    # 1. Abrir el archivo ip.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("nombres.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            cliente, serie = item.split("-")
            msg="el cliente es {} y su serie es {}"
            cliente=cliente.replace("\n","")
            serie=serie.replace("\n","")
            print(msg.format(cliente,serie))
        #fin_for
    else:
        print("No hay datos")

opc=0
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. agregar cliente    #")
    print("# 2. motrar_datos     #")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregar_cliente()
    if ( opc ==2 ):
        mostrar_datos()
#fin_while
