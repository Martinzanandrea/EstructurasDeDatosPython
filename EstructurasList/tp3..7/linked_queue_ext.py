from data_structures import ListNode
class LinkedQueueExt:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, item):
        new_node = ListNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("No se puede quitar un trámite la cola se encuentra vacía.")
        removed_data = self.front.element
        self.front = self.front.next
        self.size -= 1
        return removed_data

    def is_empty(self):
        return self.size == 0

    def __iter__(self):
        current = self.front
        while current:
            yield current.element
            current = current.next
            

            
    