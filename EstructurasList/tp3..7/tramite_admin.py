from tramite import Tramite
from linked_queue_ext import LinkedQueueExt
import sqlite3


class TramitesAdmin:
    def __init__(self, db_name='tramites.db'):
        self.db_name = db_name
        self.queue = LinkedQueueExt()
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tramites (
                    numero INTEGER PRIMARY KEY,
                    apellido TEXT NOT NULL,
                    nombre TEXT NOT NULL,
                    requerimiento TEXT NOT NULL,
                    terminada INTEGER NOT NULL
                )
            ''')
            conn.commit()

    def add(self, tramite:Tramite):
        self.queue.enqueue(tramite)
        #self.persist()

    def remove(self):
        if not self.queue.is_empty():
            tramite = self.queue.dequeue()
            self.persist()
            return tramite
        else:
            raise IndexError("No hay trámites para quitar.")

    def list(self):
        return self.queue.list()

    def persist(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tramites')  # Limpiar la tabla
            for tramite in self.queue:
                cursor.execute('INSERT OR REPLACE INTO tramites VALUES (?, ?, ?, ?, ?)', tramite.to_db_tuple())
            conn.commit()

    def load(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tramites')
            for row in cursor.fetchall():
                self.queue.enqueue(Tramite.from_db_row(row))
                
    def list(self):
     elementos = []
     current = self.queue.front
     while current:
        elementos.append(current.element)  # Agrega cada elemento a la lista
        current = current.next
     return elementos
                
                
   