from enum import Enum

class EquipacionTipoEnum:
    LOCAL = 'Local'
    VISITANTE = 'Visitante'
    TERCERA = 'Tercera'

    def __init__(self, equipacion: str):
        self.equipacion = equipacion

    def __str__(self) -> str:
        return f"{self.equipacion}"

    def __repr__(self) -> str:
        return f"EquipacionTipoEnum(equipacion={self.equipacion})"


