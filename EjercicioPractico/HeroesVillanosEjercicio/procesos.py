import csv
import re
from data_structures import ProbeHashMap
class SuperHeroesVillanos:
    def __init__(self,archivo:str = 'superheroes_villanos.txt'):
        self.archivo = archivo
        self.herovill = []
        self.superheroes = ProbeHashMap()
        self.villanos = ProbeHashMap()
        
    def leer_archivo(self):
        with open(self.archivo, 'r') as file:
            contenido = file.read()
        self.herovill = re.findall(r'([a-z_*]+)\((.+?)\)',contenido)#Busca todas las coincidencias de la forma: (Nombre_hecho)Nombre_Constante
    def bando(self):
        for hecho,nombre in self.herovill:
            if hecho == 'super_heroe':
                self.superheroes[nombre] = self.superheroes.get(nombre,0)+1
            elif hecho == 'villano':
                self.villanos[nombre] = self.villanos.get(nombre,0)+1
    def contar_bando(self):
        return len(self.superheroes),len(self.villanos)
    def mostar_resultados(self):
        num_heroes,num_villanos = self.contar_bando()
        print(f'Numero de villanos: {num_villanos}')
        print(f'Numero de SuperHeroes: {num_heroes}')

