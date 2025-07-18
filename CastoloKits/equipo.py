from liga import Liga

class Equipo:
    def __init__(self, nombre: str, liga: Liga):
        self.nombre = nombre
        self.liga = liga

    def __str__(self) -> str:
        return f"{self.nombre}"  # Solo muestra el nombre del equipo

    def __repr__(self) -> str:
        return f"Equipo(nombre={self.nombre}, liga={self.liga})"

