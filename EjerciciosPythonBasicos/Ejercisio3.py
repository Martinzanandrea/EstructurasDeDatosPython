"""Escriba un programa que exija al usuario el ingreso de:
a) 2 números enteros y determine el mayor.
b) 3 números enteros y determine el mayor.
c) N números enteros y determine el mayor (no usar colecciones)."""

#inicio
numeros = int(input("Ingrese la cantidad de enteros a comparar:  "))
mayor = None
for i in range(numeros):
    Numero = int(input(f"Ingrese el numero entero {i+1}: "))
    if (mayor is None) or (Numero > mayor) :
        mayor = Numero

print("El Numero mayor es :", mayor)        
    

    

    