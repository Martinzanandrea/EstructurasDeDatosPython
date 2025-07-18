"""
Solicite al usuario el ingreso de un número entero entre 1 y 20 y muestre por
pantalla las tablas de multiplicación del 1 al 10
"""
#Inicio
while True:
    try:
         n = int(input("Ingrese un valor del 1 al 20 :  "))
         if  (1 <= n <= 20) : 
                break
         else:
             print("el numero esta fuera del rango, intentelo nuevamente")
    except ValueError : #Puse except ,por si se llegara a ingresar un float
         print("Por favor ingrese un numero entero valido")
print(f"Las tablas de multiplicacion de {n} son: ")
for i in range (1,11):
    print(f"{n} x {i} = {n*i}")

