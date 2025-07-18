from data_structures import LinkedList
from typing import Any, List
from linked_list_ext_abstract import LinkedListExtAbstract
from data_structures import LinkedStack
from data_structures import ListNode
class LinkedListExt(LinkedListExtAbstract,LinkedList):
    def __reversed__(self) -> None: 
        if self.is_empty():
            raise Exception("La lista se encuentra vacia")
        stack = LinkedStack()
        current = self._header.next
        while current is not None:
            stack.push(current)
        
        for i in self._size:
            self.add_first(stack.pop())  
          

    def pop(self) -> None: 
        if self.is_empty():
            raise Exception("La  lista se encuentra vacia")
        current = self._header
        while current.next and current.next.next:
            current = current.next
           
        current.next = None
    def add_first(self, other: Any) -> None: 
        if other is None:
            raise ValueError("Debe ingresar algo")
        if self.is_empty():
            raise Exception("La lista se encuentra vacia")
        if other is None:
             raise ValueError("Debe ingresar algo")
        nuevo_nodo = ListNode(other,self._header.next)
        self._header.next = nuevo_nodo
        self._size += 1
        
        
    def __iadd__(self, other: List[Any]) -> None:
        if other is None:
            raise ValueError("Debe ingresar algo")
        if self.is_empty():
            raise Exception("La lista se encuentra vacia")
        for i in other:
            self.add_first(i)
            
            