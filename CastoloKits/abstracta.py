from abc import ABC, abstractmethod
from typing import List, Dict

from camiseta import Camiseta
from equipenum import EquipacionTipoEnum
from liga import Liga

class CastoloAdminAbstract(ABC):

    def __init__(self) -> None:
        """Inicializa la clase con una lista vacía de camisetas."""
        self.lista: List[Camiseta] = []

    def append(self, camiseta: Camiseta) -> None:
        """Agrega una camiseta a la lista de camisetas.

        Args:
            camiseta (Camiseta): La camiseta que se desea agregar a la lista.
        """
        self.lista.append(camiseta)

    def __str__(self) -> str:
        """Concatena en un único str todas la camisetas

        Returns:
            str: Una cadena con las camisetas, separadas por líneas.
        """
        return "\n".join(str(camiseta) for camiseta in self.lista)

    @abstractmethod
    def filtrar_por_liga(self, liga: Liga) -> List[Camiseta]:
        """Filtra las camisetas por liga.

        Args:
            liga (Liga): La liga por la cual se desea filtrar.

        Returns:
            List[Camiseta]: Una lista de camisetas que pertenecen a la liga especificada.
        """
        pass

    @abstractmethod
    def filtrar_por_equipacion_tipo(self, equipacion_tipo: EquipacionTipoEnum) -> List[Camiseta]:
        """Filtra las camisetas por tipo de equipación.

        Args:
            equipacion_tipo (EquipacionTipoEnum): El tipo de equipación por el cual se desea filtrar.

        Returns:
            List[Camiseta]: Una lista de camisetas que corresponden al tipo de equipación especificado.
        """
        pass

    @abstractmethod
    def filtrar_temporada_actual(self, solo_clubes: bool) -> List[Camiseta]:
        """Filtra las camisetas que pertenecen a la temporada actual.

        Args:
            solo_clubes (bool): Si es True, solo filtra camisetas de clubes; si es False, incluye selecciones nacionales.

        Returns:
            List[Camiseta]: Una lista de camisetas que pertenecen a la temporada actual.
        """
        pass

    @abstractmethod
    def stock_agotado(self) -> List[Camiseta]:
        """Devuelve una lista de camisetas que están agotadas en stock.

        Returns:
            List[Camiseta]: Una lista de camisetas con stock agotado.
        """
        pass

    @abstractmethod
    def mas_costosa(self) -> Camiseta:
        """Devuelve la camiseta más costosa de la lista.

        Returns:
            Camiseta: La camiseta más costosa.
        """
        pass

    @abstractmethod
    def totales_por_liga(self) -> Dict[Liga, int]:
        """Devuelve un diccionario con el número total de camisetas por liga.

        Returns:
            Dict[Liga, int]: Un diccionario donde las claves son ligas y los valores el número total de camisetas de cada liga.
        """
        pass
