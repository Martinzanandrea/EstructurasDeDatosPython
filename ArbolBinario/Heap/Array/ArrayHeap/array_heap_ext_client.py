from array_heap_ext import ArrayHeapExt
from data_structures import ArrayHeap
def main():
    heap1 = ArrayHeapExt()
    heap2 = ArrayHeapExt()
    ################
    #Add en heap1
    heap1.add(1,'a')
    heap1.add(2,'b')
    heap1.add(3,'c')
    heap1.add(4,'d')
    heap1.add(5,'e')
    heap1.add(6,'f')
    #Add en heap2
    heap2.add(7,'g')
    heap2.add(8,'h')
    heap2.add(9,'i')
    heap2.add(10,'j')
    heap2.add(11,'k')
    heap2.add(12,'l')
    ##################
    "Metodos:"
    #FUSIONAR 2 HEAPS:
    a = heap1.fusionar(heap2)
    print(f'''Heaps fucionados:
          {heap1}''')
    #CAMBIARLE LA PRIORIDAD A UN NODO:
    b = heap1.cambiar_prioridad(1,13)
    print(f'''Heap con prioridad cambiada: 
          {heap1}''')
    #ELIMINAR POR PRIORIDAD A UN NODO:
    c = heap1.eliminar_por_prioridad(12)
    print(f'''Heap con eliminacion por prioridad:
          {heap1}''')
    #VACIAR HEAP:
    d = heap1.vaciar()
    print(f'''Heap vacio: 
          {heap1}''')
    
if __name__ == '__main__':
        main()

