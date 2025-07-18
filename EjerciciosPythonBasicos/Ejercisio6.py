"""Escriba un programa Python que solicite al usuario el nombre de cada país del
continente, su nombre, superficie y cantidad de habitantes. Almacene estos datos
en una lista de elementos de tipo diccionario donde cada entrada tenga las
componentes (pais, superficie y habitantes). A continuación cumplimente los
siguiente incisos:
a) Totalizar la cantidad de habitantes.
b) Superficie total.
c) Obtener el promedio de habitantes.
d) Densidad poblacional de cada pais"""

#inicio
paises = []
"""can_paises = int(input("ingrese la cantidad de paises que exiten en el continente: " ))
for i in range(can_paises):
    pais =  input(f"Ingrese el {i+1}º pais ")           
    superficie = float(input("Ingrese la superficie del pais:  "))
    habitantes = int(input("Ingrese los habitantes del pais:  "))"""
#Intente hacerlo con un for para la cantidad de paises pero no funciono ya que me guardaba solo los datos del ultimo pais ingresado
while True:    
    pais = input("Ingrese el nombre del pais (o 'salir' para terminar ):  ")
    if pais.lower() == 'salir':
        break
    
    
    superficie = float(input("Ingrese la superficie del pais:  "))
    habitantes = int(input("Ingrese la cantidad de habitantes que posee:  "))
    dic_info = {
         "pais" : pais,
         "superficie": superficie,
            "habitantes" : habitantes
     }
    paises.append(dic_info)
total_hab = 0
total_sup = 0

for pais in paises:
    total_sup += pais["superficie"] 
    
    total_hab += pais["habitantes"]
#promhabitantes
prom = total_hab / len(paises) if paises else 0

print(f"Cantidad total de habitantes: {total_hab}")
print(f"Superficie total: {total_sup} ")
print(f"Promedio de habitantes por pais: {prom} ")
print("La densidad poblacional de cada pais es: ")
for pais in paises:
    if pais["superficie"] > 0:
        densidad = pais["habitantes"] / pais["superficie"]
        print(f"La densidad de {pais["pais"]} es : {densidad}")
    else:
        print(f"La densidad de {pais} no se pudo calcular")
