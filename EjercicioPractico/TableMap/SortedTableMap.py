from SortedTableMapAbstract import SortedTableMapAbstract
from data_structures import MapBase
from typing import List,Any,Generator
class SortedTableMap(SortedTableMapAbstract,MapBase):
    def __init__(self) -> None:
        self._table: List[MapBase._Item] = []
    
    def __len__(self) -> int:
        return len(self._table)
    pass
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
       return ','.join(str(elemento) for elemento in self._table)
    
    
    def __getitem__(self, k: Any) -> Any:
        low_element = 0
        high_element = len(self._table) - 1
        while low_element <= high_element:
            mid = (low_element + high_element) // 2
            if self._table[mid]._key == k:
                return self._table[mid]._value
            elif self._table[mid]._key < k:
                low_element= mid + 1
            else:
                high_element= mid - 1
        raise KeyError(f'Clave {k} no encontrada en el Mapeo.')
    
    def __setitem__(self, k: Any, v: Any) -> None:
        if k is None:
            raise ValueError('Key invalida')
        if v is None:
            raise ValueError('Elemento invalido')
        low_element= 0
        high_element = len(self._table) - 1
        while low_element <= high_element:
            mid = (low_element + high_element) // 2 #Busqueda binaria
            if self._table[mid]._key == k:
                self._table[mid]._value = v
                return
            elif self._table[mid]._key < k:
                low_element = mid + 1
            else:
                high_element = mid - 1
        self._table.insert(low_element, self._Item(k, v))
    
    def __delitem__(self, k: Any) -> None:
        low_element = 0
        high_element = len(self._table) - 1
        while low_element <= high_element:
            mid = (low_element + high_element) // 2
            if self._table[mid]._key == k:
                self._table.pop(mid)
                return
            elif self._table[mid]._key < k:
                low_element = mid + 1
            else:
                high_element = mid - 1
        raise KeyError(f'Clave {k} no encontrada en el Mapeo.')
    
    
    def __iter__(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield item._key

    def iter_items(self) -> Generator[Any, None, None]:
         for item in self._table:
            yield item._value
