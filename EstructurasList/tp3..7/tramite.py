


class Tramite:
    def __init__(self, numero: int, apellido: str, nombre: str, requerimiento: str, terminada: int = 1):
        self.numero = numero
        self.apellido = apellido
        self.nombre = nombre
        self.requerimiento = requerimiento
        self.terminada = int(terminada)  

    def __eq__(self, other):
        if not isinstance(other, Tramite):
            return NotImplemented
        return self.numero == other.numero

    def __str__(self) :
        estado = "Terminada" if self.terminada else "Pendiente"
        return f"Trámite {self.numero}: {self.apellido}, {self.nombre}, Requerimiento: {self.requerimiento}, Estado: {self.terminada}"

    def to_db_tuple(self):
        return (self.numero, self.apellido, self.nombre, self.requerimiento, self.terminada)

    @classmethod
    def from_db_row(cls, row):
        return cls(row[0], row[1], row[2], row[3],)
    
    def __repr__(self) -> str:
        return self.__str__()