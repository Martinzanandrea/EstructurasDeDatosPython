from data_structures import PriorityQueueBase
from sorted_priority_queue import SortedPriorityQueue
lista = SortedPriorityQueue()
def main():
    #add
    lista.add(1,'a')
    lista.add(2,'b')
    lista.add(4,'c')
    lista.add(3,'d')
    lista.add(5,'e')
    lista.add(6,'f')
    print(lista)
    #is_empty:
    empty = lista.is_empty()
    print (f'True=Vacia,False=Contiene elementos: {empty} ')
    #min:
    minimo = lista.min()
    print (f'Tupla con el elemento de menor valor de clave: {minimo} ')
    #remove_min:
    remove = lista.remove_min()
    print(f'Elemento eliminado: {remove}')
    #lista despues de la eliminacion:
    print(f'cola luego de las modificaciones:{lista}')
    #is_empty:
    empty_act = lista.is_empty()
    print (f'True=Vacia,False=Contiene elementos: {empty_act} ')
    
if __name__ == '__main__':
    main()

