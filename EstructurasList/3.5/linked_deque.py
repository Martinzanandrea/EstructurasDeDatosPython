from typing import Any, Optional
from abc import ABC, abstractmethod
from data_structures import ListNode
from Deque import DequeAbstract

# Implementación de Deque con nodos enlazados
class LinkedDeque(DequeAbstract):
    def __init__(self) -> None:
        """Inicializa una deque vacía."""
        self._front: Optional[ListNode] = None
        self._rear: Optional[ListNode] = None
        self._size = 0

    def __len__(self) -> int:
        """Devuelve la cantidad actual de elementos en la deque."""
        return self._size

    def __str__(self) -> str:
        """Concatena los elementos en la deque en un solo string."""
        elements = []
        actual = self._front
        while actual is not None:
            elements.append(str(actual.element))
            actual = actual.next
        return " <-> ".join(elements)

    def is_empty(self) -> bool:
        """Indica si la deque está vacía."""
        return self._size == 0

    def first(self) -> Any:
        """Devuelve el primer elemento de la deque."""
        if self.is_empty():
            raise Exception("La deque está vacía")
        return self._front.element

    def last(self) -> Any:
        """Devuelve el último elemento de la deque."""
        if self.is_empty():
            raise Exception("La deque está vacía")
        return self._rear.element

    def add_first(self, element: Any) -> None:
        """Agrega un elemento al frente de la deque."""
        nuevo_nodo = ListNode(element)
        if self.is_empty():
            self._front = self._rear = nuevo_nodo
        else:
            nuevo_nodo.next = self._front
            self._front = nuevo_nodo
        self._size += 1

    def add_last(self, element: Any) -> None:
        """Agrega un elemento al final de la deque."""
        nuevo_nodo = ListNode(element)
        if self.is_empty():
            self._front = self._rear = nuevo_nodo
        else:
            self._rear.next = nuevo_nodo
            self._rear = nuevo_nodo
        self._size += 1

    def delete_first(self) -> None:
        """Elimina el primer elemento de la deque."""
        if self.is_empty():
            raise Exception("La deque está vacía")
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1

    def delete_last(self) -> None:
        """Elimina el último elemento de la deque."""
        if self.is_empty():
            raise Exception("La deque está vacía")
        if self._front == self._rear:
            self._front = self._rear = None
        else:
            current = self._front
            while current.next != self._rear:
                current = current.next
            current.next = None
            self._rear = current
        self._size -= 1 
