from data_structures import ArrayHeap
from ArrayHeapExtAbstract import ArrayHeapExtAbstract
from typing import Any
class ArrayHeapExt(ArrayHeap,ArrayHeapExtAbstract):
        
     
    def fusionar(self, otro: ArrayHeap) -> None:
        if self.is_empty():
            raise Exception('Heap vacio')
        while not otro.is_empty():
            item = otro.remove_min()
            
            
            #item_2 = self.remove_min()
            self._downheap(1)
            self.add(item[0],item[1])
            
            #self._downheap(1)

    def vaciar(self) -> None:
        if self.is_empty():
            raise Exception('Heap vacio')
        while not len(self._data) == 0:
            self._data.pop()
            
            
 
    def eliminar_por_prioridad(self, k: Any) -> None:
        if self.is_empty():
            raise Exception('Heap vacio')
        if k < 0:
            raise ValueError('K debe ser positiva')
        lista = []
        while not len(self._data) == 0:
           item= self.remove_min()
           if k not in item:
            lista.append(item)
            
        for item in lista:
            self._downheap(1)
            self.add(item[0],item[1])
            
 
    def cambiar_prioridad(self, k_actual: Any, k_nueva: Any) -> None:
        if self.is_empty():
            raise Exception('Heap vacio')
        if k_actual or k_actual == None:
            raise ValueError('Las claves no deben ser None')
        if k_actual or k_nueva < 0:
            raise Exception('Las claves deben ser positivas')
        lista = []
        while not self.is_empty():
            item = self.remove_min()
            if k_actual in item:
                if item[0] == k_actual:
                    item = (k_nueva,item[1])
            lista.append(item)
        for item in lista:
            self._downheap(1)
            self.add(item[0],item[1])                