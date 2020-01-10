import libreria
#aplicacion para guardar
def agregar_curso():
    curso=libreria.pedir_nombre("ingrese curso:")
    nota=libreria.pedir_numero("ingrese nota:",1,100)
    contenido=curso + "-" + str(nota)+ "\n"
    libreria.guardar_datos("notas.txt", contenido,"a")
    print("datos guardados con exito")

def dar_informacion():
    datos=libreria.obtener_datos("notas.txt")
    if(datos!= ""):
        print(datos)
    else:
        print("archivo sin datos")

opc=0
max=3
while(opc != max):
    print("###########  MENU  ##########")
    print("1.agregar curso           #")
    print("2.dar informacion              #")
    print("3.salir                    #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if( opc==1 ):
        agregar_curso()
    if (opc==2):
        dar_informacion()

#fin_menu
print("fin del programa")
