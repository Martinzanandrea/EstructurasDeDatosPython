
from linked_deque import LinkedDeque
lista = LinkedDeque()
"Agregamos algunos elementos al principio de la deque:"
lista.add_first(5)
lista.add_first(4)
lista.add_first(3)
lista.add_first(2)
lista.add_first(1)
"Agregamos algunos elementos al final de la deque:"
lista.add_last(6)
lista.add_last(7)
lista.add_last(8)
lista.add_last(9)
lista.add_last(10)

#Deque luego de los elementos agregados:
print('Deque original:')
print(lista)

#Longitud de la deque:
len = lista.__len__()
print(f"Cantidad total de elementos: {len}")

#Muestra el primer elemento de la deque:
first = lista.first()
print(f"Primer elemento de la deque: {first}")

#Muestra el ultimo elemento de la deque:
last = lista.last()
print(f"Ultimo elemento de la deque: {last}")

#Eliminacion del primer elemento de la deque:
lista.delete_first()
#Eliminacion del ultimo elemento de la deque:
lista.delete_last()
"Impresion de la deque sin los elementos:"
print('Deque luego de la eliminacion')
print(lista)
#Deque vacia?
print(f"La deque se encuentra vacia?:{lista.is_empty()}")
