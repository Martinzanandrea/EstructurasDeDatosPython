from abstracta import CastoloAdminAbstract
from typing import List, Dict
from camiseta import Camiseta
from equipenum import EquipacionTipoEnum
from liga import Liga
from temporada import Temporada
from camisetaenum import CamisetaEnum
class CastoloAdmin(CastoloAdminAbstract):

    def filtrar_por_liga(self, liga: Liga) -> List[Camiseta]:
        return [camiseta for camiseta in self.lista if camiseta.liga == liga]

    def filtrar_por_equipacion_tipo(self, equipacion_tipo: EquipacionTipoEnum) -> List[Camiseta]:
        lista_equip: List[Camiseta] = []
        for camiseta in self.lista:
            print(f"Evaluando: {camiseta.equipacion_tipo.equipacion} == {equipacion_tipo.equipacion}")
            if camiseta.equipacion_tipo.equipacion == equipacion_tipo.equipacion:
                lista_equip.append(camiseta)
        return lista_equip



    def filtrar_temporada_actual(self, solo_clubes: bool) -> List[Camiseta]:
        lista_temporada: List[Camiseta] = []
        temporada_actual = 2024  # Asegúrate de que esto sea el año correcto
        for camiseta in self.lista:
            if camiseta.temporada.anio == temporada_actual:
               if solo_clubes:
                    if camiseta.camiseta_tipo == CamisetaEnum.CLUB:
                       lista_temporada.append(camiseta)
            else:
                lista_temporada.append(camiseta)  # Incluye selecciones si es necesario
        return lista_temporada


    def stock_agotado(self) -> List[Camiseta]:
        return [camiseta for camiseta in self.lista if camiseta.cantidad == 0]

    def mas_costosa(self) -> Camiseta:
        return max(self.lista, key=lambda camiseta: camiseta.precio)

    def totales_por_liga(self) -> Dict[Liga, int]:
        diccionario = {}
        for camiseta in self.lista:
            liga = camiseta.liga
            if liga in diccionario:
                diccionario[liga] += 1
        else:
            diccionario[liga] = 1
        return diccionario


