from linked_stack_ext_abstract import LinkedStackExtAbstract
from data_structures import LinkedStack
from typing import Any,List
from data_structures import ListNode

class LinkedStackExt(LinkedStackExtAbstract,LinkedStack):
    def multi_pop(self, num: int) -> List[Any]:
        if num < 0:
            raise ValueError("El parametro no puede ser negativo")
        lista = []
        for i in range(num):
         if self.is_empty():
            raise Exception("Accion invalidada,la pila se encuntra vacia")
         lista.append(self.pop())
        return lista
        
     
    
    def replace_all(self, param1: Any, param2: Any) -> None:
        if self.is_empty():
            raise Exception("Accion invalidada,la pila se encuntra vacia")
        nodo_actual = self._head
        #nodo_nuevo = param2
        while nodo_actual is not None:
            if nodo_actual.element == param1:
                nodo_actual.element = param2
            nodo_actual = nodo_actual.next
             
                    
                
            
    
    def __imul__(self, other: int) -> None:
       if other < 0:
           raise ValueError("El valor ingresado no puede ser negativo")
       if self.is_empty():
           raise Exception("La pila se encuentra vacia,accion invalida.")
       current = self._head
       elements = []
        
       while current:
            elements.append(current.element)
            current = current.next
       for i in range(other):
            for item in elements:
                self.push(item)
       return None
           
               