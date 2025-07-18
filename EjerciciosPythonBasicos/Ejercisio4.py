"""Escriba una función Python que tome como argumento una secuencia de números
enteros y determine:
a) La sumatoria
b) El promedio.
c) Si todos los números son diferentes entre sí, es decir, si todos los números de
la lista son distintos."""
#inicio
def lista_acciones (parametro):
    
   
    #suma, el metodo sum suma todos los elementos de la lista
    suma = sum(parametro)
    
    #promedio
    prom = suma / len(parametro)
  

    #diferentes entre si
    #len(set(lista)) devuelve si es igual de larga q la org , ya que un conjunto set no admite elem rept
    diferentes = len(parametro) == len(set(parametro))
    return suma , prom , diferentes

lista_oper = list([ 1 , 4 , 5 , 6 , 6 ])
resultado = lista_acciones(lista_oper)
print("la sumatoria total es:" , resultado[0])
print("el promedio es:", resultado[1])
if resultado[2]:
    print("todos los numeros son diferentes entre si")
else:
    print("Hubo coincidencias en los elementos de la lista")


