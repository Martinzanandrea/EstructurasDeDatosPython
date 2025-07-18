#Para facilitar el relevamiento de datos de la ropa de trabajo de una empresa, se le
#solicita un programa que permita cargar para cada empleado los siguientes datos:
#Legajo int
#Apellido string
#Nombre string
#Camisa (talle) int
#Pantalón (talle) int
#Zapatos de Seguridad bool
#El programa a construir deberá permitir:
#a) Agregar una nueva persona a la lista.
#b) Quitar una persona.
#c) Ordenar la lista por legajo
#d) Ordenar la lista por apellido y nombre

lista =[] #Lista global
#procedimiento secundario
def es_seguro(dato):
    if dato.lower() == "si":
        segu = "Mis zapatos son seguros"
    else:
        segu = "Mis zapatos no son seguros, por favor unos nuevos!"
    return segu
#INGRESO DE DATOS PARA UN NUEVO EMPLEADO
def op_1():
    while True:
        nombre = str(input("Ingrese el nombre o 'salir' para terminar la carga de datos:   "))
        if nombre.lower() == "salir":
            menu_principal()
            break
        legajo = int(input("Ingrese el Nº de legajo del empleado"))     
        apellido =str(input("Ingrese el apelllido: "))
        talle = int(input("Ingrese su talle de camisa: "))
        talle2 =int(input("Ingrese su talla de pantalon:  "))
        seguro = es_seguro(str(input("Sus zapatos son seguros? Si/No : ")))
    
        info_cli ={
        "Legajo": legajo,
        "Nombre":nombre,
        "Apellido":apellido,
        "Camisa":talle,
        "Pantalon": talle2,
        "Zapatos":seguro
        }
        lista.append(info_cli)
#ELIMINAR ENPLEADO
def op_2():
    print("Eliminara a una persona de la lista!")
    leg = int(input("Ingrese el numero de legajo del empleado: "))
    global lista #modifica la lista global
    empleado_econtrado = False
    for info_cli in lista:
        if info_cli["Legajo"] == leg:
            lista.remove(info_cli)
            empleado_econtrado = True
            print("Empleado eliminado exitosamente")
            break        
    if not empleado_econtrado:
        print("Empleado no encontrado")
    menu_principal()   
#LISTA ORDENADA POR LEGAJO
def op_3():
    print("Lista ordenada por legajo: ")
    clave = "Legajo"
    lista_ordenada = sorted(lista, key=lambda x: x[clave])
    print("Lista ordenada por legajo: ")
    for info_cli in lista:
        print(   f" Legajo: {info_cli['Legajo']}",
                 f" Nombre: {info_cli['Nombre']}",
                 f" Apellido: {info_cli['Apellido']}")
        
    menu_principal()
#LISTA ORDENADA POR NOMBRE Y APELLIDO
def op_4():
    print("Lista ordenada por Nombre:")
    global lista
    clave2 = "Nombre"
    lista_ord2 = sorted(lista,key = lambda x:[clave2])
    for  info_cli in lista_ord2:
       print(f"Nombre:{info_cli["Nombre"]}",
             f" Apellido:{info_cli["Apellido"]}",
             f"Legajo: {info_cli["Legajo"]}")
    print("Lista ordenada por apellido: ")
    clave3 = "Apelllido"
    lista_ord3 = sorted(lista,key = lambda x:[clave3])
    for info_cli in lista_ord3:
        print(f"Apellido: {info_cli["Apellido"]}",
              f"Nombre: {info_cli["Nombre"]}",
              f"Legajo: {info_cli["Legajo"]}",
              f"Zapatos seguros:{info_cli["Zapatos"]}")
    menu_principal()
#MENU PRINCIPAL
def menu_principal():
 while True:
     print("Seleccione una opcion")
     print("1-Agregar una persona a la lista")
     print("2-Quitar una persona")
     print("3-Lista ord por legajo")
     print("4-Lista ordenanada por apellido y nombre")
     print("5-salir del programa")
     opcion = int(input("Ingrese la opcion: "))
     if opcion == 1 :
        op_1()
        break
     elif opcion == 2:
        op_2()
        break
     elif opcion == 3:
        op_3()
        break
     elif opcion == 4:
        op_4()
        break
     elif opcion == 5:
        print("saliendo del programa...")
        break
     else:
        print("opcion fuera de rango")
        continue
menu_principal()    


#profe sobre este punto quisiera una retroalimentacion , cosas a mejorar o algun error q haya pasado por alto
#el programa corre y necesita que los datos se carguen manualmente,luego las demas opciones pueden usarce.

   
            




