from equipo import Equipo
from camisetaenum import CamisetaEnum
from equipenum import EquipacionTipoEnum
from temporada import Temporada
from liga import Liga

class Camiseta:
    def __init__(self, sku: int, equipo: Equipo, liga: Liga, camiseta_tipo: CamisetaEnum,
                 equipacion_tipo: EquipacionTipoEnum, manga_cortas: bool, temporada: Temporada,
                 cantidad: int, precio: float):
        self.sku = sku
        self.equipo = equipo
        self.liga = liga
        self.camiseta_tipo = camiseta_tipo
        self.equipacion_tipo = equipacion_tipo
        self.manga_cortas = manga_cortas
        self.temporada = temporada
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self) -> str:
        return (f"SKU: {self.sku}, Equipo: {self.equipo}, Liga: {self.liga}, "
                f"Tipo: {self.camiseta_tipo}, Equipación: {self.equipacion_tipo}, "
                f"Cantidad: {self.cantidad}, Precio: {self.precio:.2f}")

    def __repr__(self) -> str:
        return (f"Camiseta(sku={self.sku}, equipo={self.equipo}, liga={self.liga}, "
                f"camiseta_tipo={self.camiseta_tipo}, equipacion_tipo={self.equipacion_tipo}, "
                f"mangas_cortas={self.manga_cortas}, temporada={self.temporada}, "
                f"cantidad={self.cantidad}, precio={self.precio:.2f})")


