"""Programe la función es_multiplo(n, m) que tome dos valores enteros como
argumento y retorne True si n es múltiplo de m, esto es, si n = m * i para algún
entero i, y False en caso contrario. Demuestre el correcto funcionamiento de la
función es_multiplo invocándola a través de una aplicación de consola donde el
usuario pueda ingresar datos y visualizar los resultados."""
#inicio
import math
def es_multiplo(n,m):
   if m == 0:
       return False
   else:
       return int(n/m)
def main ():
    n = int(input("Ingrese el valor de n :  "))
    m = int(input("Ingrese el valor de m :  "))
    if es_multiplo(n,m):
        print(f"{n} es multiplo de {m}")
    else:
        print(f"{n} no es multiplo de {m}")
main()
 

        
         