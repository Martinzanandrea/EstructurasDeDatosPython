from data_structures import PriorityQueueBase
from sorted_priority_queue_abstract import SortedPriorityQueueAbstract
from typing import Any,Tuple

class  SortedPriorityQueue (PriorityQueueBase,SortedPriorityQueueAbstract):
    def __init__(self) -> None:
        self.lista= []
        self.dato = PriorityQueueBase()
        
    def __len__(self) -> int:
        return len(self.lista)
       

    def is_empty(self) -> bool:
        return len(self.lista) == 0

    def add(self, k: Any, v: Any) -> None:
        item = self.dato._Item(k,v)
        self.lista.append(item)
        self.lista = ordenar(self.lista)
              
        

    def min(self) -> Tuple[Any]:
        if len(self.lista) == 0:
            raise Exception("Lista vacia , accion invalida")
        minimo = tuple()
        minimo = min(self.lista)
        self.lista =ordenar(self.lista)
        return minimo
            

    def remove_min(self) -> Tuple[Any]:
        if len(self.lista) == 0:
            raise Exception("Lista vacia , accion invalida")
        minimo = tuple()
        minimo = min(self.lista)
        self.lista.remove(minimo)
        self.lista = ordenar(self.lista)
        return minimo
    

    def __str__(self) -> str:
        return ''.join(str(i) for i in self.lista)
    
def ordenar(lista:list):
    return sorted(lista, key=lambda x: x._key)
     
   