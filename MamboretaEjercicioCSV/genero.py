"""a) Construir las clases que considere necesarias para soportar la información
presentada.

b) Para cada una de las clases del punto anterior defina un constructor
parametrizado y el método __str__().

c) Identifique los campos clave de cada una de las clases y programe el método
__eq__()."""
class Genero:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def __str__(self) -> str:
        return self.nombre

    def __eq__(self, other) -> bool:
        if isinstance(other, Genero):
            return self.nombre == other.nombre
        return False
