"""Programe la función min_max(data) que tome una secuencia de uno o más
números y retorne el menor y el mayor de ellos en una tupla de dos posiciones de
longitud. No utilizar la función min o max para solucionar este ejercicio."""
#inicio
def min_max(data):
    if not data:
        return None
    mayor = data[0]
    menor = data[0]
    for i in data: #i representa el numero donde esta parado,por lo tanto compara con dicho numero
        if i > mayor:
            mayor = i
        if i < menor:
                menor = i
    return mayor , menor
resultado = min_max([1,4,6,7,9,45])
print(resultado)
