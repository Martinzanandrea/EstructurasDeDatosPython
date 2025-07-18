from camisetaenum import CamisetaEnum
from equipenum import EquipacionTipoEnum
from equipo import Equipo
from liga import Liga
from temporada import Temporada
from castolo_admin import CastoloAdmin
from camiseta import Camiseta
#Creamos las siguientes funciones para mejorar la salida
def formato_camiseta(camiseta):
    return f"SKU: {camiseta.sku}, Equipo: {camiseta.equipo}, Liga: {camiseta.liga}, " \
           f"Tipo: {camiseta.camiseta_tipo}, Equipación: {camiseta.equipacion_tipo}, " \
           f"Cantidad: {camiseta.cantidad}, Precio: {camiseta.precio:.2f}"

def imprimir_lista_camisetas(lista, titulo):
    print(f"\n{'=' * 50}\n{titulo}:")
    if lista:
        for camiseta in lista:
            print(formato_camiseta(camiseta))
    else:
        print("No se encontraron camisetas.")
    print(f"{'=' * 50}")

# Crear instancias de Liga y Equipo
liga_espanola = Liga("Española")
liga_premier = Liga("Premier League")
real_madrid = Equipo("Real Madrid", liga_espanola)
barcelona = Equipo("Barcelona", liga_espanola)
atletico_madrid = Equipo("Atletico Madrid", liga_espanola)
manchester_city = Equipo("Manchester City", liga_premier)

# Crear instancias de Camiseta
camiseta1 = Camiseta(1, real_madrid, liga_espanola, CamisetaEnum(CamisetaEnum.CLUB), EquipacionTipoEnum(EquipacionTipoEnum.LOCAL), True, Temporada(2024), 10, 800.50)
camiseta2 = Camiseta(12, barcelona, liga_espanola, CamisetaEnum(CamisetaEnum.CLUB), EquipacionTipoEnum(EquipacionTipoEnum.VISITANTE), True, Temporada(2024), 15, 700.50)
camiseta3 = Camiseta(13, atletico_madrid, liga_espanola, CamisetaEnum(CamisetaEnum.CLUB), EquipacionTipoEnum(EquipacionTipoEnum.LOCAL), True, Temporada(2024), 0, 400)
camiseta4 = Camiseta(14, manchester_city, liga_premier, CamisetaEnum(CamisetaEnum.CLUB), EquipacionTipoEnum(EquipacionTipoEnum.LOCAL), True, Temporada(2022), 25, 1100.50)

# Crear instancia de CastoloAdmin y agregar camisetas
ejecutar = CastoloAdmin()
ejecutar.append(camiseta1)
ejecutar.append(camiseta2)
ejecutar.append(camiseta3)
ejecutar.append(camiseta4)


# Filtrar por equipación
equip = ejecutar.filtrar_por_equipacion_tipo(EquipacionTipoEnum(EquipacionTipoEnum.LOCAL))
imprimir_lista_camisetas(equip, "Filtrar por equipación Local")

# Filtrar por liga
lig = ejecutar.filtrar_por_liga(Liga("Premier League"))
imprimir_lista_camisetas(lig, "Filtrar por liga Premier League")

# Filtrar temporada actual
temp = ejecutar.filtrar_temporada_actual(solo_clubes=True)
imprimir_lista_camisetas(temp, "Filtrar temporada actual (solo clubes)")

# Camiseta más costosa
costosa = ejecutar.mas_costosa()
if costosa:
    print("\nLa camiseta más costosa es:")
    print(formato_camiseta(costosa))
else:
    print("No se encontró ninguna camiseta.")

# Camisetas sin stock
stock = ejecutar.stock_agotado()
imprimir_lista_camisetas(stock, "Camisetas sin stock")

# Totales por liga
tot = ejecutar.totales_por_liga()
print("\nTotales por liga:")
if tot:
    for liga, total in tot.items():
        print(f"{liga}: {total} camisetas")
else:
    print("No se encontraron totales por liga.")
