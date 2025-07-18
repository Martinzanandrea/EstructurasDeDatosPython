from LinkedBinaryTreeExtAbstract import LinkedBinaryTreeExtAbstract
from data_structures import BinaryTreeNode,LinkedBinaryTree
from typing import Any,List,Optional
from data_structures import LinkedQueue


class LinkedBinaryTreeExt(LinkedBinaryTree,LinkedBinaryTreeExtAbstract):
    def __init__(self):
        """Crea un nuevo árbol binario vacío."""
        self._root: Optional[BinaryTreeNode] = None
        self._size: int = 0
    
    def ancestro_mas_inmediato(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> BinaryTreeNode:
        ancestro = None
        if self.is_empty():
            raise Exception('El arbol se encuentra vacio,accion invalida.')
        if nodo1 is None or nodo2 is None:
            raise Exception("Uno o ambos nodos estan vacios")
        if not self._contains(nodo1) and self._contains(nodo2):
            raise Exception("Uno de los nodos no pertenece a la estructura ")
        camino1 = self._search_parent(nodo1)
        while camino1 is not None:
            camino2 = self._search_parent(nodo2)
            while camino2 is not None:
                if camino1 == camino2:
                        ancestro = camino1
                        return ancestro   
                camino2 = self._search_parent(camino2)
            camino1 = self._search_parent(camino1)
        return None

    
    def hojas(self) -> List[Any]:
        if self.is_empty():
            raise Exception('Arbol vacio,accion invalida.')
        lista = []
        nodo = [self._root]
        while nodo:
            current_node = nodo.pop()
            if current_node.children_count == 0:
                lista.append(current_node.element)
            else:
                if current_node.left_child:
                    nodo.append(current_node.left_child)
                if current_node.right_child:
                    nodo.append(current_node.right_child)                
        return str(lista)
            
    
    def nivel(self, nodo: BinaryTreeNode) -> int:
       if self.is_empty():
           raise Exception('Arbol vacio,accion invalida.')
       if nodo is None:
           raise ValueError('Nodo vacio')
       return buscar_nivel(self._root,nodo,0)
   
    def diametro(self) -> int:
        if not self._root:
            return 0
        cola = [self._root]
        nodos = 0
        while cola:
            tamaño = len(cola)
            nodos = max(nodos,tamaño)
            for i in range(tamaño):
                actual = cola.pop()
                if actual.left_child:
                    cola.append(actual.left_child)
                if actual.right_child:
                    cola.append(actual.right_child)
                
        return nodos      
   
    def es_balanceado(self) -> bool:
      if self.is_empty():
          raise Exception('Arbol vacio,accion invalida.')
      return balanceado(self._root) != -1


def buscar_nivel(actual:BinaryTreeNode,nodo_buscado:BinaryTreeNode,nivel_actual:int):
           if actual is None:
               return -1
           if actual == nodo_buscado:
               return nivel_actual
           nivel_izquierdo = buscar_nivel(actual.left_child,nodo_buscado,nivel_actual+1)
           if nivel_izquierdo != -1:
             return nivel_izquierdo
           return buscar_nivel(actual.right_child,nodo_buscado,nivel_actual+1)
           
def balanceado(nodo:BinaryTreeNode):
    if nodo is None:
        return 0
    izq = balanceado(nodo.left_child)
    der = balanceado(nodo.right_child)
    if (izq == -1 or der == -1):
        return -1
    if abs (izq-der) > 1:
        return -1
    else:
        return True

    