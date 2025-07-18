from enum import Enum

class CamisetaEnum:
    CLUB = 'Club'
    SELECCION = 'Seleccion'

    def __init__(self, club: str):
        self.club = club

    def __str__(self) -> str:
        return f"{self.club}"

    def __repr__(self) -> str:
        return f"CamisetaEnum(club={self.club})"

