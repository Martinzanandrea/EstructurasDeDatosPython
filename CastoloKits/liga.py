class Liga:
    def __init__(self, nombre_lig: str):
        self.nombre_lig = nombre_lig

    def __str__(self) -> str:
        return f"{self.nombre_lig}"

    def __repr__(self) -> str:
        return f"Liga(nombre_lig={self.nombre_lig})"

    
